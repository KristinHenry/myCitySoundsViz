'''
Created on Apr 15, 2012

@author: Kristin Henry

Based on article at http://macdevcenter.com/pub/a/python/2001/01/31/numerically.html
'''
import wave
import sys
import struct
import numpy as np  # apparently, this includes fft 
#import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('Agg')   # allows saving as .svg
import matplotlib.pyplot as plt

import datetime



class ProcessFile(object):

    def __init__(self, path, dir, dest, infile):
       
        file = dir + "/" + infile


        print file
        
        fp = wave.open(file, "rb")        
        (nchannels, sampwidth, framerate, nframes, comptype, compname) = fp.getparams ()
        frames = fp.readframes (nframes * nchannels)
        out = struct.unpack_from ("%dh" % nframes * nchannels, frames)
        fp.close()
        
            
        plt.clf()       # make sure we're starting with an empty figure
        
        
        # modified from http://stackoverflow.com/a/9963564
        fftx = np.fft.fft(out)                  # the frequency transformed part
        fftx = fftx[range(int(len(fftx)/2))]    # now discard extra data  that we do not need..
        
        self.peaks = np.fft.ifft(fftx)          # we want the inverse
        
        
        # trim extra data from beginning (artifacts of file format), so we only have sound data 
        self.peaks = self.peaks[3000:]
        
        
        self.fname = infile[ :-4]      # get file name, and drop the ".wav" from it
       
        # plt.title("file: " + self.fname)
        plt.plot(self.peaks, color='grey')
        plt.axis('off')
        # plt.savefig(dest + "/" + self.fname + '.png')
        plt.savefig(dest + "/" + self.fname + '.svg')

  
       
        
    # def getDateInfo(self):
    #     #
    #     # extract datetime info from file name
        
    #     day = self.fname[ :2]
    #     month = self.fname[2:4]
    #     year = self.fname[4:8]
    #     hour = self.fname[8:10]
    #     minute = self.fname[10:12]
    #     second = self.fname[12:14]
        
    #     dt = datetime.date(int(year), int(month), int(day))
    #     dayofweek = dt.weekday()

    #     days =[ 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
        
    #     dateInfo = {'day': day, 'month': month, 'year': year, 'hour': hour, 'minute': minute,'second': second,
    #                 'dayofweek': dayofweek, 'dayname': days[dayofweek]}
        
    #     return dateInfo
    
    
        
        
    # def getPeaks(self): 
    #     #
    #     # this is rough, and could use some improvement
        
    #     freqs = abs(self.peaks)
       
    #     peaks = []
    #     maxWindow = 500
    #     window = 0
    #     max = 0
        
    #     for f in freqs:
    #         if f > max:
    #             max = f
    #         else:
    #             if window < maxWindow:
    #                 window += 1
    #             else: 
    #                 peaks.append(max)   
    #                 max = f
    #                 window = 0
        
        
    #     p = np.array(peaks)
    #     peakMin = p.min()
    #     peakMax = p.max()
    #     peakAvg = np.average(p)
        
    #     peakInfo = {'max': peakMax, 'min': peakMin, 'avg': peakAvg, 'numPeaks': len(peaks)}
    #     return peakInfo 
      
      
      
      
  