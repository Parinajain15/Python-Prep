def find_duplicates(nums):
    freq = {}
    for num in nums:          # Step 1: Fill freq with counts from nums
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    duplicates = []
    for num in freq:          # Step 2: Check which keys have count > 1
        if freq[num] > 1:
            duplicates.append(num)
    return duplicates

print(find_duplicates([4, 2, 7, 4, 8, 2, 1]))