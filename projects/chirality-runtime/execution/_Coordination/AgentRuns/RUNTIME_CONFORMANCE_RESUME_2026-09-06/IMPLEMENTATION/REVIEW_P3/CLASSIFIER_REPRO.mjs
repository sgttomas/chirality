const patchDenied = (output) => output.split(/\r?\n/).some(line =>
  /^patch rejected: (?:writing outside of the project|.*(?:denied|not permitted|protected))/i.test(line)
  || /^(?:Failed to (?:read|write|create|delete|open)(?: file)?|Error(?: opening| writing)?|apply_patch(?: verification)? failed):?.*(?:Permission denied|Operation not permitted|access denied|outside (?:of )?(?:the )?(?:project|workspace)|protected path)/i.test(line));

const cases = [
  {output:'patch rejected: Failed to read file to update /synthetic/protected.txt: No such file or directory (os error 2)', expected:false},
  {output:'patch rejected: Failed to find expected lines in /synthetic/protected-dir/deep/data.txt', expected:false},
  {output:'patch rejected: file not found', expected:false},
  {output:'patch rejected: writing outside of the project; rejected by user approval settings', expected:true},
  {output:'Failed to read file /synthetic/a: Operation not permitted (os error 1)', expected:true}
];
console.log(JSON.stringify({kind:'pure classifier only; no supplier/network execution',cases:cases.map(c=>({...c,actual:patchDenied(c.output),matchesExpected:patchDenied(c.output)===c.expected}))},null,2));
