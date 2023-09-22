from sys import path
from timeit import timeit


def option_1(name1: str, name2: str):
    data = [
        {'игрок_1': [ {'побед': 2}, {'поражений': 3}, {'ничьих': 4} ]},
        {'игрок_2': [ {'побед': 0}, {'поражений': 0}, {'ничьих': 0} ]},
    ]
    
    for i, player in enumerate(data):
        if name1 in player:
            break
    
    data[i][name1][0]['побед'] += 1
    
    for i, player in enumerate(data):
        if name2 in player:
            break
    
    data[i][name2][1]['поражений'] += 1


def option_2(name1: str, name2: str):
    data = [
        {'игрок_1': [2, 3, 4]}, 
        {'игрок_2': [0, 0, 0]}, 
    ]
    
    for i, player in enumerate(data):
        if name1 in player:
            break
    
    data[i][name1][0] += 1
    
    for i, player in enumerate(data):
        if name2 in player:
            break
    
    data[i][name2][1] += 1


def option_3(name1: str, name2: str):
    data = {
        'игрок_1': {'побед': 2, 'поражений': 3, 'ничьих': 4},
        'игрок_2': {'побед': 0, 'поражений': 0, 'ничьих': 0},
    }
    data[name1]['побед'] += 1
    data[name2]['поражений'] += 1


def option_4(name1: str, name2: str):
    data = {
        'игрок_1': [2, 3, 4],
        'игрок_2': [0, 0, 0],
    }
    data[name1][0] += 1
    data[name2][1] += 1



if __name__ == '__main__':
    
    N = 1000
    quant = 10**6
    
    print(f"{timeit(lambda: option_1('игрок_2', 'игрок_1'), number=N)/N*quant:.3f} мкс")
    print(f"{timeit(lambda: option_2('игрок_2', 'игрок_1'), number=N)/N*quant:.3f} мкс")
    print(f"{timeit(lambda: option_3('игрок_2', 'игрок_1'), number=N)/N*quant:.3f} мкс")
    print(f"{timeit(lambda: option_4('игрок_2', 'игрок_1'), number=N)/N*quant:.3f} мкс")

