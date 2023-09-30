"""
Вспомогательный модуль — чтение/запись файлов данных.
"""

# стандартная библиотека
from configparser import ConfigParser
# текущий проект
import data


def read_players() -> data.Players:
    """"""
    players = ConfigParser()
    players.read(data.players_path)
    return {
        player: {
            k: int(v)
            for k, v in players[player].items()
        }
        for player in players.sections()
    }


def read_saves() -> data.Saves:
    """"""
    raw = data.saves_path.read_text(encoding='utf-8').strip().split('\n')
    saves = {}
    for save in raw:
        try:
            players, turns, dim = save.split('!')
        # пустая строчка в файле
        except ValueError:
            continue
        players = tuple(players.split(','))
        try:
            turns = [int(t) for t in turns.split(',')]
        # сохранение до первого хода
        except ValueError:
            turns = []
        saves[players] = (turns, int(dim))
    return saves


def write_players() -> None:
    """"""
    players = ConfigParser()
    players.read_dict(data.players_db)
    with open(data.players_path, 'w', encoding='utf-8') as fileout:
        players.write(fileout)


def write_saves() -> None:
    """"""
    saves = []
    for players, save in data.saves_db.items():
        players = ','.join(players)
        turns, dim = save
        turns = ','.join(map(str, turns))
        saves.append(f"{players}!{turns}!{dim}")
    saves = '\n'.join(saves)
    data.saves_path.write_text(saves, encoding='utf-8')


