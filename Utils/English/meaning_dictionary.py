def parse(file_name):
    dic = {}
    with open(file_name, encoding="utf-8") as f:
        for line in f:
            if len(line) < 4:
                continue
            ind = line.find("  ")
            if ind != -1:
                words = line[ind + 1:].strip().split()
                for i in range(len(words)):
                    try:
                        int(words[i])
                        words[i] = "\n\t" + words[i]
                    except ValueError:
                        pass
                dic[line[0:ind].lower()] = " ".join(words)
    return dic


word_dic = parse("Utils/English/Oxford English Dictionary.txt")


def get_definition(word: str):
    if word in word_dic:
        return word_dic[word]
    return "dictionary definition not found."
