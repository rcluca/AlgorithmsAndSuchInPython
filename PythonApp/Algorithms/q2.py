# Time Spent on Question:
# 20

def get_missing_letters(sentence):
    sentence = sentence.lower()

    # setup alphabet in set for quick search
    letters = set()
    for i in range(97,123):
        letters.add(chr(i))

    # remove characters in sentence from letters
    for char in sentence:
        if char in letters:
            letters.remove(char)

    # return a sorted string of the missing letters
    return "".join(sorted(letters))