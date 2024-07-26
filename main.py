# # Функциональный стиль программирования
# # map() --- замена циклу for
lst = ["1", "2", "3"]  # [1, 2, 3]
int_lst = []

for number in lst:
    int_lst.append(int(number))
print(lst)
print(int_lst)
# # -----------------------------------------------------------------------
gen_lst = [int(number) for number in lst]
print(gen_lst)
# # -----------------------------------------------------------------------
# # 1. Создаём переменную
# # 2. Вызов функции map() внутри переменной
# # 3. Внутри функции map() указываем с каким переменным мы работаем
# # 4. Слева от этой переменной указываем что(какую функцию, метод) применить
# # к элементам списка
map_lst = map(int, lst)
print(list(map_lst))
# --------------------------------------------------------------------------
names = ["dior", "muhammad", "sanjar"]
# ["Dior", "Muhammad", "Sanjar"]

map_names = map(str.capitalize, names)
print(names)
print(list(map_names))


# ----------------------------------------------------------------------------
def double_number(number: int):
    return number ** 2


lst = [23, 42, 55, 52, 63]
# # Получить список в котором эти элементы будут в квадрате
map_lst = map(double_number, lst)
print(lst)
print(list(map_lst))
# ----------------------------------------------------------------------------
# filter() --- фильтрует

words = ["purple", "yellow", "orange", "apple",
         "nokia", "windows", "transformer",
         "not", "ton", "bin", "olx", "code"]
# Отфильтровать эти слова
# Отдельно взять те слова в котором 5 букв или меньше
# Отдельно взять те слова в котором больше 5 букв
less_5 = []
more_5 = []
for word in words:
    if len(word) <= 5:
        less_5.append(word)
    else:
        more_5.append(word)
print(less_5)
print(more_5)

words = ["purple", "yellow", "orange", "apple",
         "nokia", "windows", "transformer",
         "not", "ton", "bin", "olx", "code"]


# ---------------------------------------------------------------------
# # 1. Создаём переменную
# # 2. Вызов функции filter() внутри переменной
# # 3. Внутри функции filter() указываем с каким переменным мы работаем
# # 4. Слева от этой переменной указываем что(какую функцию, метод) применить
def get_words_less_five(word: str):
    return len(word) <= 5


filter_lst = filter(get_words_less_five, words)
print(list(filter_lst))
# ----------------------------------------------------------------------------------
words = ["apple", "align", "alive", "after", "assembler", "application",
         "byd", "banana", "bmw", "brain", "brabus", "bentley", "brazilia"]


# Отфильтровать слова которые начинаются с буквы "а" и буквы "b"

def get_words_with_a(word: str):
    return word.startswith("a")


def get_words_with_b(word: str):
    return word.startswith("b")


filtered_a = filter(get_words_with_a, words)
print(list(filtered_a))

filtered_b = filter(get_words_with_b, words)
print(list(filtered_b))

# Git, GitHub
