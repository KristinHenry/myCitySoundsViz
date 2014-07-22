myCitySoundsViz
===============


CommandLine--->to convert 3gpp files (from Android) to wav files:

#!/bin/bash
for file in *.3gpp
do
  ffmpeg -y -i $file -f wav "$file.wav"
  touch "$file.wav" -r $file
done


full instructions here: 
https://code.google.com/p/osmtracker-android/wiki/Reading3GPPFiles

ToDo: wrap this in a python script, to streamline data-conversion process

