import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define GMM parameters
K = 3  # Number of components
means = [-2, 1, 4]  # Means of the Gaussians
variances = [1, 0.5, 1.5]  # Variances (sigma^2)
weights = [0.3, 0.4, 0.3]  # Mixing coefficients (must sum to 1)

# Generate x values
x = np.linspace(-5, 8, 1000)

# Compute individual Gaussians and the combined GMM PDF
pdf_components = [weights[k] * norm.pdf(x, means[k], np.sqrt(variances[k])) for k in range(K)]
pdf_gmm = np.sum(pdf_components, axis=0)

# Plot the individual components
plt.figure(figsize=(8, 5))
for k in range(K):
    plt.plot(x, pdf_components[k], '--', label=f'Component {k+1}', alpha=0.7)

# Plot the combined GMM PDF
plt.plot(x, pdf_gmm, 'k-', linewidth=2, label='GMM')

# Labels and legend
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Gaussian Mixture Model (GMM) PDF')
plt.legend()
plt.grid(True)
plt.show()
