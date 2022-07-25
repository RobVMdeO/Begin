import random
from hangman_visual import lives_visual_dict
import string

palabras = ['árbol','brisa','canoa','dermatología','estetoscopio','flatulencia','gelatina','hipopotamo','iguana',
            'jabalina','kiwi','lombrices','maremoto','novelezco','ñoqui','operador','perìmetro','quinta','resoluciòn',
            'salchicha','trepamuros','urticaria','viajero','Waldemar','explosión','Yamandú','zaracatunga']


def get_valid_word(palabras):
    word = random.choice(palabras)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(palabras)

    return word.upper()


def hangman():
    word = get_valid_word(palabras)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('\nTe quedan', lives, 'vidas y has usado estas letras: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Palabra actual: ', ' '.join(word_list))

        user_letter = input('Elige una letras: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nTu letra,', user_letter, 'no está en la palabra.')

        elif user_letter in used_letters:
            print('\nYa has usado esa letra. Elige otra letra.')

        else:
            print('\nEsa no es una letra válida.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('Has muerto, lo siento. La palabra era', word)
    else:
        print('EXCELENTE!!! Adivinaste la palabra:', word, '!!!')


if __name__ == '__main__':

    hangman()