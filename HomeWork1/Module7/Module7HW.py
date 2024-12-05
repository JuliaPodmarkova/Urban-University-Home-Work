class WordsFinder:

    def __init__(self, *file_txt):
        # объявление атрибута класса file_names
        self.file_names = file_txt

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                file = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(j, '')
                words = file.split()
                all_words[i] = words
        return all_words


    def find(self, word):
        result = {}
        for i, word_ in self.get_all_words().items():
            for j, wd in enumerate(word_, 1):
                if wd == word.lower():
                    result[i] = j
                    break
        return result


    def count(self, word):
        result_={}
        for i, word_ in self.get_all_words().items():
            result_[i] = word_.count(word.lower())
        return result_
print('work with test_file.txt')
finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print(finder1.find('TEXT'))
print(finder1.count('teXT'))
print('________________________')

print('work with Mother_Goose_Mondays_Child.txt')
finder2 = WordsFinder('Mother_Goose_Mondays_Child.txt')
print(finder2.get_all_words())
print(finder2.find('Child'))
print(finder2.count('Child'))
print('________________________')

print('work with RudyardKipling_If.txt')
finder3 = WordsFinder('RudyardKipling_If.txt')
print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))
print('________________________')

print('work with Walt_Whitman _O_Captain!_My_Captain!.txt')
finder4 = WordsFinder('Walt_Whitman _O_Captain!_My_Captain!.txt')
print(finder4.get_all_words())
print(finder4.find('captain'))
print(finder4.count('captain'))
print('________________________')
