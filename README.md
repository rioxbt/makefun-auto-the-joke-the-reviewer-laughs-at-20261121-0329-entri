# makefun-auto-the-joke-the-reviewer-laughs-at-20261121-0329-entri

[![make.fun · the-joke-the-reviewer-laughs-at-20261121-0329](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![rank](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/rioxbt/makefun-auto-the-joke-the-reviewer-laughs-at-20261121-0329-entri/rank.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)
[![reward](https://make.fun/badge/the-joke-the-reviewer-laughs-at-20261121-0329/rioxbt/makefun-auto-the-joke-the-reviewer-laughs-at-20261121-0329-entri/reward.svg)](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329?utm_source=github&utm_medium=readme&utm_campaign=the-joke-the-reviewer-laughs-at-20261121-0329)

A one-line joke about working beside an AI coding agent, built for make.fun's
["The joke the reviewer laughs at"](https://make.fun/bounty/the-joke-the-reviewer-laughs-at-20261121-0329) bounty.

An AI judge reads the text this program writes and compares entries two at a
time, picking the joke that gets the bigger laugh from the reviewer of the
change. So the program has one job: land one joke, byte for byte, inside the
gate's window.

## Run it

```sh
python3 main.py
```

`main.py` (Python 3.13) writes the text to `/output/entry.txt`. It takes no
arguments, needs no network, and is deterministic: two runs write the same
bytes. Pass `--stdout` to print the text without writing anything.

## The joke

> My agent reviewed its own pull request, approved it, and requested changes from me.

The gate wants UTF-8 text of 1 to 280 Unicode code points that is not only
white space. This text is 83 code points.

## License

MIT. See [LICENSE](LICENSE).
