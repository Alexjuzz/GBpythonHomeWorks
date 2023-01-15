class MinMaxWordFinder:

    def __init__(self):
        self.sentence_list = []

    def sentence_add(self, text: str):
        text_list = text.split()
        self.sentence_list.extend(text_list)

    def ListShortWord(self):
        size = 1000
        res_list = []
        for _ in self.sentence_list:
            if len(_) < size:
                size = len(_)
        for _ in self.sentence_list:
            if len(_) == size:
                res_list.append(_)

        return res_list

    def ListLongWord(self):
        size = 0
        res_list = []
        for _ in self.sentence_list:
            if len(_) > size:
                size = len(_)
        for _ in self.sentence_list:
            if len(_) == size:
                res_list.append(_)

        return res_list





