def find_most_freq(num):
    freq_dic = {}
    for n in num:
        if n in freq_dic:
            freq_dic[n] +=  1
        else:
            freq_dic[n] = 1
    max_counter = 0
    most_freq = None
    for key, value in freq_dic.items():
        if value > max_counter:
            max_counter = value
            most_freq = key
    print(f"{most_freq} and {max_counter}")
find_most_freq([1, 3, 2, 3, 1, 3])