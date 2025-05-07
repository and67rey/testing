def count_vowels(text):
    vowels = 'аеиоуыэюяaeiouy'
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count
