"""
Вспомогательный модуль — дополнительные функции.
"""

# текущий проект
import bot
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
    data.start_matrices = (
        bot.calc_sm_cross(),
        bot.calc_sm_zero()
    )
    data.MESSAGES['ход не в диапазоне'].format(data.all_cells)


def generate_field_template(dimension: int) -> str:
    """"""


def generate_win_combinations(dimension: int) -> list[set[int]]:
    """"""


def concatenate_rows(
        multiline1: str,
        multiline2: str,
        *multilines: str,
        padding: int = 8
) -> str:
    """Объединяет произвольное количество строк текстов-колонок в одну строку с несколькими колонками и отступом между ними.

    :param padding: ширина отступа между колонками в пробелах
    """
    multilines = multiline1, multiline2, *multilines
    multilines = [m.split('\n') for m in multilines]
    padding = ' '*padding
    return '\n'.join(
        padding.join(row)
        for row in zip(*multilines)
    )


