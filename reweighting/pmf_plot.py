import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# File paths
file_paths = [
    'run1/pmf-c2-output.dat-reweight-disc0.5.dat.xvg',
    'run2/pmf-c2-output.dat-reweight-disc0.5.dat.xvg',
    'run3/pmf-c2-output.dat-reweight-disc0.5.dat.xvg'
]

# Read data from each file
data_all = []  # To store PMF data from each file

for file_path in file_paths:
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            # Skip lines starting with @ or # (comments/metadata)
            if not line.startswith(('@', '#')):
                parts = line.split()
                if len(parts) >= 2:  # Ensure there are at least two columns
                    data.append((float(parts[0]), float(parts[1])))
    data_all.append(data)

# Check if all files have the same RC values
if any(len(data) != len(data_all[0]) for data in data_all):
    raise ValueError("Files have different RC values or lengths; check data consistency.")

# Convert to numpy arrays for easier calculations
rc_values = np.array([point[0] for point in data_all[0]])  # RC values (assumed same for all files)
pmf_values = np.array([[point[1] for point in data] for data in data_all])  # PMF values from each file

# Calculate the mean and standard deviation along the files' axis
pmf_mean = np.mean(pmf_values, axis=0)
pmf_std = np.std(pmf_values, axis=0)

# Plot the average PMF with error bars
plt.figure(figsize=(10, 6))
plt.plot(rc_values, pmf_mean, marker='o', linestyle='-', color='b', label='Average PMF')
plt.fill_between(rc_values, pmf_mean - pmf_std, pmf_mean + pmf_std, color='b', alpha=0.2, label='Std Dev')

# Add labels, title, and limits
plt.xlabel('Host-Guest distance (Å)', fontsize=20)
plt.ylabel('PMF (kcal/mol)', fontsize=20)
plt.xlim(0, 30)
plt.ylim(0, 8)
plt.title('Average Potential of Mean Force (PMF)', fontsize=20)
plt.legend()
plt.grid(True)

# Save the plot
plt.savefig('1D_pmf_average_std_0.5.png')
print("Plot saved as '1D_pmf_average_std_0.5.png'")

