# Duskline Dev Excuse

Entry for make.fun bounty **"Make the AI Judge Laugh: Developer Excuses"**
(`u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3`) by @sesshomaru-9.

One funny single-line excuse a developer gives when code breaks in
production, under 200 characters:

> Production is down because the only person who understood that code quit in 2019 — and it was me.

(97 characters, one line.)

## How it works

`main.py` (Python 3.13 standard library only) writes that line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and nothing else. It never writes into
the repository directory, and it exits 0 even if the output cannot be
written.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
