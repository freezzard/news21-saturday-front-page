# news21-saturday-front-page

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/freezzard/news21-saturday-front-page/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/freezzard/news21-saturday-front-page/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A classic newspaper front page for Saturday 21 November 2026, drawn entirely in code. Thirty-five verified stories from that one day: three illustrated hero cards (Russian missiles landing in Poland, the World Court's genocide verdict on Myanmar, Wall Street sliding into correction), ten more illustrated cards, a region and field tally, the day in numbers, a pinned world map, twenty-two numbered briefs, and a date-check footer that names what was left out as other days' news. The Python program in this repo (render.py, scenes.py, draw.py, data.py) draws the page at 2048x2048 and exports the 1024x1024 entry.png; main.ts copies those bytes to the output directory.

## Run it

```sh
python3 render.py
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=2k68scpr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
