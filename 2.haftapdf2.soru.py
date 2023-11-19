def ikiyebolme(x):
    return x**3+4*x**2-10
x1=1
x2=2
x0=float
y0=float
a=ikiyebolme(x1)
b=ikiyebolme(x2)
for i in range(4):
    if a*b < 0:
        x0=(x1+x2)/2
        y0=ikiyebolme(x0)
        if y0*a<0:
            x2=x0
        elif y0*b<0:
            x1=x0
    print("{}.İterasyon degeri".format(i + 1))
    print("x'in degeri : {}".format(x0))
    print("f(x)'in degeri : {:.15f}".format(y0))
    print()
