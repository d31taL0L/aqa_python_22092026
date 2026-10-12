adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
removed_space = adwentures_of_tom_sawer.replace("\n", " ")
print(removed_space)

# task 02 ==
""" Замініть .... на пробіл
"""
removed_dots = removed_space.replace("....", " ")
print(removed_dots)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
removed_additional_spaces = removed_dots.replace("  ", "") # Надалі, ми будемо використовувати саму цю зміну з текстом
print(removed_additional_spaces)

print("=================================================")
# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h_letters = 0
for letter in removed_additional_spaces:
    if letter.lower() == "h":
        count_h_letters += 1
print(f"Quantity of 'h' letters: {count_h_letters}")

print("=================================================")
# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list_of_words = removed_additional_spaces.split()
count_words = 0

for word in list_of_words:
    if word.istitle():
        count_words += 1

print(f"Number of words: {count_words}")

print("=================================================")
# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
name = "Tom"
first_name_index = removed_additional_spaces.find(name)
second_name_index = removed_additional_spaces.find(name, first_name_index + len(name))
if second_name_index != -1:
    print(f"Second {name} index: {second_name_index}")
else:
    print(f"ERROR: Second {name} was not found.")

print("=================================================")
# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = removed_additional_spaces.split(". ", -1)
print(adwentures_of_tom_sawer_sentences)

print("=================================================")
# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
print(fourth_sentence.lower())

print("=================================================")
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
sentence_exist = False
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        sentence_exist = True
        break

if sentence_exist:
    print("Sentence exists.")
else:
    print("Sentence does not exist.")

print("=================================================")
# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
split_sentence = last_sentence.split()
print(f"Quantity of the last sentence: {len(split_sentence)}")
