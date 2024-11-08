import numpy as np

file_path = 'output.dat'

with open(file_path, 'r') as file:
        data = [float(line.strip()) for line in file if line.strip().isdigit() or line.strip().replace('.', '', 1).isdigit()]

arr = np.array(data)

# Extract values greater than 12 and their indices
values_above_12 = arr[arr > 12]
indices_above_12 = np.where(arr > 12)[0]

np.savetxt('values_above_12.dat', values_above_12, fmt='%f', header='Values above 12')
np.savetxt('indices_above_12.dat', indices_above_12, fmt='%d', header='Indices of values above 12')

