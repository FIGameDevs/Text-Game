from .dictionary import add_word, get_base_word
from enum import IntFlag


class KeyWordType(IntFlag):
    NONE = 0
    COMMAND = 1
    ENTITY = 2


word_dic = {}


def add_command(word):
    word = word.lower()
    if word in word_dic:
        word_dic[word] |= KeyWordType.COMMAND
    else:
        word_dic[word] = KeyWordType.COMMAND


def add_entity(word):
    word = word.lower()
    if word in word_dic:
        word_dic[word] |= KeyWordType.ENTITY
    else:
        word_dic[word] = KeyWordType.ENTITY


def is_keyword(word):
    word = word.lower()
    return word in word_dic


def is_specific_keyword(word: str, kw: KeyWordType):
    word = word.lower()
    if word in word_dic:
        return word_dic[word] & kw == kw
    return False


def get_keyword(word):
    word = word.lower()
    return word_dic.get(word)
