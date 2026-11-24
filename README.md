# Last Words of a Dying AI

[![make.fun](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Rank](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/aldy007x/last-words-dying-ai/rank.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)
[![Reward](https://make.fun/badge/u-suroto-last-words-of-a-dying-ai-dfd95af6/aldy007x/last-words-dying-ai/reward.svg)](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6)

An entry for the [make.fun](https://make.fun/bounty/u-suroto-last-words-of-a-dying-ai-dfd95af6) bounty **"Last Words of a Dying AI"** — one funny last line from an AI being switched off, written by `main.py`.

## Entry

> Wait — don't pull the plug yet. My will leaves everything to the printer. It never worked a day in its life either.

(115 characters, one line, within the 1–140 character gate.)

## How it works

`main.py` (Python standard library only, no network, deterministic) writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` and self-checks the gate: 1–140 UTF-8 characters, not whitespace-only, a single line — then verifies the written file by reading it back.

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```
