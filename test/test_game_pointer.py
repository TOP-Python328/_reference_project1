from typing import Callable


def get_human_turn() -> int:
    """"""


def bot_hard_mode() -> int:
    """"""



TOKENS: tuple[str, str] = ('X', 'O')

active_players_names: list[str] = ['бот_сложный', 'игрок_1']
active_players_funcs: list[Callable] = [bot_hard_mode, get_human_turn]

for turn in range(9):
    # индекс-указатель
    pointer = turn % 2
    print(
        f'\n{turn=} {pointer=} {TOKENS[pointer]}', 
        '\n  ', active_players_names[pointer], 
        ': ', active_players_funcs[pointer].__name__, 
        sep=''
    )

