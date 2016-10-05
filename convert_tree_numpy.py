import ROOT
#rfile = ROOT.TFile("/afs/cern.ch/work/m/mstoye/DeepBs/CMSSW_8_0_12/src/RecoBTag/TagVarExtractor/test/JetTaggingVariables.root")
#tree = rfile.Get("tagVars/ttree")


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

#    print ' the following is input to x'
#    for index, Names in enumerate(BranchList):
#        print 'arrray',index, ' :' , Names
# jet cleaning
#Jet_flavour_c =Tuple['Jet_flavour']
#for i in range (Tuple.shape[0]):
#    if abs(Jet_flavour_c[i]) == 4:
#        Tuple = numpy.delete(Tuple,(i),axis=0)
#Tuple = Tuple[~(Tuple['Jet_flavour']==2)]

    Jet_flavour =Tuple['Jet_flavour']
    # adds getting the truth from flavor
    Y = abs(Jet_flavour)==5
    NoY =  abs(Jet_flavour)!=5
    noY = 1.*NoY# converts bool to float
    yesy =1.*Y # converts bool to float
    Cs = abs(Jet_flavour)==4
    Cs_float = 1.*Cs
    U =  abs(Jet_flavour) == 1
    D =  abs(Jet_flavour) == 2
    S =  abs(Jet_flavour) == 3
    G =  abs(Jet_flavour) == 21
    Light = [U,D,S,G]
    Light_sum = numpy.sum(Light,axis = 0)
    Light_sum_float = Light_sum*1
#yesy.reshape(1,len(yesy))
    y = numpy.column_stack((yesy,noY,Cs_float ,Light_sum_float))
    y = y.astype('float32')
    #print 'y shape ' , y.shape, ' other shapes ',  noY.shape , ' ' , yesy.shape
    #print y
#x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_genpt','Jet_phi','Jet_mass','Jet_flavour','Jet_nbHadrons','Jet_JP','Jet_JBP','Jet_CSV','Jet_CSVIVF'])
    x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_flavour','Jet_nbHadrons','Jet_cbHadrons','Jet_CSV'])
#x = numpy.lib.recfunctions.drop_fields(Tuple,['Jet_genpt','Jet_phi','Jet_mass','Jet_flavour','Jet_nbHadrons','Jet_CSV'])
#    mynames = x.dtype.names
#    print 'number of branches ', len(mynames) 
#    for index , name in enumerate(mynames):
#        print 'branch index: ' ,index, ' , branch name: ',name

    if(train):
        numpy.save(name+"_X.npy", x)
        numpy.save(name+"_Y.npy", y)
    else:
        numpy.save(name+"_X.npy", x)
        numpy.save(name+"_Y.npy", y)



convertToTree("QCD2C_train",train=True)
convertToTree("QCD2C_test",train=False)
