"""
Точка входа. 
Модуль верхнего уровня.
"""

# текущий проект
import data
import files
import help
import utils



def start():
    """"""
    data.players_db = files.read_players()
    data.saves_db = files.read_saves()
    
    if not data.players_db:
        print(help.render_all())
    
    ...
    
    utils.change_dimension(3)



def mainloop():
    """"""
    while True:
        command = input(data.MESSAGES['ввод команды'])
        
        if command in data.COMMANDS['начать новую партию']:
            ...
        
        # elif command in data.COMMANDS[...]:
        
        elif command in data.COMMANDS['выйти']:
            break



def end():
    """"""



if __name__ == '__main__':
    start()
    mainloop()
    end()

