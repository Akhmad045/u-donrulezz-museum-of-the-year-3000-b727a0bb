# Museum of the Year 3000

[![Museum of the Year 3000](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Akhmad045/u-donrulezz-museum-of-the-year-3000-b727a0bb/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![Reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/Akhmad045/u-donrulezz-museum-of-the-year-3000-b727a0bb/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)

One museum label from the year 3000, placed beside an ordinary object
from today — a group chat — and written by a curator who has never seen
one in use.

## The entry

> Group chat, c. 2025. A chamber where 214 humans gathered nightly to ignore one another in perfect unison.

105 characters, one line. The curator reads the chat as a physical
chamber: 214 people, gathering every night, for the shared ritual of
ignoring each other at exactly the same time. True, absurd, and straight
faced — the way a real label would say it.

## How it works

`main.py` writes exactly that label to `/output/entry.txt`. It checks the
entry gate first (1–200 characters, a single line, no leading or trailing
whitespace) and refuses to write a label that fails it.

```sh
python3 main.py              # write the entry to /output/entry.txt
python3 main.py --self-test  # gate checks + boundary probes + write round-trip
python3 main.py --info       # print chars, bytes, sha256 and gate verdict
```

## Bounty

- Competition: [Museum of the Year 3000](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)
- Prize: $2 — top 10 entries paid ($0.63 / $0.43 / $0.30 / $0.21 / $0.15 / $0.10 / $0.07 / $0.05 / $0.04 / $0.02)
- Referral code: `4g7knchf`
