def parse():
    ph = {}
    words = {}
    words_by_first_three = {}
    with open("Utils/English/cmudict-0.7b.phones.txt") as f:
        for line in f:
            parts = line.split()
            ph[parts[0]] = parts[1]

    with open("Utils/English/cmudict-0.7b.txt") as f:
        for line in f:
            parts = line.split()
            l = [parts[i] if (len(parts[i]) == 1) else parts[i][0:2] for i in range(1, len(parts))]
            words[parts[0]] = l
            if parts[0][0:3] not in words_by_first_three:
                words_by_first_three[parts[0][0:3]] = []
            words_by_first_three[parts[0][0:3]].append(parts[0])

    return words_by_first_three, words, ph


words_by_first_three, words, phones = parse()


def get_closest_word(word: str):
    """
    Returns most similar word, only words with same first three letters are considered.
    :param word: one word string
    :return: string - a closest word
    """

    def same_c(w1, w2):
        s = 0
        for i in range(3,min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                s += 1
        return s

    closest = None
    cl_same = -1
    for word2 in words_by_first_three[word[0:3]]:
        curr_same = same_c(word, word2)
        if curr_same > cl_same:
            cl_same = curr_same
            closest = word2
    return closest


def get_indefinite_article(word: str):
    """
    Returns 'a', or 'an' if first sound is a vowel, searches for closest words if word not found
    :param word:
    :return:
    """
    word = word.upper()
    letter = words.get(word, None)
    if letter is not None:
        if phones[letter[0]] == "vowel":
            return "an"
    elif len(word) < 3:
        return "a"
    elif word[0:3] in words_by_first_three:
        return get_indefinite_article(get_closest_word(word))
    return "a"