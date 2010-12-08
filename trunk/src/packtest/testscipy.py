from numpy import *
from scipy import interpolate

x=[1,2,3,4,5]
y=[1,4,8,16,25]
f = interpolate.interp1d(x,y)

ynew=f(x)

print ynew
