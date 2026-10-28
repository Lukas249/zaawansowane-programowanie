def count_vowels(s: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w']

    s = s.lower()

    vowel_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1

    return vowel_count
