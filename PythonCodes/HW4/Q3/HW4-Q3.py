import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

s = ctrl.TransferFunction([1, 0], [1])
g = ctrl.TransferFunction([5, 5], [5, 1, 0])

delay_time = 2
G = ctrl.pade(delay_time, 4)  # Pade approximation for delay
G = ctrl.TransferFunction(G[0], G[1])

final_g = g * G

plt.figure()
ctrl.bode(g, dB=True)
plt.title('Bode plot without exp')
plt.grid()

plt.figure()
ctrl.bode(final_g, dB=True)
plt.title('Bode plot with exp')
plt.grid()

plt.show()
