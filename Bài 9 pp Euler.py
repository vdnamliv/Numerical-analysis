#Bài 9 pp Euler
import numpy as np
# y'(t) = 2/t * y(t) + t^2 * e^t 
def g(t, y):
    return 2/t * y + t**2 * np.exp(t)
#exact solution y(t) = t^2 * (e^t -e)
def y(t):
  return t**2 * (np.exp(t) - np.exp(1))
# y" = 2(e^t -e) + 4te^t + t^2*e^t
def dhb2y(t):
  return 2*(np.exp(t) - np.exp(1)) + 4*t*np.exp(t) + t**2 * np.exp(t)
def euler(n, a, b, w):
  h = (b - a) / n
  t = a
  for i in range(n):
    w = w + h * g(t, w)
    t = a + (i+1) * h
    print ("i =", i+1, ": t = ", t, "   w =", w, ", sai số là: ", np.abs(w - y(t)))
  return
def find_h(n, a, b, L):
  j = (b - a) / n
  t = a
  for i in range(n+1):
    w = dhb2y(t)
    temp = np.exp(L*(t-a)) - 1
    h = 2*L*0.1/(w*temp)
    if(h <= 0):
      break
    print ("i =", i+1, ": t = ", t, "   h =", h)
    t = a + (i+1) * j
  return

# câu a:
#euler(10, 1, 2, 0)
# câu b:
# ý i
#euler(100, 1, 1.04, 0)
# ý ii
#euler(100, 1, 1.55, 0)
# ý iii
#euler(100, 1, 1.97, 0)
# câu c: 
# vi phân y theo t <= 2. Suy ra L =2
#find_h(100, 1, 2, 2)