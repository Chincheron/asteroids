import json
from constants import *

class ScoringSystem():
    running_score_destroy_asteroid = 0

    def __init__(self):
        self
        

    def score_destroy_asteroid(self, asteroid_radius):
        if asteroid_radius == 60:
            self.running_score_destroy_asteroid += 30
        elif asteroid_radius == 40:
            self.running_score_destroy_asteroid += 70
        elif asteroid_radius == 20:
            self.running_score_destroy_asteroid += 100
        #print(self.running_score_destroy_asteroid)

    def write_high_score(self, high_score):

        #file for storing high scores
        file_path = "scoring/test.txt"

        #create high score file if it doesn't exist
        try:
            with open(file_path, "x") as file:
            #    content = file.read()
                print(f"File '{file_path}' created succesfully")
        except FileExistsError:
            print(f"File '{file_path}' already exists") 

        #pull current high scores from file
        with open(file_path, "r") as file:
            current_scores = json.load(file)
        
        #Decide whether score is new high score
        min_score = min(current_scores)
        current_scores.sort(reverse=True)
        new_scores = current_scores.copy()
        if high_score <= min_score and len(current_scores) >= 10:
            pass
        else:
            if len(current_scores) >= 10:
                new_scores.pop()
                new_scores.append(high_score)
            else:
                new_scores.append(high_score)
        new_scores.sort(reverse=True)


        #write new list keep 10 highest scores)
        with open(file_path, "w") as file:
            json.dump(new_scores, file)

        return f"write high score: {high_score}"
    
    def display_high_score(self):
        #intended to display high score at game over in console 
        print("display high score")