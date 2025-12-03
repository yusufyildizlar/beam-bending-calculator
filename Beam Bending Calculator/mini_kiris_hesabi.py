import matplotlib.pyplot as plt
import numpy as np


loads = np.array([500, 1000, 1500, 2000, 3000, 4000])
L = 2
E = 2e11
I = 5e-6
deflections = loads * L**3 / (3 * E * I)

plt.plot(loads, deflections, marker='o')
plt.xlabel("Force (N)")
plt.ylabel("Deflection (m)")
plt.title("Kiriş Eğilmesi")
plt.grid(True)


plt.savefig("results.png")
plt.show()