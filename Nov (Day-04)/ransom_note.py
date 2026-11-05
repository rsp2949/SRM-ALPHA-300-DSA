def can_construct(ransom_note, magazine):
    magazine_freq = {}
    note_freq = {}
    for ch in magazine:
        magazine_freq[ch] = magazine_freq.get(ch, 0) + 1
    for ch in ransom_note:
        note_freq[ch] = note_freq.get(ch, 0) + 1
    for ch in note_freq:
        if note_freq[ch] > magazine_freq.get(ch, 0):
            return False
    return True
ransom_note = "aa"
magazine = "aab"
print(can_construct(ransom_note, magazine))
