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
    dividers = ' \t\0'

    def adj(word, words, infl):
        word.add_part(PartOfSpeech.ADJECTIVE)
        if len(words) != 2:
            if words[2] == "COMP":
                word.comparative = infl
            elif words[2] == "SUPER":
                word.superlative = infl

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

    def prep(word, words, infl):
        word.add_part(PartOfSpeech.PREPOSITION)

    def det(word, words, infl):
        word.add_part(PartOfSpeech.DETERMINER)

    def conj(word, words, infl):
        word.add_part(PartOfSpeech.CONJUNCTION)

    def adv(word, words, infl):
        word.add_part(PartOfSpeech.ADVERB)

    switch = {"A": adj, "N": noun, "V": verb, "Prep": prep, "Det": det, "Conj": conj, "Adv": adv}

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
                dic[words[0]] = my_word
                dic[inflected] = my_word
                switch.get(words[1], lambda _x, _y, _z: None)(my_word, words, inflected)

    return dic


word_dic = parse_dictionary("Utils/English/morph_english.txt")
