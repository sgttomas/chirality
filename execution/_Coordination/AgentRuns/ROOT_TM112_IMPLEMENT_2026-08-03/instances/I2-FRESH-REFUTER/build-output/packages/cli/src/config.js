import { homedir } from "node:os";
import { join, resolve } from "node:path";
export function resolveCliRuntimePaths(environment = process.env, homeDirectory = homedir()) {
    const userData = resolve(environment["CHIRALITY_USER_DATA"] ??
        join(homeDirectory, "Library", "Application Support", "Chirality"));
    const runtimeDirectory = join(userData, "runtime");
    return {
        userData,
        runtimeDirectory,
        socketPath: resolve(environment["CHIRALITY_RUNTIME_SOCKET_PATH"] ??
            join(runtimeDirectory, "control.sock")),
        tokenFile: resolve(environment["CHIRALITY_RUNTIME_TOKEN_FILE"] ??
            join(runtimeDirectory, "auth", "tokens", "operator.token")),
        launchAgentsDirectory: resolve(environment["CHIRALITY_LAUNCH_AGENTS_DIRECTORY"] ??
            join(homeDirectory, "Library", "LaunchAgents"))
    };
}
export function runtimeClientOptions(paths) {
    return {
        socketPath: paths.socketPath,
        tokenFile: paths.tokenFile
    };
}
