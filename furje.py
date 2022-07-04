from scipy import integrate
import math
import matplotlib.pyplot as plt

l1 = math.pi
l2 = l1*-1
firstarr = []
secondarr = []
originf = []
funkcja = input("Type function:")

for xd in range(-200,200):
    firstarr.append(xd)
    def a0(x):
        return eval(funkcja)
    v, err = integrate.quad(a0 , l1 , l2)
    ac = v / l1
    summm = 0

    for w in range(1,30):
        def aw(x,wd):
            return eval(funkcja) * (math.cos((math.pi * wd * x) / l1))
        h , err = integrate.quad(aw , l1 , l2 , args = w)
        a = h / l1

        def bw(x,wd):
            return eval(funkcja) * (math.sin((math.pi * wd * x) / l1))
        g , err = integrate.quad(bw , l1 , l2 , args = w)
        b = g / l1

        summm += a * math.cos((math.pi * w * xd) / l1)+b * math.sin((math.pi * w * xd) / l1)
    summa = ac / 2 + summm
    x = xd
    originf.append(eval(funkcja))
    secondarr.append(-summa)

plt.plot(firstarr, originf,label='f(x)' )
plt.plot(firstarr, secondarr,label='Furje(f(x))')
plt.axis([-100, 100, -100, 100])
plt.show()
