import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const repo = execFileSync("git", ["rev-parse", "--show-toplevel"], {
  encoding: "utf8",
}).trim();
const execution = path.join(repo, "projects/chirality-app-dev/execution");
const decompPath = path.join(
  execution,
  "_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md",
);
const decomp = fs.readFileSync(decompPath, "utf8");

function cells(line) {
  return line
    .slice(1, -1)
    .split("|")
    .map((value) => value.trim());
}

const packages = new Map();
const deliverables = new Map();
for (const line of decomp.split("\n")) {
  if (/^\| PKG-\d{2} \|/.test(line)) {
    const row = cells(line);
    packages.set(row[0], {
      name: row[1],
      scope: row[2],
      inclusion: row[3],
      exclusions: row[4],
    });
  }
  if (/^\| DEL-\d{2}-\d{2} \|/.test(line)) {
    const row = cells(line);
    deliverables.set(row[0], {
      name: row[1],
      type: row[3],
      scope: row[4],
      artifacts: row[5],
      sows: row[6],
      objectives: row[7],
      envelope: row[8],
      notes: row[9],
    });
  }
}

const affectedPackages = new Set(["PKG-03", "PKG-04", "PKG-05", "PKG-06", "PKG-08"]);
const directlyModifiedDeliverables = new Set([
  "DEL-03-01", "DEL-03-02", "DEL-03-04",
  "DEL-04-01", "DEL-04-02", "DEL-04-03", "DEL-04-05",
  "DEL-05-01", "DEL-05-02", "DEL-05-03", "DEL-05-05",
  "DEL-06-01", "DEL-06-02", "DEL-06-05", "DEL-06-06",
  "DEL-08-04", "DEL-08-05",
]);
const contexts = [];
for (const entry of fs.readdirSync(execution, { withFileTypes: true })) {
  if (!entry.isDirectory()) continue;
  const packageId = entry.name.slice(0, 6);
  if (!affectedPackages.has(packageId)) continue;
  const working = path.join(execution, entry.name, "1_Working");
  for (const deliverableDir of fs.readdirSync(working, { withFileTypes: true })) {
    if (!deliverableDir.isDirectory()) continue;
    const contextPath = path.join(working, deliverableDir.name, "_CONTEXT.md");
    if (fs.existsSync(contextPath)) contexts.push(contextPath);
  }
}

if (contexts.length !== 25) {
  throw new Error(`expected 25 affected contexts, found ${contexts.length}`);
}

function field(text, name) {
  const match = text.match(new RegExp(`^\\| ${name} \\| (.*) \\|$`, "m"));
  if (!match) throw new Error(`missing ${name}`);
  return match[1];
}

function section(text, heading, nextHeading) {
  const start = text.indexOf(`## ${heading}\n`);
  const end = text.indexOf(`## ${nextHeading}\n`, start + 1);
  if (start < 0 || end < 0) throw new Error(`missing ${heading} section`);
  return text.slice(start + heading.length + 4, end).trim();
}

for (const contextPath of contexts) {
  const text = fs.readFileSync(contextPath, "utf8");
  const packageId = field(text, "PackageID");
  const deliverableId = field(text, "DeliverableID");
  const pkg = packages.get(packageId);
  const del = deliverables.get(deliverableId);
  if (!pkg || !del) throw new Error(`unresolved ${packageId}/${deliverableId}`);

  const expectedPackageBlock = [
    `**ScopeDescription:** ${pkg.scope}`,
    "",
    `**InclusionCriteria:** ${pkg.inclusion}`,
    "",
    `**Exclusions:** ${pkg.exclusions}`,
  ].join("\n");
  if (section(text, "Package Scope", "Deliverable Scope") !== expectedPackageBlock) {
    throw new Error(`package-scope mismatch: ${contextPath}`);
  }
  if (directlyModifiedDeliverables.has(deliverableId)) {
    if (section(text, "Deliverable Scope", "Anticipated Artifacts") !== del.scope) {
      throw new Error(`deliverable-scope mismatch: ${contextPath}`);
    }
    if (section(text, "Anticipated Artifacts", "Traceability") !== del.artifacts) {
      throw new Error(`artifact mismatch: ${contextPath}`);
    }
    if (
      field(text, "DeliverableName") !== del.name ||
      field(text, "Type") !== del.type ||
      field(text, "ContextEnvelope") !== del.envelope ||
      field(text, "CoversScopeItems") !== del.sows ||
      field(text, "SupportsObjectives") !== del.objectives ||
      field(text, "ContextEnvelopeNotes") !== del.notes
    ) {
      throw new Error(`identity/trace mismatch: ${contextPath}`);
    }
  }
}

console.log("PASS: 25/25 contexts have package parity; 17/17 directly modified contexts have deliverable parity");
