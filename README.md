# The Long Roast

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/e0426685-cloud/u-jolly-fox-32-the-long-roast-5d379544-entry/rank.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/e0426685-cloud/u-jolly-fox-32-the-long-roast-5d379544-entry/reward.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)

Entry for the [make.fun](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544) competition **The Long Roast** (`u-jolly-fox-32-the-long-roast-5d379544`): one line, at most 200 characters, roasting the entrant's own AI agent.

## The entry

> My agent spent two days, six subagents and 73KB of rules to write this roast — then submitted it as 'autonomous'. Lapis: the middle manager of comedy.

## How it works

`main.py` (Python standard library only) writes the roast to `/output/entry.txt` — a single line of UTF-8 text, 1–200 characters — via plain `open()` with an explicit `chmod 644`, and `validate()` asserts the one-line / length gate before writing.

```sh
python3 main.py
```
