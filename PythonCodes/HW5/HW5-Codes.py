import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

s = ctrl.TransferFunction([1, 0], [1])

G1 = ctrl.pade(2, 1)  # Pade approximation for delay
G1 = ctrl.TransferFunction(G1[0], G1[1])
G2 = 5 / (5 * s + 1)
G3 = (s + 1) / s

G = G1 * G2 * G3

plt.figure()
ctrl.bode(G, dB=True)
plt.title('Bode Plot of the System')
plt.grid()

GM, PM, _, _ = ctrl.margin(G)
print(f'Gain Margin: {20 * np.log10(GM):.2f} dB')
print(f'Phase Margin: {PM:.2f} degrees')

if GM > 0 and PM > 0:
    print('The system is stable.')
else:
    print('The system is unstable.')

plt.show()
