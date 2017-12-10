class Rand:
    def __init__(self, seed=123456789):
        self.seed = seed

    def random(self):
        self.seed = (2147483629 * self.seed + 2147483587) % 2147483647
        return self.seed / 2147483647

    def randto(self, maximum):
        """
        Calculates random number from 0 to maximum, both inclusive
        :param maximum:
        :return:
        """
        self.seed = (2147483629 * self.seed + 2147483587) % 2147483647
        return self.seed % (maximum + 1)

    def randint(self, minimum, maximum):
        """
        Calculates random number from minimum to maximum, both inclusive
        :param minimum:
        :param maximum:
        :return:
        """
        self.seed = (2147483629 * self.seed + 2147483587) % 2147483647
        return int(self.seed / 2147483647 * (maximum - minimum) + minimum)
