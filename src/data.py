"""
Вспомогательный модуль — глобальные переменные и условные константы.
"""

# стандартная библиотека
from pathlib import Path
from sys import path, argv


# "флаг" внутреннего режима тестирования и отладки
DEBUG: bool = 'debug' in argv
# выводимые данные
debug_data: dict = {}


# переменные для аннотаций
Players = dict[str, dict[str, int]]
Saves = dict[tuple[str, str], tuple[list[int], int]]


# корень проекта
ROOT_DIR = Path(path[0]).parent
# каталог данных
DATA_DIR = ROOT_DIR / 'data'

# модификация путей для тестовых файлов данных
test_path = 'test/' if DEBUG else ''
# пути к файлам данных
players_path = DATA_DIR / f'{test_path}players.ini'
saves_path = DATA_DIR / f'{test_path}saves.ttt'


# база игроков
players_db: Players = {}
# база сохранений
saves_db: Saves = {}

