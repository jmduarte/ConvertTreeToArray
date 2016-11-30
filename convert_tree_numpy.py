import ROOT

#rfile = ROOT.TFile("/afs/cern.ch/work/m/mstoye/DeepBs/CMSSW_8_0_12/src/RecoBTag/TagVarExtractor/test/JetTaggingVariables.root")
#tree = rfile.Get("ttree")

def convertToTree (name, train) :
    rfile = ROOT.TFile(name+".root")
    print 'Converting', name+".root", " to ",name+".npy"
    tree = rfile.Get("ttree")
#tree.Show(5)
    from root_numpy import tree2array
    import numpy
    import numpy.lib.recfunctions
    Tuple = tree2array(tree)
    BranchList = Tuple.dtype.names
    
#import random
#print ' first ' , Tuple
    if train:
        numpy.random.shuffle(Tuple)
        numpy.random.shuffle(Tuple)
        numpy.random.shuffle(Tuple)
        print ' reshuffeled ', Tuple

    Jet_flavour =Tuple['Jet_flavour']
    Jet_nbHadrons =Tuple['Jet_nbHadrons']
    Jet_cbHadrons =Tuple['Jet_ncHadrons']

    # adds getting the truth from flavor
    Y = Jet_nbHadrons  == 1
   # NoY =  Jet_nbHadrons !=1
   # noY = 1.*NoY# converts bool to float
    yesy =1.*Y # converts bool to float
    Cs = abs(Jet_flavour)==4
    Cs_float = 1.*Cs
    Csplit = 1*(Jet_cbHadrons>1)
    Csingle = 1*(Jet_cbHadrons==1)
    Csingle = numpy.multiply(Cs_float,Csingle)
    Csplit= numpy.multiply(Cs_float,Csplit)
    U =  abs(Jet_flavour) == 1
    D =  abs(Jet_flavour) == 2
    S =  abs(Jet_flavour) == 3
    G =  abs(Jet_flavour) == 21
    Light = [U,D,S,G]
    Light_sum = numpy.sum(Light,axis = 0)
    Light_sum_float = Light_sum*1
    
    splitb = 1*(Jet_nbHadrons  > 1)
#yesy.reshape(1,len(yesy))
    y = numpy.column_stack((yesy, Csingle,Light_sum_float,splitb,Csplit))
    y = y.astype('float32')
    #print 'y shape ' , y.shape, ' other shapes ',  noY.shape , ' ' , yesy.shape
    #print y
#x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_genpt','Jet_phi','Jet_mass','Jet_flavour','Jet_nbHadrons','Jet_JP','Jet_JBP','Jet_CSV','Jet_CSVIVF'])
    x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_flavour','Jet_nbHadrons','Jet_ncHadrons','Jet_CSV'])

    if(train):
        numpy.save(name+"_X.npy", x)
        numpy.save(name+"_Y.npy", y)
    else:
        numpy.save(name+"_test_X.npy", x)
        numpy.save(name+"_test_Y.npy", y)


#convertToTree("allMi",train=True)
#convertToTree("QCDflat",train=True)
