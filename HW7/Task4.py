# Завдання №4. Гра "Поле Чудес"
# У Вас є файл зі словами та поясненнями, кожна лінійка якого має формат:
# слово || Пояснення слова
# Для кожного слова застосовуємо такі правила:
# Спершу виводимо слово, кожна буква якого замінюється на *
# Користувач вводить букву, і там, де ця буква є у слові, * замінюється на неї, якщо ні,
# то лічильник невірних вгадувань інкрементується на 1
# Якщо користувач не вгадає букви довжина_слова * 2 (довжина слова - до 10 літер),
# інакше стільки невірних спроб, скільки букв у слові, гру програно
# Якщо всі букви вгадані, користувач виграв партію та отримує 32 / довжина_слова очків
# Перебіг гри побудувати на основі coroutine.
import os
import random


def read_and_separate():
    with open(os.path.join(os.path.curdir, "words_with_explanations.txt"), "r") as words:
        full_text = words.read()
        lines = full_text.split("\n")
    list1 = []
    for i in range(len(lines)):
        list1.append(lines[i].split(" || "))
    return list1


def get_word():
    list1 = read_and_separate()
    rand = random.randint(0, 42)
    word = list1[rand][0]
    explanation = list1[rand][1]
    print(explanation)
    print(word)
    return word


def play():
    word = get_word()
    hidden_word = list(word)
    for s in range(len(word)):
        hidden_word[s] = "*"
    print(''.join(hidden_word))
    count_of_fails = 0
    while True:
        new_letter = (yield)
        if word.count(new_letter) > 0:
            for i in range(len(word)):
                if new_letter == word[i]:
                    hidden_word[i] = new_letter
            print(f"You guessed letter")
            print(''.join(hidden_word))
            if ''.join(hidden_word) in ''.join(word):
                print(f"You win, the word is {''.join(hidden_word)}, you got {32//len(hidden_word)} points")
                break
        else:
            count_of_fails += 1
            print(f"No such letter in word. Attempts left: {(len(word)*2)-count_of_fails}")
            if count_of_fails == len(word)*2:
                print(f"You lose!")
                break


magic_field = play()
magic_field.__next__()

while True:
    try:
        magic_field.send(input("Input missed letter: "))
    except StopIteration as si:
        break
