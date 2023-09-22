from itertools import islice
from timeit import timeit


wins = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},
    {1, 4, 6},
    {2, 5, 8},
    {3, 6, 9},
    {1, 5, 9},
    {3, 5, 7},
]
TOKENS = ('X', 'O')
field_template = ' {} | {} | {} \n———————————\n {} | {} | {} \n———————————\n {} | {} | {} '


empty_d = dict.fromkeys(range(1, 10), ' ')

def option_1(new_turn: int):
    turns = {5: 'X', 3: 'O', 9: 'X'}
    
    # добавление хода
    turns[new_turn] = TOKENS[1]
    
    # генерация строки игрового поля для вывода в stdout
    field = (empty_d | turns).values()
    field_template.format(*field)
    
    # проверка достижения победы
    zeros = set(islice(turns, 1, None, 2))
    for comb in wins:
        if comb <= zeros:
            return True
    else:
        return False


empty_l = [' ']*9

def option_2(new_turn: int):
    turns = [5, 3, 9]
    
    # добавление хода
    turns.append(new_turn)
    
    # генерация строки игрового поля для вывода в stdout
    field = empty_l.copy()
    for i, cell in enumerate(turns):
        field[cell-1] = TOKENS[i%2]
    field_template.format(*field)
    
    # проверка достижения победы
    zeros = set(turns[1::2])
    for comb in wins:
        if comb <= zeros:
            return True
    else:
        return False



# ход в занятую ячейку
# генерация строки во время записи файла сохранения
# парсинг строки во время чтения файла сохранения
# вывод двух последних ходов во время загрузки


if __name__ == '__main__':
    
    N = 1000
    quant = 10**6
    
    print(f"{timeit(lambda: option_1(1), number=N)/N*quant:.2f} мкс")
    print(f"{timeit(lambda: option_2(1), number=N)/N*quant:.2f} мкс")

