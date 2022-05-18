#Rock! Paper! Scissors! (Python)

from os import name as os_name, system as os_system
from random import choice as ran_choice

if os_name == "nt":
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("Rock! Paper! Scissors!")

def clearconsole():
    if os_name == "nt": os_system("cls")
    else: os_system("clear")

class Main():
    def __init__(self):
        self.score = 0
        self.highscore = 0
        self.won = False
        self.lost = False
        self.draw = False
        valid_list = [1, 2, 3]
        self.rps_list = ["Rock", "Paper", "Scissors"]

        while True:
            clearconsole()
            print(f"Score:{self.score}\nHighscore:{self.highscore}\n\n[1]Rock\n[2]Paper\n[3]Scissors\n\n'Ctrl + C' to exit.\n")   
            self.player_input = int(input(">"))
            while self.player_input not in valid_list:
                clearconsole() 
                print(f"Score:{self.score}\nHighscore:{self.highscore}\n\n[1]Rock\n[2]Paper\n[3]Scissors\n\n'Ctrl + C' to exit.\n")   
                self.player_input = int(input(">"))
                
            self.computer_input = ran_choice(valid_list)
                    
            self.handlechoices()
            self.setresults()
            self.handlescores()
                
            clearconsole()
            print(f"You: {self.player_display}\nComputer: {self.computer_display}\nResults: {self.results}\nScore: {self.score}\nHighScore: {self.highscore}\n")
            print("Do you want to exit? Type 'yes' or 'y' to exit, Press Enter to continue.")

            console = input(">")

            if console in ["yes", "y"]:
                clearconsole()
                break
                
    def handlechoices(self):
        choice_made = self.player_input-1

        if self.player_input:
            self.player_display = self.rps_list[choice_made]

        if self.computer_input:
            self.computer_display = self.rps_list[choice_made]
            
        #Rock
        if self.player_input == 1:
            if self.computer_input == 1:
                self.draw = True
            elif self.computer_input == 2:
                self.lost = True
            elif self.computer_input == 3:
                self.won = True
                
        #Paper
        elif self.player_input == 2:
            if self.computer_input == 1:
                self.won = True
            elif self.computer_input == 2:
                self.draw = True
            elif self.computer_input == 3:
                self.lost = True
                
        #Scissors
        elif self.player_input == 3:
            if self.computer_input == 1:
                self.lost = True
            elif self.computer_input == 2:
                self.won = True
            elif self.computer_input == 3:
                self.draw = True           
               
    def setresults(self):
        results_list = ["You Won", "You Lost", "Draw"]
        
        if self.won:
            self.results = results_list[0]
        elif self.lost:
            self.results = results_list[1]
        elif self.draw:
            self.results = results_list[2]
        

    def handlescores(self):
        #Add to Score
        if self.won:
            self.score += 1
            self.won = False

        #HighScore
        elif self.lost:
            if self.score > self.highscore:
                self.highscore = self.score
                self.score = 0
            self.lost = False

        #etc
        elif self.draw:
            self.draw = False

if __name__ == "__main__":
    try:
        Main()
    except KeyboardInterrupt:
        clearconsole()