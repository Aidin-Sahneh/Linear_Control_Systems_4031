import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

s = ctrl.TransferFunction([1, 0], [1])

G = (5 * s + 10) / (s**2 + 4 * s + 5)

zeros_G = ctrl.zero(G)
print("Zeros of the system:")
print(zeros_G)

poles_G = ctrl.pole(G)
print("Poles of the system:")
print(poles_G)

plt.figure()
time, response = ctrl.step_response(G)
plt.plot(time, response, label="Step Response of G")
plt.title("Step Response of G")
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.grid()
plt.legend()

K_p = ctrl.dcgain(G)
ss_error_step = 1 / (1 + K_p)
print("Ess:")
print(ss_error_step)

plt.show()
