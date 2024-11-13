import numpy as np

# Load data from the .dat file
data = np.loadtxt('output.dat')

# Ensure all elements are valid numbers if needed (this step might not be necessary)
data_2 = data[np.isfinite(data)]

# Convert to a NumPy array (if not already)
arr = np.array(data_2)

# Extract values greater than 30 and their indices
values_above_30 = arr[arr > 30]
indices_above_30 = np.where(arr > 30)[0]

# Save the extracted data to new files
np.savetxt('values_above_30.dat', values_above_30, fmt='%f', header='Values above 30')
np.savetxt('indices_above_30.dat', indices_above_30, fmt='%d', header='Indices of values above 30')

print("Extraction and saving completed.")
