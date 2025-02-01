import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

s = ctrl.TransferFunction([1, 0], [1])

T1 = 10.24 / (s**2 + 4.41*s + 10.24)

plt.figure()
time, response = ctrl.step_response(T1)
plt.plot(time, response, label="Step Response of T1")
plt.title("Step Response of T1")
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.grid()
plt.legend()
plt.show()
