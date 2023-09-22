from pathlib import Path
from sys import path
from timeit import timeit


saves_db  = {
    ('игрок_2', 'игрок_1'): ([7, 9, 10, 22, 1, 20], 5),
}

def parse_to_string() -> str:

    saves_txt = []
    for players, save in saves_db.items():
        players = ','.join(players)
        turns, dim = save
        turns = ','.join(str(t) for t in turns)
        saves_txt.append(f'{players}!{turns}!{dim}')
    return '\n'.join(saves_txt)


save = 'игрок_2,игрок_1!7,9,10,22,1,20!5'

def parse_from_string() -> dict:
    saves_db = {}
    
    players, turns, dim = save.split('!')
    players = tuple(players.split(','))
    turns = [int(t) for t in turns.split(',')]
    
    saves_db[players] = (turns, int(dim))
    return saves_db


saves_path = Path(path[0]) / 'saves.ttt'

def write_save(saves: str) -> None:
    saves_path.write_text(saves, encoding='utf-8')



if __name__ == '__main__':
    
    N = 1000
    quant = 10**6
    
    saves = parse_to_string()
    
    print(f"{timeit(parse_to_string, number=N)/N*quant:.1f} мкс")
    print(f"{timeit(parse_from_string, number=N)/N*quant:.1f} мкс")
    print(f"{timeit(lambda: write_save(saves), number=N)/N*quant:.0f} мкс")

