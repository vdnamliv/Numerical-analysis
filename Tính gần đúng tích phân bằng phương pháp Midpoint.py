# Tính tích phân gần đúng bằng PP Midpont 
# B9
import math
def f(x):
    # a) x^4
    # return x**4

    # b) 2/(x-4)
    # return 2/(x-4)

    # c) x^2 ln x
    # return x**2 * math.log(x)

    # d) x^2 * e^-x
    # return x**2 * math.exp(-x)

    # e) 2x/(x^2-4)
    # return 2*x/(x**2-4)

    # f) 2/(x^2-4)
    # return 2/(x**2-4)

    # g) xsinx
    # return x*math.sin(x)

    # h) e^3x*sin(2x)
    # return math.exp(3*x)*math.sin(2*x)



def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

a = float(input("Nhập cận dưới: "))
b = float(input("Nhập cận trên: "))
# số khoảng
n = 1000

print("Kết quả tích phân theo phương pháp midpoint là: %0.8f" % (midpoint(f, a, b, n)))