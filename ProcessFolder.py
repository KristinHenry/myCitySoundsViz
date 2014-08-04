'''
Created on Apr 30, 2012

@author: Kristin
'''
import ProcessFile

import os


print os.path.basename(".")
abspath = os.path.abspath(".")
print abspath

src = "waves"
dst = "waveforms"

print "srcpath:" + src  
                
        
subdirList=os.listdir(src)
for subdir in subdirList:
    print subdir + "  --------------------"

    srcdir = os.path.join(src,subdir)
    targdir = os.path.join(dst,subdir)
    if not os.path.isdir(targdir):
        os.makedirs(targdir)

    for fname in os.listdir(srcdir):
        #print fname

        if fname[-3:] == "wav":
            print "."
            print srcdir + " " + fname

            
            pf = ProcessFile.ProcessFile(abspath, srcdir, targdir, fname)
        

            # dateInfo = pf.getDateInfo()            
            # peakInfo = pf.getPeaks()
            
            # # add this file's data to list of results
            # fileInfo = {'sourceName': fname[:-4], 'peakInfo': peakInfo, 'sampletime':sampletime ,'samplefreq':samplefreq}
            # for key in dateInfo:
            #     fileInfo[key] = dateInfo[key]
                
            
            # self.results.append(fileInfo)
