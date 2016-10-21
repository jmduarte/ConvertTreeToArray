import numpy
def extract_features_labels(filenameX,filenameY):
  
  print('Extracting label from ', filenameY, ' and features from: ' , filenameX)
 # print('free and happy ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)
  y = numpy.load(filenameY)
  y = y.astype('float32')

# below reduces to 2 D
#  print(y)
#  print(y.shape)
#  print('shapes')
#  Y_true = numpy.vstack((y[:,0],y[:,3])).transpose() 
#  Y_false = numpy.vstack((y[:,1],y[:,2]))
#  Y_false = numpy.vstack((Y_false,y[:,4])).transpose() 
  #print( Y_false)
#  print( Y_false.shape)
#  Y_false = numpy.sum( Y_false, axis=1)
#  Y_true = numpy.sum( Y_true, axis=1)
#  y = numpy.vstack( (Y_true, Y_false )).transpose() 
#  print(y.shape)
#  print(y)


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
  
  for i in range(6):
    print(90-i)
    x = numpy.delete(x, [90-i], 1)
# CSV  x = numpy.delete(x, [2,3,4,5,6,7, 61,62,65,66,69,70,73,74,77,78,81,82], 1)
  x = numpy.delete(x, [4,5,61,62,65,66,69,70,73,74,77,78,81,82], 1)

  print(y)
  #print( x[0][0],' ' , x[0][1], ' ', x[0][2],' ' , x[0][3], ' ',x[0][4],' ' , x[0][5], ' ', x[0][6],' ' , x[0][7] , ' and ' , CheckMVA)
  
  #  print('Read X ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)


  
  # subtract mean and 
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
#    print (i, 'before a threshold ' , x[:,i].size, 'before a threshold ' , CutTHres.size)
    CutTHresMean=CutTHres.mean(axis=0)
    CutTHresStdv=CutTHres.std(axis=0)
    x[:,i] = numpy.subtract(x[:,i],CutTHresMean)
    # values are set upstream (in CMSSW to -99 if not present). We want them at 0, which e.g. also UCI did.
    x[:,i][ x[:,i]<-90-CutTHresMean] = 0.
    x[:,i] = numpy.divide( x[:,i],CutTHresStdv)    
    print('Feature ', i, ' after rescaling. mean: ', x[:,i].mean(axis=0) , ' , std: ' ,x[:,i].std(axis=0), x.shape)

  print(' x (feature) shape ', x.shape, ' y (truth) shape ', y.shape)
  # deletes useless branches (for now)
 # for i in range(6,57):
#    print(i)
#    x = numpy.delete(x, [i], 1)
 
  print('Finished extraction')
  return x,y

x , y,  = extract_features_labels("QCD_ttbar/allMix_test2_X.npy","QCD_ttbar/allMix_test2_Y.npy")
numpy.save("test_Conv_X.npy", x)
numpy.save("test_Conv_Y.npy", y)
