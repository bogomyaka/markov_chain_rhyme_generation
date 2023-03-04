import markovify
import sentence_generation

MAX_TRIES = 10000

class MarkovModel(markovify.Text):
    def __init__(self, **kwargs):
        #Класс наследуется от markovify.Text,
        #поэтому вызываем инит родительского класса с переданным 
        #словарем параметров.
        super().__init__(**kwargs)
    
    def generate_rhyme(self, total_couplets=2, max_tries=MAX_TRIES):
        """
        Генерирует рифму с заданным количеством двустиший и попыток.
        
            total_couplets: количество двустиший.
            max_tries: максимальное количество попыток
            придумать рифму к предложению. Если оно исчерпано, 
            то рифма ищется относительно нового сгенерированного 
            предложения.
        """
        couplets = 0

        while couplets != total_couplets:
            first_sentence = sentence_generation.Sentence(self)
            second_sentence = sentence_generation.Sentence(self)

            tries = 0
            complete_rhyme = True
            while not any(first_sentence.end_syllables.intersection(second_sentence.end_syllables)) or first_sentence.last_word == second_sentence.last_word:
                if tries > max_tries:
                    complete_rhyme = False
                    break
                second_sentence = sentence_generation.Sentence(self)
                tries += 1
            
            if complete_rhyme:
                print(f"{first_sentence.text}\n{second_sentence.text}")
                couplets += 1
                if couplets % 2 == 0:
                    print('\n')