"""
Вспомогательный модуль — глобальные переменные и условные константы.
"""

# стандартная библиотека
from collections.abc import Sequence, Callable
from numbers import Real
from pathlib import Path
from re import compile
from sys import path, argv


# "флаг" внутреннего режима тестирования и отладки
DEBUG: bool = 'debug' in argv
# выводимые данные
debug_data: dict = {}


# переменные для аннотаций
Players = dict[str, dict[str, int]]
Saves = dict[tuple[str, str], tuple[list[int], int]]
SquareIndex = int
Series = Sequence[Real | str]
Matrix = Sequence[Series]


# корень проекта
ROOT_DIR = Path(path[0]).parent

# модификация пути для тестовых данных
test_path = '/test' if DEBUG else ''
# каталог данных
DATA_DIR = ROOT_DIR / f'data{test_path}'

# пути к файлам данных
players_path = DATA_DIR / 'players.ini'
saves_path = DATA_DIR / 'saves.ttt'


# база игроков
players_db: Players = {}
# база сохранений
saves_db: Saves = {}


# regex шаблон для имени игрока
NAME_PATTERN = compile(r'[A-Za-zА-ЯЁа-яё][A-Za-zА-ЯЁа-яё\d_]+')
# regex шаблон для размера игрового поля
DIM_PATTERN = compile(r'[3-9]|1[0-9]|20')


# текущий авторизованный игрок
authorized: str
# список имён активных игроков
active_players_names: list[str] = []
# список функций активных игроков
active_players_funcs: list[Callable] = []


# размер поля — все переменные, связанные с размером, вычисляются в utils.change_dim(), первый вызов со значением по умолчанию осуществляется в main.start()
dim: int = None
# числовая последовательность от 0 до размера поля
dim_range: range = None
# количество ячеек поля
all_cells: int = None
# числовая последовательность от 1 до количества ячеек поля
all_cells_range: range = None
# словарь всех ячеек игрового поля --> номер: ' '
empty: dict[int, str] = None
# шаблон игрового поля
field: str = None
# индексы выигрышных последовательностей
wins: list[set[int]] = None
# стратегические матрицы
start_matrices: tuple[Matrix, Matrix] = None


# строковые представления токенов
TOKENS = ('X', 'O')

# веса токенов
WEIGHT_OWN: float = 1.5
WEIGHT_FOE: float = 1.0
WEIGHTS: set[float] = {WEIGHT_OWN, WEIGHT_FOE}


# словарь сделанных ходов
turns: dict[int, str] = {}


# наименование приложения
APP_TITLE = 'КРЕСТИКИ-НОЛИКИ'
# названия и способы ввода команд главного меню
COMMANDS = {
    'начать новую партию': ('new', 'n', 'начать', 'н'),
    'загрузить существующую партию': ('load', 'l', 'загрузка', 'з'),
    'отобразить раздел помощи': ('help', 'h', 'помощь', 'п'),
    'создать или переключиться на игрока': ('player', 'p', 'игрок', 'и'),
    'отобразить таблицу результатов': ('table', 't', 'таблица', 'т'),
    'изменить размер поля': ('dim', 'd', 'размер', 'р'),
    'выйти': ('quit', 'q', 'выход', 'в'),
}
# тексты запросов, ответов и сообщений
MESSAGES = {
    'ввод команды': '\n _ введите команду > ',
    'некорректная команда': ' ! используйте команды из списка ниже',
    
    'ввод имени': '\n _ введите имя игрока > ',
    'некорректное имя': ' ! имя игрока должно начинаться с буквы, содержать только буквы, цифры и символ подчёркивания',
    
    'ввод размерности': ' _ введите новый размер поля > ',
    'некорректная размерность': ' ! размер поля должен находиться в диапазоне от 3 до 20',
    
    'ввод режима': '\n _ выберите режим игры\n    1 - один человек\n    2 - два человека\n > ',
    'ввод уровня': '\n _ выберите уровень сложности\n    1 - низкий (бот делает случайные ходы)\n    2 - высокий (бот стремится выиграть)\n > ',
    'ввод токена': '\n _ выберите токен, которым хотите играть\n    1 - крестик\n    2 - нолик\n > ',
    'некорректный выбор': ' ! введите цифру 1 или 2',
    
    'ввод сохранения': '\n _ выберите сохранение\n{}',
    'некорректное сохранение': ' ! введите число от 1 до {}',
    'нет сохранений': ' ! у вас нет ни одного сохранения',
    
    'ввод хода': '\n _ введите номер свободной ячейки > ',
    'ход не число': ' ! номер ячейки должен быть числом',
    'ход не в диапазоне': ' ! номер ячейки должен находиться в диапазоне от 1 до {} включительно',
    'ход в занятую': ' ! ячейка занята',
    
    'победитель': 'побеждает игрок {}',
    'ничья': 'ничья',
    
    # '': '',
}
