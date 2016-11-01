import ROOT
from root_numpy import array2root
import numpy
import numpy.lib.recfunctions
myarray = numpy.load("/afs/cern.ch/work/m/mstoye/DeepGPU/test_result.npy")
print myarray
#AllSruct = myarray.view(numpy.recarray)
#print AllSruct
#mynames = AllSruct.dtype.names
#AllSruct.dtype.names = 'nama'
#print AllSruct.dtype

array2root(myarray,"prob_QCD_Debug.root",mode="recreate")
