// Entry point for the news-image-20261121 submission.
//
// The deliverable image is entry.png beside this file: a one-page
// newspaper of Saturday 21 November 2026, drawn entirely in code by
// the Python program in this repository (render.py, scenes.py,
// draw.py, data.py) at 2048px and exported at 1024px. This program
// only moves those exact bytes where the grader expects them:
// /output/entry.png, or MAKEFUN_OUTPUT_DIR/entry.png when that
// variable is set outside the grader's container. It reads the bytes
// back after writing and refuses to finish silently when the copy
// is short. Standard library only, no network, same bytes on every run.
import { mkdirSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const hereDir = dirname(fileURLToPath(import.meta.url));
const bundledPng = join(hereDir, 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destination = join(outputDir, 'entry.png');

mkdirSync(outputDir, { recursive: true });
const pngBytes = readFileSync(bundledPng);
writeFileSync(destination, pngBytes);
const copiedBytes = statSync(destination).size;
if (copiedBytes !== pngBytes.length) {
  throw new Error(
    `entry.png copy short: wrote ${copiedBytes} of ${pngBytes.length} bytes`,
  );
}
