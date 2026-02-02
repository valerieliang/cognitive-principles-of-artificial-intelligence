import numpy as np
import matplotlib.pyplot as plt

A = np.linspace(0, 1, 100)

# bayes rule equations:
f1 = lambda A: (0.1 * A) / (0.1 * A + 0.75 * (1 - A))
f2 = lambda A: A
f3 = lambda A: (0.9 * A) / (0.9 * A + 0.25 * (1 - A))

# plot figs
plt.figure(figsize=(8, 6))

plt.plot(A, f1(A), label='"the sneg of..." (postnominal)')
plt.plot(A, f2(A), label='"a..." (either)')
plt.plot(A, f3(A), label='"a tufa\'s dax..." (prenominal)')

plt.xlabel('Prior: P(animate)')
plt.ylabel('Posterior: P(animate | fragment)')
plt.legend()
plt.grid(True)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()