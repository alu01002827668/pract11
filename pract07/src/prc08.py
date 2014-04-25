#! src/bin/python
PI = 3.14155926535897931159979634685441852
import sys
def aproximacion(n):
  if (n!=0):
    suma = 0
    for i in range(1,n+1):
      xi = (i - (1/2)) / float(n)
      f_xi = 4 / (1 + xi**2)
      b = i / float(n)
      a = b - (1 / float(n))
      suma = suma + f_xi
    pi = suma/n
    return pi