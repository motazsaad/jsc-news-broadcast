#!/usr/bin/env bash

cd headlines_10pm_17_07_2017
for f in *; do printf "%s\n" " ($f)"; done > ../headlines_10pm_17_07_2017.transcription

cd ..
cd headlines_10pm_28_07_2017
for f in *; do printf "%s\n" " ($f)"; done > ../headlines_10pm_28_07_2017.transcription

cd ..
cd headlines_10pm_29_07_2017
for f in *; do printf "%s\n" " ($f)"; done > ../headlines_10pm_29_07_2017.transcription



################################
cd ..
cd headlines_10am_2_11_2015
for f in *.wav ; do printf " (%s)\n" "${f}"; done > ../../headlines_10am_2_11_2015.transcription

cd ..
cd headlines_10pm_14_08_2017
for f in *.wav ; do printf " (%s)\n" "${f}"; done > ../../headlines_10pm_14_08_2017.transcription


cd ..
cd headlines_10pm_15_08_2017
for f in *.wav ; do printf " (%s)\n" "${f}"; done > ../../headlines_10pm_15_08_2017.transcription

cd ..
cd headlines_10pm_19_4_2016
for f in *.wav ; do printf " (%s)\n" "${f}"; done > ../../headlines_10pm_19_4_2016.transcription

