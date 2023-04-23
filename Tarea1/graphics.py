import matplotlib.pyplot as plt


s_4 = [71.517, 74.299, 74.817, 76.483, 77.039]
s_8 = [84.303, 90.030, 91.285, 93.698, 94.154]
s_12 = [90.863, 93.671, 94.311, 95.946, 96.248]
s_16 = [91.481, 93.861, 94.463, 96.077, 96.385]
s_20 = [91.495, 93.877, 94.475, 96.086, 96.393]

s = [s_4, s_8, s_12, s_16, s_20]
labels = ["s = 4", "s = 8", "s = 12", "s = 16", "s = 20"]

GH = [2, 6, 8, 16, 20]

fig, ax = plt.subplots()
for i in range(0, len(s)):
    ax.plot(GH, s[i], label = labels[i])

ax.set_title("Perceptron Branch Predictor")
ax.set_xlabel("Bits de Historia Global")
ax.set_ylabel("Porcentaje de aciertos")
plt.xticks(GH, GH)
ax.grid()
ax.legend()
plt.show()