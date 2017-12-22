from enum import IntFlag


class PartOfSpeech(IntFlag):
    NONE = 0
    NOUN = 1
    ADJECTIVE = 2
    VERB = 4
    PRONOUN = 8
    PREPOSITION = 16
    DETERMINER = 32
    CONJUNCTION = 64
    ADVERB = 128


class Word:
    def __init__(self):
        self.part = PartOfSpeech.NONE

    def add_part(self, part_of_speech):
        self.part |= part_of_speech

    def __str__(self):
        text = ""
        for k, v in self.__dict__.items():
            text += k + ": " + str(v) + '\n'
        return text


def parse_dictionary(path):
    dic = {}
    words_by_first_three = {}
    base_words_by_first = {}

    def adj(word, words, infl):
        word.add_part(PartOfSpeech.ADJECTIVE)
        if len(words) != 2:
            if words[2] == "COMP":
                word.comparative = infl
            elif words[2] == "SUPER":
                word.superlative = infl
        else:
            word.adjective = infl

    def noun(word, words, infl):
        word.add_part(PartOfSpeech.NOUN)
        if words[2] == "3sg":
            if len(words) == 3 or words[3] != "GEN":
                word.third_singular = infl
            else:
                word.third_singular_gen = infl
        else:
            if len(words) == 3 or words[3] != "GEN":
                word.third_plural = infl
            else:
                word.third_plural_gen = infl

    def verb(word, words, infl):
        word.add_part(PartOfSpeech.VERB)
        word.present = words[0]
        if words[2] == "INF":
            word.infinitive = infl
        elif words[2] == "3sg" and words[3] == "PRES":
            word.third_singular_present = infl
        elif words[2] == "PROG":
            word.progressive = infl
        elif words[2] == "PAST":
            word.past = infl
        elif words[2] == "PPART":
            word.past_particle = infl

    def pron(word, words, infl):
        word.add_part(PartOfSpeech.PRONOUN)
        if len(words) != 2:
            if len(words) != 3:
                if words[3] == "acc":
                    if words[2] == "1sg":
                        word.first_sing_pron_obj = infl
                    elif words[2] == "2sg":
                        word.second_sing_pron_obj = infl
                    elif words[2] == "3sg":
                        word.third_sing_pron_obj = infl
                    elif words[2] == "1pl":
                        word.first_plur_pron_obj = infl
                    elif words[2] == "2pl":
                        word.second_plur_pron_obj = infl
                    elif words[2] == "3pl":
                        word.third_plur_pron_obj = infl
                elif words[3] == "refl":
                    if words[2] == "1sg":
                        word.first_sing_pron_refl = infl
                    elif words[2] == "2sg":
                        word.second_sing_pron_refl = infl
                    elif words[2] == "3sg":
                        word.third_sing_pron_refl = infl
                    elif words[2] == "1pl":
                        word.first_plur_pron_refl = infl
                    elif words[2] == "2pl":
                        word.second_plur_pron_refl = infl
                    elif words[2] == "3pl":
                        word.third_plur_pron_refl = infl
                elif words[3] == "nomacc":
                    if words[2] == "1sg":
                        word.first_sing_pron = infl
                        word.first_sing_pron_obj = infl
                    elif words[2] == "2sg":
                        word.second_sing_pron = infl
                        word.second_sing_pron_obj = infl
                    elif words[2] == "3sg":
                        word.third_sing_pron = infl
                        word.third_sing_pron_obj = infl
                    elif words[2] == "1pl":
                        word.first_plur_pron = infl
                        word.first_plur_pron_obj = infl
                    elif words[2] == "2pl":
                        word.second_plur_pron = infl
                        word.second_plur_pron_obj = infl
                    elif words[2] == "3pl":
                        word.third_plur_pron = infl
                        word.third_plur_pron_obj = infl
                elif words[2] == "GEN":
                    if words[3] == "ref1sg":
                        word.first_sing_pron_poss = infl
                    elif words[3] == "ref2sg":
                        word.second_sing_pron_poss = infl
                    elif words[3] == "ref3sg":
                        word.third_sing_pron_poss = infl
                    elif words[3] == "ref1pl":
                        word.first_plur_pron_poss = infl
                    elif words[3] == "ref2pl":
                        word.second_plur_pron_poss = infl
                    elif words[3] == "ref3pl":
                        word.third_plur_pron_poss = infl
                else:
                    if words[2] == "1sg":
                        word.first_sing_pron = infl
                    elif words[2] == "2sg":
                        word.second_sing_pron = infl
                    elif words[2] == "3sg":
                        word.third_sing_pron = infl
                    elif words[2] == "1pl":
                        word.first_plur_pron = infl
                    elif words[2] == "2pl":
                        word.second_plur_pron = infl
                    elif words[2] == "3pl":
                        word.third_plur_pron = infl
            else:
                if words[2] == "1sg":
                    word.first_sing_pron = infl
                elif words[2] == "2sg":
                    word.second_sing_pron = infl
                elif words[2] == "3sg":
                    word.third_sing_pron = infl
                elif words[2] == "1pl":
                    word.first_plur_pron = infl
                elif words[2] == "2pl":
                    word.second_plur_pron = infl
                elif words[2] == "3pl":
                    word.third_plur_pron = infl

    def prep(word, words, infl):
        word.add_part(PartOfSpeech.PREPOSITION)

    def det(word, words, infl):
        word.add_part(PartOfSpeech.DETERMINER)

    def conj(word, words, infl):
        word.add_part(PartOfSpeech.CONJUNCTION)

    def adv(word, words, infl):
        word.add_part(PartOfSpeech.ADVERB)

    switch = {"A": adj, "N": noun, "V": verb, "Prep": prep, "Det": det, "Conj": conj, "Adv": adv, "Pron": pron}

    with open(path) as f:
        for line in f:
            if line[0] == ';':
                continue
            variants = line.split('#')
            inflected = variants[0].strip("\t\0").split()[0]
            for i in range(len(variants)):
                words = variants[i].strip("\t\0").split()
                if i == 0:
                    for j in range(len(words) - 1):
                        words[j] = words[j + 1]
                my_word = dic.get(words[0], Word())
                my_word.base_word = words[0]
                if words[0].lower() not in dic:
                    dic[words[0].lower()] = my_word
                if inflected.lower() not in dic:
                    dic[inflected.lower()] = my_word
                switch.get(words[1], lambda _x, _y, _z: None)(my_word, words, inflected)
                if words[0][0:3] not in words_by_first_three:
                    words_by_first_three[words[0][0:3]] = []
                if inflected[0:3] not in words_by_first_three:
                    words_by_first_three[inflected[0:3]] = []
                words_by_first_three[words[0][0:3]].append(words[0])
                words_by_first_three[inflected[0:3]].append(inflected)
                if words[0][0].lower() not in base_words_by_first:
                    base_words_by_first[words[0][0].lower()] = []
                base_words_by_first[words[0][0].lower()].append(words[0])

    for k, v in words_by_first_three.items():
        v.sort()
    return base_words_by_first, words_by_first_three, dic


base_words_by_first, words_by_first_three, word_dic = parse_dictionary("Utils/English/morph_english.txt")


def add_word(word):
    if word not in word_dic:
        w = Word()
        w.base_word = word
        word_dic[word.lower()] = w


def get_word(word):
    word = word.lower()
    if word in word_dic:
        return word_dic[word]


def get_base_word(word):
    word = word.lower()
    if word in word_dic:
        return word_dic[word].base_word
    return word


def is_in_dictionary(word):
    word = word.lower()
    return word in word_dic


def get_closest_word_baseonly(word: str):
    if word is None or len(word) == 0:
        return "none"
    word = word.lower()

    if word in word_dic:
        return word

    def count_same(w1, w2):
        s = 0
        if len(w1) == len(w2):
            s = 0.5
        for i in range(1, min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                s += 1
        return s

    closest = "none"
    cl_same = -1
    if word[0] not in base_words_by_first:
        return "none"
    for tryword in base_words_by_first[word[0]]:
        same = count_same(word, tryword)
        if same > cl_same:
            cl_same = same
            closest = tryword
        if cl_same + 1.51 >= len(word):
            break
    return closest


def get_closest_word_precise(word: str):
    """
    Returns most similar word, only words with same first three letters are considered.
    :param word: one word string
    :return: string - a closest word
    """
    if len(word) < 3:
        return "none"
    word = word.lower()

    def same_c(w1, w2):
        s = 0
        for i in range(3, min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                s += 1
        return s

    closest = None
    cl_same = -1
    if word[0:3] not in words_by_first_three:
        return "none"
    for word2 in words_by_first_three[word[0:3]]:
        curr_same = same_c(word, word2)
        if curr_same > cl_same:
            cl_same = curr_same
            closest = word2
    return closest


def get_closest_word(word: str):
    """
    Returns most similar word, only words with same first three letters are considered.
    :param word: one word string
    :return: string - a closest word
    """
    if len(word) < 3:
        return "none"
    word = word.lower()

    def same_c(w1, w2):
        s = 0
        for i in range(3, min(len(w1), len(w2))):
            if w1[i] == w2[i]:
                s += 1
        return s

    closest = None
    cl_same = -1
    if word[0:3] not in words_by_first_three:
        return "none"
    for word2 in words_by_first_three[word[0:3]]:
        curr_same = same_c(word, word2)
        if curr_same > cl_same:
            cl_same = curr_same
            closest = word2
        if cl_same > 1:
            break
    return closest


alpha_whitelist = set('abcdefghijklmnopqrstuvwxy ABCDEFGHIJKLMNOPQRSTUVWXYZ')


def to_present(sentence):
    new_s = ''.join(filter(alpha_whitelist.__contains__, sentence))
    words = new_s.split()
    new_s = sentence
    if words[0] not in word_dic and words[0].lower() in word_dic:
        new_s = new_s[0].lower() + new_s[1:]
        words[0] = words[0].lower()

    new_s = new_s.replace("have done", "do")
    new_s = new_s.replace("have had", "have")
    new_s = new_s.replace("could", "can")

    for i in range(len(words)):
        if words[i] == "will":
            new_s = new_s.replace(" will", "", 1)
            words[i] = words[i - 1]
        elif words[i] == "be":
            if words[i - 1] == "I":
                new_s = new_s.replace("be", "am", 1)
            elif words[i - 1] == "you" or words[i - 1] == "they" or words[i - 1] == "we":
                new_s = new_s.replace("be", "are", 1)
            else:
                new_s = new_s.replace("be", "is", 1)
        if words[i] in word_dic and word_dic[words[i]].part & PartOfSpeech.VERB == PartOfSpeech.VERB:
            if words[i - 1] == "she" or words[i - 1] == "he" or words[i - 1] == "it":
                try:
                    new_s = new_s.replace(words[i], word_dic[words[i]].third_singular_present, 1)
                except AttributeError:
                    pass
            if words[i - 1] == "on":
                new_s = new_s.replace(words[i], word_dic[words[i]].progressive, 1)
            elif words[i - 1] != "the" and words[i - 1] != "very":
                new_s = new_s.replace(words[i], word_dic[words[i]].present, 1)

    if sentence[0].isupper():
        new_s = new_s[0].upper() + new_s[1:]
    return new_s
