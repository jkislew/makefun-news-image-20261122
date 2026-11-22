# The World Today — 22 November 2026

[![make.fun entry](https://img.shields.io/badge/make.fun-news--image--20261122-red)](https://make.fun/bounty/news-image-20261122)
[![Author](https://img.shields.io/badge/author-@jimkis-blue)](https://make.fun/@jimkis)
[![Referral](https://img.shields.io/badge/referral-tpc75c2v-green)](https://make.fun/r/tpc75c2v)

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

## Run

```sh
python3 main.py
```

`main.py` copies the bundled `entry.png` to `/output/entry.png`
(or to `$ENTRY_OUTPUT` when set). It needs no network and writes
the same bytes on every run.

`make_image.py` is the generator that drew `entry.png` with Pillow:
fixed story data, fixed fonts, no randomness. Re-running it
reproduces `entry.png` byte for byte.

## Competition

Entry for make.fun **news-image-20261122** — "Sum up 22 November's
world news in one image". Stories were cross-checked against
Reuters, AP, BBC and Al Jazeera reports published on 22 November
2026.

License: MIT.
