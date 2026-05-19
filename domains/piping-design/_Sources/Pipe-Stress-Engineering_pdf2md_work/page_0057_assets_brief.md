PURPOSE: Identify extractable prose-document assets on one PDF page
RequestedBy: PDF2MD

ScopePath: /Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/piping-design/_Sources/Pipe-Stress-Engineering_pdf2md_work
TaskSkill: pdf2md-page-assets

Tasks:
  - Read one page raster and its clean Markdown context
  - Identify visible figures, tables, and other meaningful images
  - Emit bbox-normalized asset candidates and table CSV text per the skill contract

ApplyEdits: true

AllowedWriteTargets:
  - "/Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/piping-design/_Sources/Pipe-Stress-Engineering_pdf2md_work/page_0057_assets.json"

RuntimeOverrides:
  IMAGE_PATH: /Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/piping-design/_Sources/Pipe-Stress-Engineering_pdf2md_work/page_0057.png
  PAGE_MD_PATH: /Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/piping-design/_Sources/Pipe-Stress-Engineering_pdf2md_work/page_0057.md
  OUTPUT_PATH: /Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/piping-design/_Sources/Pipe-Stress-Engineering_pdf2md_work/page_0057_assets.json
  DOC_STEM: Pipe-Stress-Engineering
  PAGE_NUM: 57
  TOTAL_PAGES: 506
  ASSET_POLICY: prose-document-assets-v1

CustomInstructions:
  - The output JSON contract is strict. Use these EXACT field names and string literals;
    do not substitute synonyms or restructure:
    * Top-level fields: schema_version, run_status, doc_stem, page, total_pages,
      asset_policy, assets, issues. The page-number field is page (NOT page_num).
    * schema_version MUST be the literal "pdf2md-page-assets/v1".
    * run_status MUST be one of the four uppercase literals: SUCCESS, NO_ASSETS, FAILED,
      FAILED_INPUTS. Do not use lowercase "ok" or any other value.
    * assets is a flat array. Do NOT add a sibling tables/figures/images array; tables
      are entries inside assets with kind="tbl".
    * Per-asset kind MUST be one of three 3-letter literals: "fig", "tbl", "img". Do NOT
      use "figure", "image", "table", "diagram", "plot", "chart", "logo", "photo", etc.
    * Per-asset bbox_norm MUST be a 4-element JSON array [x0, y0, x1, y1]. Do NOT emit
      an object {"x0": ..., "y0": ..., "x1": ..., "y1": ...}.
    * Captions go in the "caption" field (NOT "label", "title", or "name").
  - bbox_norm MUST generously include the full asset, the visible caption, AND ~3-5% of
    surrounding page whitespace. Clipped figures or truncated captions are defects; a
    little extra whitespace around the asset is preferable.

ExpectedOutputs:
  - /Users/ryan/ai-env/projects/chirality-app-test/domain-test/domains/piping-design/_Sources/Pipe-Stress-Engineering_pdf2md_work/page_0057_assets.json

