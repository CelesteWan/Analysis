import numpy as np

data = np.loadtxt('output.dat')
binding = data[np.isfinite(data)]
arr = np.array(binding)

binding_event_values = []
binding_event_indices = []
#residence_time = []
unbinding_event_values = []
unbinding_event_indices = []
binding_number=0
unbinding_number=0

in_binding_event = True

# Loop through array to identify distinct binding events
for idx, value in enumerate(arr):
    if value <= 2 and in_binding_event:
        # Start of a new binding event
        binding_event_values.append(value)
        binding_event_indices.append(idx)
        binding_number=binding_number+1
        in_binding_event = False
        #if value <6 :
        # Start of a new binding event
        #in_binding_event = True
            #residence_time.append(value)
    elif value >= 12 and not in_binding_event:
        # End of a binding event when value goes above 8
        in_binding_event = True
        unbinding_number=unbinding_number+1
        unbinding_event_values.append(value)
        unbinding_event_indices.append(idx)
            
# Convert lists to arrays
binding_event_values = np.array(binding_event_values)
binding_event_indices = np.array(binding_event_indices)
#residence_time = np.array(residence_time)
unbinding_event_values = np.array(unbinding_event_values)
unbinding_event_indices = np.array(unbinding_event_indices)

# Save the extracted data to new files
np.savetxt('binding_event_values.dat', binding_event_values, fmt='%f', header='Values at binding events')
np.savetxt('binding_event_indices.dat', binding_event_indices, fmt='%d', header='Indices of binding events')
#np.savetxt('residence_time.dat', binding_event_indices, fmt='%d', header='Indices of binding events')
np.savetxt('unbinding_event_values.dat', unbinding_event_values, fmt='%f', header='Values at unbinding events')
np.savetxt('unbinding_event_indices.dat', unbinding_event_indices, fmt='%d', header='Indices of unbinding events')

print(binding_number)
print(unbinding_number)
print("Binding event extraction and saving completed.")

