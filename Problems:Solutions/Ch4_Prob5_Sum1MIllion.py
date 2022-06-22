minval = 1
maxval = 1000001
values = [val for val in range(minval, maxval)]

for val in range(minval, maxval):
	values.append(val)

print(f"Values from", minval, "to", maxval-1)
print("Min Value is:", min(values))
print("Max Value is:", max(values))
print("Sum of all is:", sum(values))

# print(min(values), max(values), sum(values))