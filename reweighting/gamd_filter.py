import numpy as np

# Load the indices to be summed
indices_to_sum = np.loadtxt('indices_above_30.dat', dtype=int)

# Read the content of gamd.log as a list of lines
with open('gamd.log', 'r') as file:
    lines = file.readlines()

# Extract and sum only the relevant numbers from the specified indices
values_to_sum = []
for i in indices_to_sum:
    # Split the line by spaces to extract individual parts
    parts = lines[i].strip().split()
    
    # Check if the first part can be converted to a float and use it
    try:
        value = float(parts[0])  # Adjust index if a different part is needed
        values_to_sum.append(value)
    except ValueError:
        print(f"Skipping line {i}: could not convert to float")

# Sum the extracted values
summed_value = sum(values_to_sum)

# Replace the first index with the summed value and clear the others
for j, index in enumerate(sorted(indices_to_sum)):
    if j == 0:
        lines[index] = f"{summed_value}\n"  # Replace the first occurrence with the sum
    else:
        lines[index] = ''  # Clear other lines

# Filter out the empty lines
filtered_lines = [line for line in lines if line.strip() != '']

# Save the modified content back to a new file or overwrite the existing one
with open('gamd_filter.log', 'w') as file:
    file.writelines(filtered_lines)

print("Lines summed and file updated successfully.")

