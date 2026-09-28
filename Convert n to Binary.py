num = "19"
binary_4bit_list = [format(int(digit), '08b') for digit in num]
binary_4bit = ' '. join(binary_4bit_list) 
print(binary_4bit)

