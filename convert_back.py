# this file converts python structured arrays back to root. Especially useful for converting the KERAS output back to root for ROC curves

import ROOT
from root_numpy import array2root
import numpy
import numpy.lib.recfunctions
import sys
if(len(sys.argv)!=3):
    print 'please give input path and output file name'

print 'converting: ' , sys.argv[1], ' to ' ,sys.argv[2]
myarray = numpy.load(sys.argv[1])

#print myarray
array2root(myarray,sys.argv[2],mode="recreate")
