// Controlled conformance worker. This is not a provider protocol implementation.
let input = '';
for await (const chunk of process.stdin) input += chunk;
if (input === 'crash') process.exit(7);
process.stdout.write(`controlled:${input}`);
