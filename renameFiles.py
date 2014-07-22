#
#	first draft of script to process data as it comes from the OSMtracker app
#	-reads the xml formatted .gpx file with gps data and associated audio files
#	-renames associated audio files, adding the values for lat & lon to file name
#	-Must rename .gpx to 'test.xml', or change this script to open with other name
#	-call from command line: 
#			> cd into_dir_with_files 
#			> python renameFiles.py 
#
#	ToDo: 	-modify so that foldername passed through command line
#			-find the .gpx file, and open that
#

from bs4 import BeautifulSoup
import os


data = open('test.xml', 'r').read()
soup = BeautifulSoup(data)

for w in soup.findAll('wpt'):
	print(w.find('link'))
	if w.find('link') != None:
		filename = w.find('link').get('href')
		
		lat = w.get('lat')
		lon = w.get('lon')
		print(filename)
		print(lat)
		print(lon)
		newname = filename[:-5] + "_" + lat + "_" + lon + ".3gpp"
		print(newname)
		filepath_split = os.path.split(filename)
		print(filepath_split)
		root = filepath_split[0]


		filename_split = os.path.splitext(filename) # filename and extensionname (extension in [1])
        print(filename_split)

        filename_zero = filename_split[0]
        print(filename_zero)

        directory = "data"

        for f in os.listdir(directory):
        	
        	if f == filename:
	        	print "found file---------------------"
	        	print f
	        	path = os.path.join(directory, f)
	        	target = os.path.join(directory, newname)
	        	os.rename(path, target)
	        	
	        	
	print("-------------------")

