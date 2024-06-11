def single_root_words(root_word, *other_words):
    same_words = []
    root_word.lower()
    for i in range(len(other_words)):
        if root_word in other_words[i].lower() or other_words[i].lower() in root_word:
            same_words.append(other_words[i])
    return same_words
print(single_root_words('disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

