def normalize(text):
    text = text.lower()
    punctuation = set(",.;:?!/\"'()")
    return "".join(" " if ch in punctuation else ch for ch in text)

def tokenize(text):
    return [word for word in text.split() if word]

def count_words(words):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

def top_k(counts, k):
    items = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return items[:k]

line = input("Enter text: ")
words = tokenize(normalize(line))
top3 = top_k(count_words(words), 3)

print(" ".join(f"{w}={c}" for w, c in top3))
