import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['DELE (Secure)', 'Graphic A', 'Graphic B']
l2_means = [68, 42, 82]
heritage_means = [88, 75, 94]
iep_means = [55, 38, 78]

x = np.arange(len(labels))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, l2_means, width, label='L2 Learners', color='#4e79a7')
rects2 = ax.bar(x, heritage_means, width, label='Heritage', color='#f28e2b')
rects3 = ax.bar(x + width, iep_means, width, label='IEP Progress', color='#e15759')

# Labels and Title
ax.set_ylabel('Accuracy (%)')
ax.set_title('Class Performance Summary (N=22)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.set_ylim(0, 100)

plt.show()