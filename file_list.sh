#!/usr/bin/env bash

cd headlines_10pm_17_07_2017
for f in *; do printf "%s\n" " ($f)"; done > ../headlines_10pm_17_07_2017.transcription

cd ..
cd headlines_10pm_28_07_2017
for f in *; do printf "%s\n" " ($f)"; done > ../headlines_10pm_28_07_2017.transcription

cd ..
cd headlines_10pm_29_07_2017
for f in *; do printf "%s\n" " ($f)"; done > ../headlines_10pm_29_07_2017.transcription
