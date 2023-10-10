import os
import sys

class Singleton():
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance 

class Error(Singleton):
    message = ''
    
    def set(self, message):
        self.message = message

    def pop(self):
        if self.message:
            print(self.message)
            self.message = ''


class Player():
    def __init__(self, name: str):    
        self.name = name
        self.score = []
    
    def add_score(self, number):
        self.score.append(number)
    
    def score_clear(self):
        self.score = []
    
    def getname(self):
        return self.name
    
    def getscore(self):
        return self.score
    
class ScoreWindow():
    def __init__(self, days_limit, money_limit, players: list):
        self.days_limit = days_limit
        self.money_limit = money_limit
        self.players = players
        self.scores = {}
        self.__update()
    
    def __update(self):
        for player in self.players:
            self.scores[player.getname()] = []
            
    def get_money_limit(self):
        return self.money_limit
    
    def update_player_score(self, player: Player):
        self.scores[player.getname()] = player.getscore()
    
    def show_statistic(self):
        print(f'{self.days_limit} дней подряд нужно зарабатывать {self.money_limit} монет.\n')
        for player, score in self.scores.items():
            days_to_win = self.days_limit - len(self.scores[player])
            print(f'{player} имеет {score} очков.')
            print(f'Ему осталось {days_to_win} дней до победы!\n')
        
    def check_winner(self):
        win_count = 0
        winner = ''
        
        for player, score in self.scores.items():
            if len(score) == self.days_limit:
                win_count += 1
                winner = player
        
        if win_count == len(self.players):
            print('Ничья!')
            win_count = 0
            return True
        
        if win_count == 1:
            print(f'Победил {winner}')
            win_count = 0
            return True
        
        return False
                
    def update_statistic(self, player_object: Player):
        for player, score in self.players.items():
            self.players[player] = (player_object.getscore())                
    
    def update_money_limit(self, money):
        self.money_limit = money

    
    def update_days_limit(self, days):
        self.days_limit = days

def create_player(names: list):
    players = []
    for name in names:
        players.append(Player(name))
    return players


def main():
    players = create_player(['Гоша', 'Артем'])
    statistic = ScoreWindow(days_limit=7, money_limit=200, players=players)
    
    while True:
        Error().pop()
        if statistic.check_winner():
            day_limit = int(input('Установи новый лимит дней: '))
            money_limit = int(input('Установи новый лимит монет: '))
            statistic.update_days_limit(day_limit)
            statistic.update_money_limit(money_limit)
        statistic.show_statistic()
        
        uname = input('Напиши имя игрока:')
        for player in players:
            if uname == player.getname():
                try:
                    scores = int(input(f'Напиши сколько дать очков для {player.getname()}: '))
                    if scores >= statistic.get_money_limit():
                        player.add_score(scores)
                    else:
                        player.score_clear()
                    statistic.update_player_score(player)
                except Exception:
                    Error().set('[ERROR] Введи пожалуйста число.')
                
        
        os.system('cls')
    
if __name__ == "__main__":
    main()