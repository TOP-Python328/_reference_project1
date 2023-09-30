from collections.abc import Callable
from pathlib import Path
from random import sample, randrange as rr
from string import ascii_lowercase as letters
from sys import path
from time import perf_counter as pc


SRC_DIR = Path(path[0]).parent / 'src'
path.insert(1, str(SRC_DIR))


import data
import files


def generate_test_players(amount: int) -> data.Players:
    players = {}
    for _ in range(amount):
        name = ''.join(sample(letters, k=rr(5, 9))).capitalize()
        players[name] = {'побед': rr(10), 'поражений': rr(10), 'ничьих': rr(20)}
    return players


def generate_test_saves(amount: int) -> data.Saves:
    saves = {}
    for _ in range(amount):
        name1 = ''.join(sample(letters, k=rr(5, 9))).capitalize()
        name2 = ''.join(sample(letters, k=rr(5, 9))).capitalize()
        dim = rr(3, 21)
        all_cells = dim**2
        turns = [rr(1, all_cells+1) for _ in range(rr(2, all_cells-1))]
        saves[(name1, name2)] = (turns, dim)
    return saves


def test_func(func: Callable) -> float:
    start = pc()
    func()
    end = pc()
    return end - start



if __name__ == '__main__':
    
    quant = 10**6
    
    for n in (1, 10, 1000):
        data.players_db = generate_test_players(n)
        elapsed = test_func(files.write_players)
        print(f'elapsed time for {n} players file output: {elapsed*quant:.0f} us')
    
    for n in (1, 10, 1000):
        data.saves_db = generate_test_saves(n)
        elapsed = test_func(files.write_saves)
        print(f'elapsed time for {n} saves file output: {elapsed*quant:.0f} us')

