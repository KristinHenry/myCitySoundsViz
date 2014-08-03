#
#	second draft of script to process data as it comes from the OSMtracker app
#	-finds .gpx in folder with .gpp files	
#	-reads the xml formatted .gpx file with gps data and associated audio files
#	-renames associated audio files, adding the values for lat & lon to file name
#	-renamed files moved to new folder
#	
#	-call from command line: 
#			> cd into_dir_with_folders
#			> python renameFiles.py 
#
#			
#

from bs4 import BeautifulSoup
import os

rootdir = 'data'

for subdir, dirs, files in os.walk(rootdir):
    for subdir in dirs:
    	print "-------------------"
        print "subdir" + subdir

        srcdir = os.path.join(rootdir, subdir)

        targdir = os.path.join(rootdir,subdir + '_new')
        if not os.path.isdir(targdir):
        	os.makedirs(targdir)


        for file in os.listdir(srcdir):
        	
        	if file[-3:] == "gpx":

        		path = os.path.join(srcdir, file)
        		data = open(path, 'r').read()
        		soup = BeautifulSoup(data)

        		for w in soup.findAll('wpt'):

        			if w.find('link') != None:
        				filename = w.find('link').get('href')
        				lat = w.get('lat')
        				lon = w.get('lon')
        				newname = filename[:-5] + "_" + lat + "_" + lon + ".3gpp"

        				for f in os.listdir(srcdir):
        					if f == filename:
        						print "found file ------------"
        						src = os.path.join(srcdir, f)
        						targ = os.path.join(targdir, newname)
        						os.rename(src, targ)
        						print f, filename




