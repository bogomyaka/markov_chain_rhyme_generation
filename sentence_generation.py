import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import cmudict

MIN_WORDS = 5
MAX_WORDS = 8
MAX_TRIES = 10000
STRESSES = {'0', '1', '2'}

class Sentence:
    def __init__(self, model, min_words=MIN_WORDS, max_words=MAX_WORDS, max_tries=MAX_TRIES):
        """
        Инициализирует созданный экзепляр класса:
        генерирует текст предложения, а также сохраняет в атрибуты
        последнее слово предложения и его последний слог.

            model: модель, генерирующая текст. 
            min_words: минимальное количество слов в предложении.
            max_words: максимальное количество слов в предложении.
            max_tries: максимальное количество попыток на генерацию 
            предложения с заданными параметрами.  
        """
        self.text = model.make_sentence(min_word=min_words, max_words=max_words, tries=max_tries)
        self.last_word = Sentence.get_last_word(self.text)
        self.end_syllables = Sentence.get_endings(self.last_word)
    
    @staticmethod
    def get_last_word(sentence: str) -> str:
        """
        Возвращает последний токен из переданной строки пропуская символы, не
        являющиеся буквами (очень по-русски написано, да).

            sentence: предложение, для которого нужно получить
            последнее слово.
        """
        return RegexpTokenizer(r'\w+').tokenize(sentence)[-1]
    
    @staticmethod
    def get_endings(last_word: str) -> set:
        """
        Возвращает множество последних слогов слова (т.к. слово
        может иметь несколько произношений).

            last_word: слово, для которого нужно получить
            множество последних слогов.
        """
        pronunciations = [pron for (word, pron) in cmudict.entries() if word == last_word]
        endings = set()

        for p in pronunciations:
            idx = -1
            phoneme = p[idx]

            while not any(stress in phoneme for stress in STRESSES):
                idx -= 1
                phoneme = p[idx]
                
            endings.add(tuple(p[idx:]))

        return endings
    
    @staticmethod
    def count_syllables(sentence: str) -> int:
        """
        Считает количество слогов в предложении.
        
            sentence: предложение, для которого нужно посчитать
            количество слогов.
        """
        syllables = 0
        tokens = RegexpTokenizer(r"\w+").tokenize(sentence)

        for token in tokens:
          pronunciations = [pron for (word, pron) in cmudict.entries() if word == token]
          if not pronunciations:
            break
          
          for phoneme in pronunciations[0]:
            if any(stress in phoneme for stress in STRESSES):
              syllables += 1

        return syllables