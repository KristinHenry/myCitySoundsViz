'''
Created on Aug 3, 2014

@author: Kristin  (@KristinHenry)
'''
import os

src = "waves"              
        
subdirList=os.listdir(src)
for subdir in subdirList:

    srcdir = os.path.join(src,subdir)

    for fname in os.listdir(srcdir):

        if fname[-3:] == "wav":
            targ = fname[:-8] + "wav"

            srcpath = os.path.join(srcdir, fname)
            targpath = os.path.join(srcdir, targ)

            os.rename(srcpath, targpath)

            