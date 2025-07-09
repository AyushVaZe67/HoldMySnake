text = 'Ayush'
print(text[::-1])


text = "Reverse me"
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text  # Prepend each character
print(reversed_text)  # Output: "em esreveR"