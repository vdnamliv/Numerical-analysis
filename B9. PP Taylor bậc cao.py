#B9. PP Taylor bậc cao
import numpy as np
#exact solution
def es(t):
  return t**2 * (np.exp(t) - np.exp(1))

# y' = 2y/t + t^2*e^t
def f(t, y):
  return 2/t *y + t**2 * np.exp(t)

def df(t, y):  # tinh dao ham cua f hay dao ham cap 2 cua y theo t
  eps = 1e-6
  return (f(t+eps, y) - f(t, y)) / eps

def Taylor(a, b, n, y, t):
  h = (b - a) / n
  t = a
  for i in range(n):
  # Formula for second order Taylor expansion
    t = a + (i+1) * h
    y_next = y[i] + h*f(t, y[i]) + (h**2/2)*df(t, y[i])
    y.extend([y_next])
    print ("i =", i+1, ": t = ", t, "   y =", y_next, ", sai số là: ", np.abs(y_next - es(t)))

y=[0]
# câu a
#Taylor(1,2,10,y,t)
#câu b
#ý i
#Taylor(1,1.04,100,y,t)
#ý ii
#Taylor(1,1.55,100,y,t)
#ý iii
Taylor(1,1.97,100,y,t)