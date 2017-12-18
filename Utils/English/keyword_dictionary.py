from .dictionary import add_word, get_base_word
from enum import IntFlag


class KeyWordType(IntFlag):
    NONE = 0
    COMMAND = 1
    ENTITY = 2


word_dic = {}


def add_command(word):
    if word in word_dic:
        word_dic[word] |= KeyWordType.COMMAND
    else:
        word_dic[word] = KeyWordType.COMMAND


def add_entity(word):
    if word in word_dic:
        word_dic[word] |= KeyWordType.ENTITY
    else:
        word_dic[word] = KeyWordType.ENTITY


def is_keyword(word):
    return word in word_dic


def get_keyword(word):
    return word_dic.get(word, default=KeyWordType.NONE)
