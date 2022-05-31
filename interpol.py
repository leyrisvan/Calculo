import numpy as np
import matplotlib.pyplot as plt

X = [0,0.2,0.5,0.8,1.1,1.4,1.6,1.8,1.9,2.2,2.5,2.8,2.9,3.1,3.2,3.5,3.9,4.0]
Y = [-0.5,-0.3,0.2,0.6,0.3,0.1,0.0,-0.4,-0.9,-1.2,-0.4,-0.1,0.7,0.9,1.5,1.7,1.2,1.1]

plt.scatter(X,Y)
plt.plot(X,Y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Y(X)')
plt.tight_layout()

X_interp = [0.3,0.6,1.2,1.5,2.0,2.6,3.0,3.3,3.7]
Y_interp = np.interp(X_interp, X, Y)

plt.scatter(X,Y,label='Valores Reais')
plt.plot(X,Y)
plt.scatter(X_interp,Y_interp,color='red',label='Valores Interpolados')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Y(X)')
plt.legend()
plt.tight_layout()
