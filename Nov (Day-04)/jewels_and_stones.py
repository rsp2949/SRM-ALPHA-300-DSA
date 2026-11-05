def num_jewels_in_stones(jewels, stones):
    jewel_freq = {}
    stone_freq = {}
    for ch in jewels:
        jewel_freq[ch] = 1
    for ch in stones:
        stone_freq[ch] = stone_freq.get(ch, 0) + 1
    count = 0
    for ch in jewel_freq:
        count += stone_freq.get(ch, 0)
    return count
jewels = "aA"
stones = "aAAbbbb"
print(num_jewels_in_stones(jewels, stones))
