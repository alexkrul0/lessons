class WordsFinder:

    def __init__(self, *args):
        self.args = args
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}


        for name in self.file_names:
            word_list = []

            with open(name, encoding='utf-8') as file:

                for line in file:
                    line = line.lower()
                    marks = ',.=!?;:-'
                    for x in line:
                        if x in marks:
                            line = line.replace(x, '')

                    word_list.extend(line.split())
                all_words[name] = word_list
        return all_words

    def find(self, word):
        words = []
        word = word.lower()
        key_ = None
        for keys, value in self.get_all_words().items():
            words.extend(value)
            key_ = keys
        pos = words.index(word)
        return {key_: pos + 1}

    def count(self, word):
        words = []
        word = word.lower()
        key_ = None
        for keys, value in self.get_all_words().items():
            words.extend(value)
            key_ = keys
        count_ = words.count(word)
        return {key_: count_}


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
