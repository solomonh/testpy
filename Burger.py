import numpy as np
import matplotlib.pyplot as plt

def initialBell(x):
    return np.where(x%1. <0.5, np.power(np.sin(2*x*np.pi),2),0)

nx=40
c=0.2
x=np.linspace(0.0,1.0, nx+1)
phi=initialBell(x)
phiNew=phi.copy()
dt=0.001
dx=1./nx
nt=40
for n in xrange(1,nt):

    for j in xrange (1,nx):
        phiNew[j]=phi[j]*(1+0.5*(dt/dx)*(phi[j+1]-phi[j-1]))
    phiNew[0]=phi[0]*(1+0.5*(dt/dx)*(phi[1]-phi[nx-1]))
    phiNew[nx]=phiNew[0]

    phi=phiNew.copy()

t=nt*dt
plt.plot(x, phi, 'b', label='CTCS')
plt.legend(loc='best')
plt.xlabel('x')
plt.ylabel('$\phi$')
plt.axhline(0, linestyle=':', color='black')
plt.show()

