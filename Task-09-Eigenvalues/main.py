
import numpy as np

# Network connection matrix
A = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Find the dominant eigenvector
index = np.argmax(eigenvalues)
centrality = np.abs(eigenvectors[:, index])

# Normalize centrality scores
centrality = centrality / np.sum(centrality)

print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvector centrality:")
for i, score in enumerate(centrality, start=1):
    print(f"Computer {i}: {score:.4f}")
