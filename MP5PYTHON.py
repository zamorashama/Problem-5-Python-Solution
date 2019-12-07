import numpy as np
import matplotlib.pylab as plt
n=np.linspace(0,199,200)    
         
def x(n): 
    e=eval(x1)  
    return e 
x1=(input("Input your Equation x(n):"))   
 
for i in range(0,200):
    if i==0:
        y=(-1.5*x(n))+(2*x(n+1))-(0.5*x(n+2))
    elif i==199:
        y=(1.5*x(n))-(2*x(n-1))+(0.5*x(n-2))
    else:
        y= (0.5*x(n+1))-(0.5*x(n-1))

plt.plot(x(n),color="k")
plt.plot(y,color="b")
plt.show