"""
Вспомогательный модуль — дополнительные функции.
"""

# текущий проект
import data


def change_dimension(new_dimension: int) -> None:
    """Переопределяет все глобальные переменные, связанные с размером игрового поля."""
    data.dim = new_dimension
    data.all_cells = new_dimension ** 2
    data.dim_range = range(new_dimension)
    data.all_cells_range = range(1, data.all_cells+1)
    data.empty = dict.fromkeys(data.all_cells_range, ' ')
    data.field = generate_field_template(new_dimension)
    data.wins = generate_win_combinations(new_dimension)
    data.MESSAGES['ход не в диапазоне'].format(data.all_cells)


def generate_field_template(dimension: int) -> str:
    """"""


def generate_win_combinations(dimension: int) -> list[set[int]]:
    """"""


