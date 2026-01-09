import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 1. მონაცემების შეყვანა (X არის ვერტიკალური, Y - ჰორიზონტალური)
x_vertical = np.array([0.60, 2.250, 4.90, 7.10, 9.40, -1.40, -3.70, -5.90, -8.20])
y_horizontal = np.array([0.90, 2.240, 4.20, 6.10, 8.50, -1.10, -2.80, -4.90, -7.50])

# 2. პირსონის კორელაციის კოეფიციენტის გამოთვლა
correlation, _ = pearsonr(x_vertical, y_horizontal)
print(f"Pearson Correlation Coefficient: {correlation:.5f}")

# 3. ვიზუალიზაცია მომხმარებლის მოთხოვნის შესაბამისად
plt.figure(figsize=(10, 8))
# ვატრიალებთ: ჰორიზონტალურზე ვსვამთ Y-ს, ვერტიკალურზე - X-ს
plt.scatter(y_horizontal, x_vertical, color='teal', alpha=0.6, edgecolors='black', s=80, label='Data Points')

plt.title(f"Correlation Analysis (r = {correlation:.5f})", fontsize=14)
plt.ylabel("X ღერძი (Vertical)", fontsize=12)
plt.xlabel("Y ღერძი (Horizontal)", fontsize=12)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()

plt.savefig('correlation_plot.png')
plt.show()
