myCitySoundsViz
===============

#Data Collection Method

1. use OSMtracker app  
2. transfer files to laptop with usb cable
3. run renameFiles.py on folder 
  -goes through the xml file for "track", finds audio files corresponding to gps positions, appends gps info to filename of corresponding audio file
4. run commandline call to ffmpeg to convert renamed .3gpp files to .wav formats


####CommandLine--->to convert 3gpp files (from Android) to wav files:

```
#!/bin/bash
for file in *.3gpp
do
  ffmpeg -y -i $file -f wav "$file.wav"
  touch "$file.wav" -r $file
done
```


full instructions here: 
https://code.google.com/p/osmtracker-android/wiki/Reading3GPPFiles

ToDo: wrap this in a python script, to streamline data-conversion process

