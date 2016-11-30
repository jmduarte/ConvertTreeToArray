import numpy
def preprocess_features(filenameX,Means,STD,toJson):
  
  print('preprocess features from: ' , filenameX)
 
# below reduces to 2 D
#  print(y)
#  print(y.shape)
#  print('shapes')
#  Y_true = numpy.vstack((y[:,0],y[:,3])).transpose() 
#  Y_false = numpy.vstack((y[:,1],y[:,2]))
#  Y_false = numpy.vstack((Y_false,y[:,4])).transpose() 
#  Y_false = numpy.sum( Y_false, axis=1)
#  Y_true = numpy.sum( Y_true, axis=1)
#  y = numpy.vstack( (Y_true, Y_false )).transpose() 
#  print('Read y ', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000)

  X = numpy.load(filenameX)
  mynames = X.dtype.names
  print ('number of branches (root jargon) ', len(mynames) )
  for index , name in enumerate(mynames):
         print (' branch index ', index, ' branch name ',name)
  CheckMVA = X['Jet_cMVAv2']
  x = X.view(numpy.float32).reshape(X.shape + (-1,))
  x = x.astype('float32')
  deleteList = [4,5,60,61,64,65,68,69,72,73,76,77,80,81,84,85,86,87,88,89]
  x = numpy.delete(x,deleteList , 1)
  nameList = []
  for index , name in enumerate(mynames):
    if (index in deleteList):
         print (' branch index ', index, ' branch name ',name)
    else:
      nameList.append(name)

  text_file = open("Parameters.json", "w")
  text_file.write("{\n")
  text_file.write("\"inputs\": [\n")
  

  CutTHresMeanAll=  numpy.load(Means)
  CutTHresStdvAll= numpy.load(STD)
  
  for i in range (x.shape[1]):
    text_file.write("{\"name\": \""+nameList[i]+"\",\n")
    print (i, ' selected index ',nameList[i])
    # fix of bug of unknown source, accurs rarely
    x[:,i][ numpy.isnan(  x[:,i])  ] = 1.
    # The soft lepton taggers are -inf, if not present, -0.2 is below the actual range (> 0) where you expect results 
    x[:,i][ numpy.isinf(  x[:,i])  ] = -0.2

#   old bug fix
#    if (i==53 or i==54 or i==55):
#      print   (x[:,i])
#      x[:,i][ x[:,i] == 0  ] = -99
#      print (x[:,i])
#          x[:,i][]
    Cur = x[:,i]

# only  relevant if you want toget means from this sample (be BEWARE, all sample must use same means)     
# values are set upstream (in CMSSW to -99 if not present). We want mean and std without using the -99s
#    CutTHres = Cur[Cur>-90]
#   
#    print (i, 'before a threshold ' , x[:,i].size, 'before a threshold ' , CutTHres.size)

    CutTHresMean=CutTHresMeanAll[i]
    CutTHresStdv=CutTHresStdvAll[i]

    text_file.write("\"scale\":%s" % CutTHresStdv+",\n")
    text_file.write("\"offset\":%s" %  CutTHresMean +",\n")
    if (i != x.shape[1]):
        text_file.write("\"default\": 0.0 },\n")
    else:
        text_file.write("\"default\": 0.0 }\n")

    x[:,i] = numpy.subtract(x[:,i],CutTHresMean)  
    # values are set upstream (in CMSSW to -99 if not present). We want them at 0, which e.g. also UCI did.
    x[:,i][ x[:,i]<-90-CutTHresMean] = 0.
    x[:,i] = numpy.divide( x[:,i],CutTHresStdv)    
    print('Feature ', i, ' after rescaling. mean: ', x[:,i].mean(axis=0) , ' , std: ' ,x[:,i].std(axis=0), x.shape)
    print('Feature ', i, ' suntracted mean: ', CutTHresMean , ' ',CutTHresStdv)
    
    
  #print( x[0][0],' ' , x[0][1], ' ', x[0][2],' ' , x[0][3], ' ',x[0][4],' ' , x[0][5], ' ', x[0][6],' ' , x[0][7] , ' and ' , CheckMVA)
  text_file.write("],\n")
  text_file.write("\"class_labels\": [\"prob_b\", \"prob_c\", \"prob_udsg\", \"prob_bb\",\"prob_cc\"],\n")
  # Warning, hardcoded what we use 
  text_file.write("\"keras_version\" : \"1.1.0\"\n")
  text_file.write("}\n")
  # this is only in case you want to make a json for the LWNN (leight weight neural net)
  if(toJson):
    text_file.close()
 
 
  print('Finished extraction')
  return x

x   = preprocess_features("JetTaggingVariablesDebug_X.npy","Means.npy","STD.npy", false)


