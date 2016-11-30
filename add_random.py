import numpy


def add_and_randomize(filenameX,filenameY):
  xo = numpy.load(filenameX[0])
  yo = numpy.load(filenameY[0])
  print (' shape ', xo.shape)
  xl = xo.shape[1]
  yl = yo.shape[1]
  print xl, ' ' , yl
  X0 =   numpy.hstack([xo,yo])
  for index , name in enumerate(filenameX):
      if index>0:
          xi =  numpy.load(filenameX[index])
          yi = numpy.load(filenameY[index])
          xi = numpy.hstack([xi,yi])
          X0 = numpy.vstack([X0,xi])
          
  numpy.random.shuffle(X0)
  numpy.random.shuffle(X0)
  numpy.random.shuffle(X0)
  return numpy.hsplit(X0, [xl,xl+yl])

filenameX = numpy.array(["mix_prepro_X.npy","allc_prepro_X.npy","allb_prepro_X.npy","allQCDu1_prepro_X.npy"])
filenameY = numpy.array(["mix_small_Y.npy","allc_small_Y.npy","allb_small_Y.npy","allQCDu1_small_Y.npy"])
x,y,z =  add_and_randomize(filenameX,filenameY)
print x.shape, ' ' , y.shape, ' ' , z.shape
numpy.save("MIX_X.npy", x)
numpy.save("MIX_Y.npy", y)

