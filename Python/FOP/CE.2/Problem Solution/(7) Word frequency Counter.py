text = input("enter text: ")
words = text.lower().split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1 #so their (word, 0) + 1 is how much will be printed for example if we write 2 in 1 place the number of words will become 2 and if we change 0  into 1 the numbers will raise 1 and so on
    
for word, count in freq.items():
    print(f"{word}: {count}")
 
