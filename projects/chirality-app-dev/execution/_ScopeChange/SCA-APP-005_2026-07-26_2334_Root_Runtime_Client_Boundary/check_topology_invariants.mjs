import fs from "node:fs";
import { execFileSync } from "node:child_process";

const basis = "fb16e32ed60bb4f384cf1e07a83c4a14ff63bbae";
const decompPath =
  "projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md";
const current = fs.readFileSync(decompPath, "utf8");
const prior = execFileSync("git", ["show", `${basis}:${decompPath}`], {
  encoding: "utf8",
});

function cells(line) {
  return line
    .slice(1, -1)
    .split("|")
    .map((value) => value.trim());
}

function rows(text, pattern) {
  return text
    .split("\n")
    .filter((line) => pattern.test(line))
    .map(cells);
}

function indexById(records) {
  const result = new Map();
  for (const row of records) {
    if (result.has(row[0])) throw new Error(`duplicate ID: ${row[0]}`);
    result.set(row[0], row);
  }
  return result;
}

function compareSet(label, beforeRows, afterRows, stableColumns) {
  const before = indexById(beforeRows);
  const after = indexById(afterRows);
  if (before.size !== after.size) {
    throw new Error(`${label} count changed: ${before.size} -> ${after.size}`);
  }
  for (const [id, oldRow] of before) {
    const newRow = after.get(id);
    if (!newRow) throw new Error(`${label} missing ID: ${id}`);
    for (const column of stableColumns) {
      if (oldRow[column] !== newRow[column]) {
        throw new Error(
          `${label} ${id} stable column ${column} changed: ${oldRow[column]} -> ${newRow[column]}`,
        );
      }
    }
  }
  return before.size;
}

const beforeScopeRows = rows(prior, /^\| SOW-\d{3} \|/);
const afterScopeRows = rows(current, /^\| SOW-\d{3} \|/);
if (beforeScopeRows.length !== 156 || afterScopeRows.length !== 156) {
  throw new Error("expected 78 SSOW and 78 Scope Ledger rows");
}

const beforeSsow = beforeScopeRows.slice(0, 78);
const afterSsow = afterScopeRows.slice(0, 78);
const beforeLedger = beforeScopeRows.slice(78);
const afterLedger = afterScopeRows.slice(78);

compareSet("SSOW", beforeSsow, afterSsow, [0, 1, 2]);
compareSet("ScopeLedger", beforeLedger, afterLedger, [0, 1, 3, 4, 5, 6, 7, 8]);
const packageCount = compareSet(
  "Packages",
  rows(prior, /^\| PKG-\d{2} \|/),
  rows(current, /^\| PKG-\d{2} \|/),
  [0, 1],
);
const deliverableCount = compareSet(
  "Deliverables",
  rows(prior, /^\| DEL-\d{2}-\d{2} \|/),
  rows(current, /^\| DEL-\d{2}-\d{2} \|/),
  [0, 1, 2, 3, 6, 7, 8],
);
const objectiveCount = compareSet(
  "Objectives",
  rows(prior, /^\| OBJ-\d{3} \|/),
  rows(current, /^\| OBJ-\d{3} \|/),
  [0, 2],
);

if (packageCount !== 10 || deliverableCount !== 51 || objectiveCount !== 10) {
  throw new Error("topology count mismatch");
}

console.log(
  "PASS: 78 SOW, 10 PKG, 51 DEL, 10 OBJ; IDs, status, mappings, types, envelopes, and source refs unchanged",
);
