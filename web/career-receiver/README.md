# Career experience React receiver

Build offline using the existing scene-browser dependencies:

```powershell
node ../scene-browser/node_modules/vite/bin/vite.js build --outDir dist-v006
```

Copy the successful `dist-v006/` to the final WebGL output's `receiver/`. Serve the build using HTTP and open `/receiver/`. It loads `../index.html` from the same origin. No CDN is required. Earlier `dist/` was an unsuccessful intermediate dependency-resolution attempt; use the versioned successful bundle.

The example starts only PAN-001 / career-net-253-office-documents v002, awaits and stores the actual end response, deduplicates original event IDs, sorts sequence, requests replay, and records delivery unconfirmed after a 30-second timeout. Same-ID retry is available. Observed in-game end receipts are accepted. On reload, preserved nonterminal records are shown as unknown/unconfirmed interruption, never invented user abort or restored game completion.

Source of truth: ../../AGENTS.md. Detailed Korean integration notes: ../../docs/human/integrations/workplace-runtime-protocol-v001.md. A successful Vite build and mocked adapter checks do not prove Unity/React runtime integration; see actual final build evidence separately.
