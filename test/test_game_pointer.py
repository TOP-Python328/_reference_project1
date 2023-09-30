from typing import Callable


def get_human_turn() -> int:
    """"""


def bot_hard_mode() -> int:
    """"""


dim = 3
all_cells = dim**2

TOKENS: tuple[str, str] = ('X', 'O')

active_players_names: list[str] = ['бот_сложный', 'игрок_1']
active_players_funcs: list[Callable] = [bot_hard_mode, get_human_turn]

turns: dict[int, str] = {5: 'X', 1: 'O', 3: 'X'}

for turn in range(len(turns), all_cells):
    # индекс-указатель
    pointer = turn % 2
    print(
        f'\n{turn=} {pointer=} {TOKENS[pointer]}',
        '\n  ', active_players_names[pointer],
        ': ', active_players_funcs[pointer].__name__,
        sep=''
    )

