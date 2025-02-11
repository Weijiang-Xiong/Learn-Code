import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
sns.set_style('darkgrid')
# -----------------------------------------
# 1. Simulated Data and GMM PDF Computation
# -----------------------------------------
T = 50   # number of time steps
K = 5    # number of Gaussian components
time = np.arange(T)  # time steps

# Define a range of y-values (predicted variable values) for PDF evaluation
y_vals = np.linspace(-5, 15, 300)

# Simulated GMM parameters (replace with your model outputs)
np.random.seed(42)
means = np.random.rand(T, K) * 10           # shape (T, K)
variances = np.random.rand(T, K) * 2          # shape (T, K)
weights = np.random.rand(T, K)
weights = weights / weights.sum(axis=1, keepdims=True)  # normalize weights per time step

# Compute the GMM PDF at each time step over y_vals
pdf_matrix = np.zeros((T, len(y_vals)))
for t in range(T):
    for k in range(K):
        pdf_matrix[t, :] += weights[t, k] * norm.pdf(y_vals, 
                                                      loc=means[t, k],
                                                      scale=np.sqrt(variances[t, k]))

# Compute a single predicted value per time step (e.g., weighted average of component means)
predicted_mean = np.sum(weights * means, axis=1)

# Simulated ground truth (replace with your actual values)
ground_truth = np.sin(time / 5) * 3 + 5 + np.random.randn(T) * 0.5

# -----------------------------------------
# 2. Create the Rotated Ridge Plot
# -----------------------------------------
plt.figure(figsize=(12, 8))

# Set a scaling factor so the density ridge is visible horizontally.
# Adjust this value based on the range of your density values.
scale = 10
palette = sns.color_palette("husl", T)
# For each time step t, we will plot the density ridge as a horizontal fill.
# Here, the baseline is at x = t. Then we add a horizontal offset equal to:
#    (scale * pdf_matrix[t, :])
# so that for each y (vertical axis) the fill goes from x = t to x = t + scale*pdf.
for t in range(T):
    x_baseline = t  # the left side (time coordinate) for this ridge
    ridge_x = t + scale * pdf_matrix[t, :]  # the right edge, shifted by the (scaled) density
    plt.fill_betweenx(y_vals, x_baseline, ridge_x, color=palette[t], alpha=0.6)

# Overlay the predicted time series and ground truth.
# These are plotted as points (or lines) with x = time and y = predicted/true value.
plt.plot(time, predicted_mean, 'o-', label='Predicted Mean')
plt.plot(time, ground_truth, 'x-', label='Ground Truth')

# Label the axes
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Rotated Ridge Plot of GMM Densities with Predicted Mean and Ground Truth")

# Adjust the x-axis limits to ensure all density ridges are fully visible.
max_pdf_extension = scale * pdf_matrix.max()
plt.xlim(-1, T + max_pdf_extension * 1.1)

plt.legend()
plt.tight_layout()
plt.show()