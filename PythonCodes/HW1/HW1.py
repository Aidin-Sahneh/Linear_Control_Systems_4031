import numpy as np
import control as ctrl

s = ctrl.TransferFunction([1, 0], [1])

G1 = 1 / s
G2 = 2 * s + 1
G3 = 1 / (s**2 + 1)
G4 = s / (s + 1)

H1 = 3 / s
H2 = (s - 1) / (s + 3)
H3 = s / (s**2 + 3*s + 1)
H4 = 1 / (s + 2)

G1_input = G1 - H1 - H3
G2_input = G2 * G1_input
G3_input = G2_input - H2 + G4
G3_output = G3 * G3_input

soal4 = ctrl.minreal(G3_output - H4, verbose=False)

print("Simplified Transfer Function:")
print(soal4)

poles = ctrl.pole(soal4)
print("\nPoles of the system:")
print(poles)
