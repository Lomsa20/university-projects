def merge_sort_length(words):
    if len(words) <= 1:
        return words

    mid = len(words) // 2
    left = merge_sort_length(words[:mid])
    right = merge_sort_length(words[mid:])

    return merge_by_length(left, right)

def merge_by_length(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
        elif len(left[i]) > len(right[j]):
            result.append(right[j])
            j += 1
        else:
            # tie-breaker: alphabetical
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

words = input("Enter words: ").split()
print(merge_sort_length(words))
