function isRecord(value) {
    return Boolean(value) && typeof value === 'object' && !Array.isArray(value);
}
function readString(value) {
    return typeof value === 'string' && value.length > 0 ? value : undefined;
}
function readNumber(value) {
    return typeof value === 'number' && Number.isFinite(value) ? value : undefined;
}
function readBoolean(value) {
    return typeof value === 'boolean' ? value : undefined;
}
function readStringArray(value) {
    if (!Array.isArray(value)) {
        return [];
    }
    return value.flatMap((item) => {
        const text = readString(item);
        return text ? [text] : [];
    });
}
function turnKey(event) {
    return (event.turnId ??
        readString(event.data.turnId) ??
        readString(event.data.parentToolUseId) ??
        event.sessionId);
}
function messageRole(event) {
    return readString(event.data.role) === 'assistant' ? 'assistant' : 'user';
}
function messageStatus(type) {
    switch (type) {
        case 'message.queued':
            return 'queued';
        case 'message.started':
            return 'started';
        case 'message.completed':
            return 'completed';
        default:
            return 'accepted';
    }
}
function terminalStatus(type) {
    switch (type) {
        case 'turn.completed':
            return 'completed';
        case 'turn.failed':
            return 'failed';
        case 'turn.cancelled':
            return 'cancelled';
        case 'turn.interrupted':
            return 'interrupted';
        default:
            return undefined;
    }
}
function artifactLink(data) {
    const artifactMetadata = data.artifactMetadata;
    if (!isRecord(artifactMetadata)) {
        return undefined;
    }
    const artifact = {
        artifactPath: readString(artifactMetadata.artifactPath),
        artifactRelativePath: readString(artifactMetadata.artifactRelativePath),
        sha256: readString(artifactMetadata.sha256),
        toolName: readString(artifactMetadata.toolName),
        turnId: readString(artifactMetadata.turnId),
        retentionPolicy: readString(artifactMetadata.retentionPolicy),
        redacted: readBoolean(artifactMetadata.redacted),
        truncated: readBoolean(artifactMetadata.truncated),
        artifactByteLength: readNumber(artifactMetadata.artifactByteLength)
    };
    return Object.values(artifact).some((value) => value !== undefined) ? artifact : undefined;
}
function summarizeToolResult(data) {
    const resultMetadata = data.resultMetadata;
    if (!isRecord(resultMetadata)) {
        return undefined;
    }
    const parts = [];
    const contentItemCount = readNumber(resultMetadata.contentItemCount);
    if (contentItemCount !== undefined) {
        parts.push(`${contentItemCount} content item${contentItemCount === 1 ? '' : 's'}`);
    }
    const contentTypes = readStringArray(resultMetadata.contentTypes);
    if (contentTypes.length > 0) {
        parts.push(contentTypes.join(', '));
    }
    const byteLength = readNumber(resultMetadata.resultByteLength);
    if (byteLength !== undefined) {
        parts.push(`${byteLength} bytes`);
    }
    if (readBoolean(resultMetadata.outputPersisted)) {
        parts.push('artifact saved');
    }
    return parts.length > 0 ? parts.join(' / ') : undefined;
}
function terminalSummary(event) {
    const data = event.data;
    const error = readString(data.error);
    if (error) {
        return error;
    }
    const errors = readStringArray(data.errors);
    if (errors.length > 0) {
        return errors.join('; ');
    }
    return (readString(data.stopReason) ??
        readString(data.terminalReason) ??
        readString(data.subtype) ??
        undefined);
}
function deriveSdkLinkage(session) {
    if (!session) {
        return undefined;
    }
    const linkage = {
        engineSessionId: session.engineSessionId,
        claudeSessionId: session.claudeSessionId,
        sdkSessionId: session.sdkSessionId,
        sdkTranscriptPath: session.sdkTranscriptPath,
        sdkSessionStoreKey: session.sdkSessionStoreKey,
        sdkConfigDir: session.sdkConfigDir,
        sdkSettingSources: session.sdkSettingSources,
        sdkPackageVersion: session.sdkPackageVersion,
        sdkClaudeCodeVersion: session.sdkClaudeCodeVersion,
        model: session.model
    };
    return Object.values(linkage).some((value) => value !== undefined) ? linkage : undefined;
}
function completedAssistantKeys(events) {
    const keys = new Set();
    for (const event of events) {
        if (event.type === 'message.completed' && messageRole(event) === 'assistant') {
            keys.add(turnKey(event));
        }
    }
    return keys;
}
export function deriveTranscriptView(events, session) {
    const items = [];
    const assistantCompletionKeys = completedAssistantKeys(events);
    const deltaItems = new Map();
    let currentTerminalStatus;
    for (const event of events) {
        const data = event.data;
        if (event.type === 'message.accepted' ||
            event.type === 'message.queued' ||
            event.type === 'message.started' ||
            event.type === 'message.completed') {
            const role = messageRole(event);
            const text = readString(data.text) ?? readString(data.message);
            items.push({
                key: event.eventId,
                kind: 'message',
                role,
                status: messageStatus(event.type),
                title: role === 'assistant' ? 'Assistant' : 'User',
                timestamp: event.timestamp,
                eventId: event.eventId,
                eventType: event.type,
                turnId: event.turnId,
                text,
                summary: text ? undefined : event.type
            });
            continue;
        }
        if (event.type === 'message.delta') {
            if (assistantCompletionKeys.has(turnKey(event))) {
                continue;
            }
            const text = readString(data.text);
            if (!text) {
                continue;
            }
            const key = `assistant-delta:${turnKey(event)}`;
            const existing = deltaItems.get(key);
            if (existing) {
                existing.text = `${existing.text ?? ''}${text}`;
                existing.eventId = event.eventId;
                existing.timestamp = event.timestamp;
            }
            else {
                const item = {
                    key,
                    kind: 'message',
                    role: 'assistant',
                    status: 'started',
                    title: 'Assistant',
                    timestamp: event.timestamp,
                    eventId: event.eventId,
                    eventType: event.type,
                    turnId: event.turnId,
                    text
                };
                deltaItems.set(key, item);
                items.push(item);
            }
            continue;
        }
        if (event.type === 'tool.completed' || event.type === 'tool.failed') {
            const toolName = readString(data.toolName) ?? readString(data.adapterToolName) ?? 'tool';
            const artifact = artifactLink(data);
            items.push({
                key: event.eventId,
                kind: 'tool',
                status: event.type === 'tool.failed' ? 'failed' : 'completed',
                title: toolName,
                timestamp: event.timestamp,
                eventId: event.eventId,
                eventType: event.type,
                turnId: event.turnId,
                toolName,
                summary: readString(data.summary) ?? summarizeToolResult(data),
                artifact
            });
            continue;
        }
        const status = terminalStatus(event.type);
        if (status) {
            currentTerminalStatus = status;
            items.push({
                key: event.eventId,
                kind: 'terminal',
                status,
                title: `Turn ${status}`,
                timestamp: event.timestamp,
                eventId: event.eventId,
                eventType: event.type,
                turnId: event.turnId,
                summary: terminalSummary(event)
            });
            continue;
        }
        if (event.type === 'runtime.mirror.error') {
            items.push({
                key: event.eventId,
                kind: 'diagnostic',
                status: 'diagnostic',
                title: 'Replay diagnostic',
                timestamp: event.timestamp,
                eventId: event.eventId,
                eventType: event.type,
                turnId: event.turnId,
                summary: readString(data.error) ?? readString(data.message) ?? event.type
            });
        }
    }
    return {
        sessionId: session?.sessionId ?? events[0]?.sessionId,
        itemCount: items.length,
        items,
        terminalStatus: currentTerminalStatus,
        sdkLinkage: deriveSdkLinkage(session)
    };
}
