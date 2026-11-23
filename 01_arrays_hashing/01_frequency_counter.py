def count_frequency(items):
    freq = {}
    for item in items:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq
print(count_frequency(["ai", "ml", "ai", "rag", "ml", "ai"]))    