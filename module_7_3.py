class WordsFinder(object):

    def __init__(self, *file_names):
        self.file_names = file_names

    @staticmethod
    def __get_words_from_file(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            # Для начала считываем файл в строку и удаляем перевод строки
            text = file.read().replace('\n', ' ')
            # далее удаляем все символы кроме букв и пробелов
            text = ''.join(char for char in text if char.isalpha() or char.isspace() or char == '-')
            # убираем артефакты типа "-буква" или "буква-" (пример изначальное слово 'utf-8')
            text = text.replace(' -', ' ').replace('- ', ' ')
            # перед возвратом убираем лишние пробелы и разделяем слова в список используя разделитель - пробел
        return ' '.join(text.split()).split()

    def get_all_words(self):
        dict_words = {}
        for file_name in self.file_names:
            words = self.__get_words_from_file(file_name)
            dict_words[file_name] = words
        return dict_words

    def find(self, word):
        result = {}
        for file, words in self.get_all_words().items():
            words_lower = [word.lower() for word in words]
            if word.lower() in words_lower:
                result[file] = words_lower.index(word.lower())
        return result

    def count(self, word):
        result = {}
        for file, words in self.get_all_words().items():
            words_lower = [word.lower() for word in words]
            if word.lower() in words_lower:
                result[file] = words_lower.count(word.lower())
        return result


if __name__ == '__main__':
    wf = WordsFinder('test1.txt', 'test2.txt', 'test3.txt', 'test.txt')
    print(wf.get_all_words())
    print(wf.find('таким'))
    print(wf.count('В'))
