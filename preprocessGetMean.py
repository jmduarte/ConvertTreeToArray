import numpy
def extract_features_labels(filenameX):

#  y = numpy.delete(y, [3,4],1)
#  print('Read y ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
  X = numpy.load(filenameX)
  mynames = X.dtype.names
  print ('number of branches (root jargon) ', len(mynames) )
  for index , name in enumerate(mynames):
         print (' branch index ', index, ' branch name ',name)
  CheckMVA = X['Jet_cMVAv2']
  x = X.view(numpy.float32).reshape(X.shape + (-1,))
  x = x.astype('float32')
  # drop branches you do not want to be trained on
#  x = numpy.delete(x, [6,7], 1)

  print 'delete now'
  print( x[0][0],' ' , x[0][1], ' ', x[0][2],' ' , x[0][3], ' ',x[0][4],' ' , x[0][5], ' ', x[0][6],' ' , x[0][7] , ' and ' , CheckMVA)
 
  for i in range(6):
    print(90-i)
    x = numpy.delete(x, [90-i], 1)
# CSV  x = numpy.delete(x, [2,3,4,5,6,7, 61,62,65,66,69,70,73,74,77,78,81,82], 1)
  x = numpy.delete(x, [4,5,61,62,65,66,69,70,73,74,77,78,81,82], 1)

 
  print( x[0][0],' ' , x[0][1], ' ', x[0][2],' ' , x[0][3], ' ',x[0][4],' ' , x[0][5], ' ', x[0][6],' ' , x[0][7] , ' and ' , CheckMVA)
  
  #  print('Read X ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)


  
  # subtract mean and 
  std = numpy.zeros(x.shape[1])
  mean = numpy.zeros(x.shape[1])
  for i in range (x.shape[1]):
    x[:,i][ numpy.isnan(  x[:,i])  ] = 1.
    x[:,i][ numpy.isinf(  x[:,i])  ] = -0.2
    if (i==53 or i==54 or i==55):
      print   (x[:,i])
      x[:,i][ x[:,i] == 0  ] = -99
      print (x[:,i])
#          x[:,i][]
    Cur = x[:,i]
     
  # values are set upstream (in CMSSW to -99 if not present). We want mean and std without using the -99s
    CutTHres = Cur[Cur>-90]

   
    CutTHresMean=CutTHres.mean(axis=0)
    CutTHresStdv=CutTHres.std(axis=0)
    print  i, ' ' ,  CutTHresStdv , ' ' , CutTHresStdv
    std[i] = CutTHresStdv
    mean[i] = CutTHresMean
  
  numpy.save("Means.npy", mean)
  numpy.save("STD.npy", std)

  print('Finished extraction')
  return x

x  = extract_features_labels("allMix_test2_X.npy")
#numpy.save("/afs/cern.ch/work/m/mstoye/DeepGPU/Conv_QCD50to80_X.npy", x)
#numpy.save("/afs/cern.ch/work/m/mstoye/DeepGPU/Conv_QCD50to80_Y.npy", y)
