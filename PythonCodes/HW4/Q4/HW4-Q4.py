import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

soorat = np.convolve([1, 1], np.convolve([1, 2], np.convolve([1, 3], [1, 4])))
makhraj = np.convolve([1, 0, 0, 0], [1, 100])

h = ctrl.TransferFunction(-1 * soorat, makhraj)

print(ctrl.zero(h))
print(ctrl.pole(h))
print(ctrl.zpk(h))

plt.figure()
ctrl.nyquist(h)
plt.grid()
plt.title('Nyquist plot of the transfer function')
plt.show()
