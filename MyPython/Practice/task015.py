l1 = [15,25,48,36,85,62,45]

largest = l1[0]
for i in l1:
    if i > largest:
        largest = i

print(largest)

numbers = [15, 25, 48, 36, 85, 62, 45]
numbers.sort()  # Sorts in ascending order
largest = numbers[-1]  # Last element is largest
print("Largest number:", largest)  # Output: 85