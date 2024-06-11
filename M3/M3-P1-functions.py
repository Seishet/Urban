def single_root_words(root_word, *other_words):
    same_words = []
    root = root_word.lower()
    for i in range(len(other_words)):
        word = other_words[i].lower()
        if root.count(word) > 0 or word.count(root) > 0:
            same_words.append(other_words[i])
    return same_words
print(single_root_words('disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

