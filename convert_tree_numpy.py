import ROOT
#rfile = ROOT.TFile("/afs/cern.ch/work/m/mstoye/DeepBs/CMSSW_8_0_12/src/RecoBTag/TagVarExtractor/test/JetTaggingVariables.root")
#tree = rfile.Get("tagVars/ttree")
rfile = ROOT.TFile("QCD_test.root")
tree = rfile.Get("ttree")
#tree.Show(5)
from root_numpy import tree2array
import numpy
import numpy.lib.recfunctions
Tuple = tree2array(tree)
BranchList = Tuple.dtype.names

#import random
#print ' first ' , Tuple
#numpy.random.shuffle(Tuple)
#numpy.random.shuffle(Tuple)
#numpy.random.shuffle(Tuple)

print ' reshuffeled ', Tuple

#print ' the following is input to x'
for index, Names in enumerate(BranchList):
    print 'arrray',index, ' :' , Names
#numpy.random.shuffle(Tuple)

# jet cleaning

#Jet_flavour_c =Tuple['Jet_flavour']
#for i in range (Tuple.shape[0]):
#    if abs(Jet_flavour_c[i]) == 4:
#        Tuple = numpy.delete(Tuple,(i),axis=0)
#Tuple = Tuple[~(Tuple['Jet_flavour']==2)]

Jet_flavour =Tuple['Jet_flavour']
    
Y = abs(Jet_flavour)==5
NoY =  abs(Jet_flavour)!=5
noY = 1.*NoY
yesy =1.*Y # converts bool to int.
#yesy.reshape(1,len(yesy))
y =  numpy.column_stack((yesy,noY))
y = y.astype('float32')
print 'y shape ' , y.shape, ' other shapes ',  noY.shape , ' ' , yesy.shape
print y
#x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_genpt','Jet_phi','Jet_mass','Jet_flavour','Jet_nbHadrons','Jet_JP','Jet_JBP','Jet_CSV','Jet_CSVIVF'])
x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_genpt','Jet_phi','Jet_mass','Jet_flavour','Jet_nbHadrons','Jet_CSV'])
#x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_genpt','Jet_phi','Jet_mass','Jet_flavour','Jet_nbHadrons','Jet_CSV'])

mynames = x.dtype.names
print 'number of branches ', len(mynames) 
for index , name in enumerate(mynames):
    print 'branch index: ' ,index, ' , branch name: ',name


# converts from structured array to simple array
#X = x.view(numpy.float32).reshape(x.shape + (-1,))
# Assuming that -99 is used if a feature is not present all features are mean subtracted and brought to standard deviation of 1 excluding the values below -90. All values smaller -90 are set to 0.


#for i in range (0):
#    print i;
#    X[:,i][ numpy.isnan(X[:,i])] = 1.
#    Cur = X[:,i]
#    CutTHres = Cur[Cur>-90]
    #print 'before a threshold ' , X[:,i].size, 'before a threshold ' , CutTHres.size
#    CutTHresMean=CutTHres.mean(axis=0)
#    CutTHresStdv=CutTHres.std(axis=0)
    #print('mean and std ', CutTHresMean, ' ' ,CutTHresStdv)
    #CutTHresMean = CutTHresMean.reshape((X.shape[0]), 1)
#    X[:,i] = numpy.subtract(X[:,i],CutTHresMean)
    #print('before X mean and std ', X[:,i].mean(axis=0) , ' ' ,X[:,i].std(axis=0))
#    X[:,i][ X[:,i]<-90] = 0.
#    X[:,i] = numpy.divide( X[:,i],CutTHresStdv)
#    print('X mean and std ', X[:,i].mean(axis=0) , ' ' ,X[:,i].std(axis=0))

#import matplotlib.pyplot as plt
#plt.hist(X[0,i])

numpy.save("MyExtractFileXQCD_test.npy", x)
numpy.save("MyExtractFileYQCD_test.npy", y)

#print array.x
#print array.i
#print tree.to_array()
#tree = 

