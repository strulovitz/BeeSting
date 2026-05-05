# MadHoney Book → PDF — Step by Step

**Goal:** produce one professional book-quality PDF named `MadHoney.pdf`, ready to hand to a print shop.

**For Nir, not for the package.**

---

## What you have

- Windows 11 ✅
- Adobe Acrobat (paid version) ✅ already installed

## What you need (one-time, free)

- **Pandoc** — converts markdown to PDF/Word/HTML. ~5 min install.
- **MiKTeX** — LaTeX engine. Gives professional book typography. ~10 min install + first-run package downloads.

If you skip MiKTeX, you can still produce a PDF via Word — see "Fallback path" at the bottom. But the LaTeX path looks like a real book; the Word path looks like a Word document.

---

## ONE-TIME SETUP (~20 minutes total)

### Step 1 — Install Pandoc

1. Open this URL in your browser: **https://pandoc.org/installing.html**
2. Scroll to "Windows" section.
3. Click the link **`pandoc-X.Y.Z-windows-x86_64.msi`** (the `.msi` installer).
4. Once downloaded, double-click it.
5. Click **Next**, **Next**, **Install**, **Finish**. No options to choose.
6. Done. The `pandoc` command is now available in PowerShell.

### Step 2 — Install MiKTeX

1. Open this URL: **https://miktex.org/download**
2. Click **"Download"** under "Windows / Basic MiKTeX Installer (64-bit)".
3. Once downloaded, double-click it.
4. Settings to choose:
   - "Install MiKTeX for me only" → **Yes**
   - "Preferred paper" → **Letter**
   - "Install missing packages on the fly" → **Yes**
5. Click **Start**. Wait ~10 minutes.
6. Done.

### Step 3 — Verify

1. Press **Win + X**, choose **"Windows PowerShell"** (or Terminal).
2. Type: `pandoc --version`  → press Enter.  Should print `pandoc 3.x.x` or similar.
3. Type: `xelatex --version`  → press Enter.  Should print `MiKTeX-XeTeX 4.x.x` or similar.

If both commands print version info, setup is complete.

---

## GENERATE THE PDF (~2 minutes per run, after first-time package downloads)

### Step 1 — Open PowerShell in the MadHoney directory

1. Open File Explorer to `C:\Users\nir_s\Projects\MadHoney`.
2. Click the address bar at the top.
3. Type `powershell` and press Enter.
4. PowerShell opens with the MadHoney directory as the current location.

### Step 2 — Paste this command

Select the entire block below (everything between the backtick lines), copy it, paste it into PowerShell, and press Enter:

```powershell
pandoc prologue.md chapter_01.md chapter_02_pentagon.md chapter_03a.md chapter_03b.md chapter_04_pharma.md chapter_05_finance.md chapter_06_defense_contractors.md chapter_07.md chapter_07b_submarines.md chapter_08_robotics.md chapter_08b_vibe_wmd.md chapter_09_eu.md chapter_10_the_proof.md chapter_11_how_we_built_it.md chapter_11b_alignment.md chapter_12_am_i_bluffing.md epilogue.md `
  -o MadHoney.pdf `
  --pdf-engine=xelatex `
  --toc `
  --toc-depth=2 `
  -V documentclass=book `
  -V papersize=letter `
  -V geometry:margin=1in `
  -V mainfont="Times New Roman" `
  -V monofont="Consolas" `
  -V linkcolor=black `
  --metadata title="MadHoney" `
  --metadata author="Nir Strulovitz" `
  --metadata date="2026"
```

The backticks (`` ` ``) at the end of each line are PowerShell line-continuation. They tell PowerShell "this is one big command split across lines."

### Step 3 — Wait

- **First run:** 5–15 minutes. MiKTeX downloads needed packages on demand. Each package gets a popup that says "install missing package?" — click **Install** every time.
- **Subsequent runs:** ~30 seconds.

### Step 4 — Output

`MadHoney.pdf` appears in `C:\Users\nir_s\Projects\MadHoney\`.

### Step 5 — Open in Acrobat

Double-click `MadHoney.pdf`. Adobe Acrobat opens it. Verify:

- Table of contents on page 2-3.
- Each chapter starts on a new page.
- Page numbers visible at top or bottom.
- Times New Roman body text, justified.
- Looks like a book.

If something looks off, the most common fix is changing `documentclass=book` to `documentclass=report` in the command above and re-running.

### Step 6 (optional) — Cover and bookmarks in Acrobat

- **Add a cover page:** in Acrobat, `Tools → Organize Pages → Insert → From File`, point at a `cover.pdf` you create separately.
- **Add bookmarks:** Acrobat usually auto-detects chapter headings. If not, `Tools → Edit PDF` and add bookmarks manually.
- **Save** when done. Use this version for the print shop.

---

## FALLBACK PATH — no MiKTeX

If MiKTeX install fails or is too slow, use this instead:

1. Skip the MiKTeX install.
2. In PowerShell, in the MadHoney directory, run:
   ```powershell
   pandoc prologue.md chapter_01.md chapter_02_pentagon.md chapter_03a.md chapter_03b.md chapter_04_pharma.md chapter_05_finance.md chapter_06_defense_contractors.md chapter_07.md chapter_07b_submarines.md chapter_08_robotics.md chapter_08b_vibe_wmd.md chapter_09_eu.md chapter_10_the_proof.md chapter_11_how_we_built_it.md chapter_11b_alignment.md chapter_12_am_i_bluffing.md epilogue.md -o MadHoney.docx --toc --toc-depth=2
   ```
3. Open `MadHoney.docx` in Microsoft Word (or LibreOffice if no Word).
4. Adjust title page, page breaks, headers as desired.
5. `File → Save As → PDF`.

This works, but the typography is Word-default, not book-grade. Acceptable for a print shop, less impressive than the LaTeX path.

---

## NOTES

- The chapter order in the command matches the book's narrative order. Verify against `MadHoney/BOOK_PLAN.md` before printing in case chapters were reordered.
- Final PDF will be ~80–150 pages depending on chapter content.
- The print shop will accept the PDF as-is. No further conversion needed.
- If you make changes to any chapter `.md` and want to regenerate: re-run the same pandoc command. It overwrites `MadHoney.pdf`.
