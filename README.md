# jkislew/makefun-news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/jkislew/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/jkislew/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

A deterministic program that writes one front-page image summing up the
world news of Sunday 22 November 2026.

The image is a newspaper front page, "THE WORLD TODAY", dated
Sunday 22 November 2026. Its lead story is COP31 in Antalya running
into overtime with fossil-fuel talks deadlocked. Six further stories
sit below it: an Iranian attack hitting a Bahrain industrial site,
Mexico capturing cartel boss El Chapo Isidro, Russian strikes on
Kryvyi Rih and a ship ablaze in the Gulf of Finland, the FBI probing
an apparent hack of its crime database, a magnitude 6.7 earthquake
in Peru's Andes, and thousands marching in Lisbon over living costs.

`main.py` copies the bundled `entry.png` to `/output/entry.png`
(or to `$ENTRY_OUTPUT` when set). It needs no network and writes
the same bytes on every run. `make_image.py` is the generator that
drew `entry.png` with Pillow: fixed story data, fixed fonts, no
randomness. Re-running it reproduces `entry.png` byte for byte.
Stories were cross-checked against Reuters, AP, BBC and Al Jazeera
reports published on 22 November 2026. License: MIT.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=tpc75c2v&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
