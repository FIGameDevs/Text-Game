numbers_to_text = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",  # yes it is
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
    1000000: "million",
    1000000000: "billion"
}


def rev(dic):
    ndic = {}
    for k, v in dic.items():
        ndic[v] = k
    return ndic


text_to_numbers = rev(numbers_to_text)


def change_to_number(text: str):
    words = text.replace(",", "").replace("-", " ").split()
    if words[0] == "zero":
        return 0, False
    minus = words[0] == "minus"
    if minus:
        words.pop(0)
    number = 0
    curr_part = 0
    said_zero = False
    ordinal = False
    for word in words:
        n = 0
        if word not in text_to_numbers:
            ordinal = True
            if word == "first":
                n = 1
            elif word == "second":
                n = 2
            elif word == "third":
                n = 3
            elif word[-3:] == "fth" and word[:-3] + "ve" in text_to_numbers:
                n = text_to_numbers[word[:-3] + "ve"]
            elif word[-2:] == "th" and word[:-2] + "e" in text_to_numbers:
                n = text_to_numbers[word[:-2] + "e"]
            elif word[-4:] == "ieth" and word[:-4] + "y" in text_to_numbers:
                n = text_to_numbers[word[:-4] + "y"]
            elif word[-2:] == "th" and word[:-2] in text_to_numbers:
                n = text_to_numbers[word[:-2]]
            else:
                return None, False
        else:
            n = text_to_numbers[word]
        if n == 0:
            said_zero = True
        if n < 100:
            curr_part += n
        elif n < 1000:
            if curr_part == 0 and not said_zero:
                curr_part = 1
            curr_part *= n
        else:
            if curr_part == 0 and not said_zero:
                curr_part = 1
            curr_part *= n
            number += curr_part
            curr_part = 0
    number += curr_part
    if minus:
        number *= -1
    return number, ordinal


def change_to_text(number: int, ordinal=False):
    text = ""
    minus = number < 0
    number = abs(number)
    billions = number // 1000000000
    number %= 1000000000
    millions = number // 1000000
    number %= 1000000
    thousands = number // 1000
    number %= 1000
    if minus:
        text += "minus "
    if billions > 0:
        text += up_to_hundreds(billions) + " billion, "
    if millions > 0:
        text += up_to_hundreds(millions) + " million, "
    if thousands > 0:
        text += up_to_hundreds(thousands) + " thousand, "
    if number > 0:
        if ordinal:
            text += up_to_hundreds_ordinal(number)
        else:
            text += up_to_hundreds(number)
    elif ordinal:
        text = text[:-1] + "th"
    if len(text) == 0:
        return "zero"
    if len(text.split()) < 5:
        text = text.replace(",", "")
    return text.strip().strip(",")


def up_to_hundreds(number):
    text = ""
    hundreds = number // 100
    number %= 100
    tens = number // 10
    number %= 10
    ones = number
    if hundreds > 0:
        text += numbers_to_text[hundreds] + " hundred "
    if tens > 1:
        text += numbers_to_text[tens * 10]
    elif tens > 0:
        text += numbers_to_text[10 * tens + ones]
    if tens > 1 and ones > 0:
        text += "-" + numbers_to_text[ones]
    elif tens == 0 and ones > 0:
        text += numbers_to_text[ones]
    return text.strip()


def up_to_hundreds_ordinal(number: int):
    text = ""
    hundreds = number // 100
    number %= 100
    tens = number // 10
    number %= 10
    ones = number
    if hundreds > 0:
        text += numbers_to_text[hundreds] + " hundred "
    if tens > 1:
        text += numbers_to_text[tens * 10]
    elif tens > 0:
        text += numbers_to_text[10 * tens + ones]
    if tens > 1 and ones > 0:
        text += "-"
    elif tens == 0 and ones > 0:
        if ones == 1:
            text += "first"
        elif ones == 2:
            text += "second"
        elif ones == 3:
            text += "third"
        else:
            n_t = numbers_to_text[ones]
            if n_t[-1] == "e" and n_t[-2] == "v":
                text += n_t[:-2] + "fth"
            elif n_t[-1] == "e":
                text += n_t[:-1] + "th"
            elif n_t[-1] == "y":
                text += n_t[:-1] + "ieth"
            else:
                text += "th"
    else:
        if text[-1] == "e" and text[-2] == "v":
            text = text[:-2] + "fth"
        elif text[-1] == "e":
            text = text[:-1] + "th"
        elif text[-1] == "y":
            text = text[:-1] + "ieth"
        else:
            text += "th"
    return text.strip()


"""
print(change_to_number(change_to_text(2, True)))
print(change_to_number(change_to_text(-9000, True)))
print(change_to_number(change_to_text(8001, True)))
print(change_to_number(change_to_text(7895, False)))
print(change_to_number(change_to_text(99999999999, False)))
print(change_to_number(change_to_text(3, False)))
print(change_to_text(15, True))
print(change_to_number(change_to_text(15, True)))
print(change_to_text(11, True))
print(change_to_number(change_to_text(11, True)))
print(change_to_number(change_to_text(90000000001, False)))
"""
# TODO first, second...
