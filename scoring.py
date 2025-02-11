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
        #create file if not exist
        #store as number (keep 10 highest scores)
        #need to 1) read current scores (figure out how to store scores in text and then read. can you store a lsit in text?)
        #           2) check if new score is higher than any of old scores
        #               3) if yes, delete lowest old score and add new score
        # other considerations: Keep values sorted in text file
        #                       
        print(f"write high score: {high_score}")
    
    def display_high_score(self):
        #intended to display high score at game over in console 
        print("display high score")