from constants import *
class ScoringSystem():
    running_score_destroy_asteroid = 0

    def __init__(self):
        self
        

    def score_destroy_asteroid(self, asteroid_radius):
        if asteroid_radius == 60:
            self.running_score_destroy_asteroid += 30
            print("30")
        elif asteroid_radius == 40:
            self.running_score_destroy_asteroid += 70
            print("70")
        elif asteroid_radius == 20:
            self.running_score_destroy_asteroid += 100
            print("100")
        #print(self.running_score_destroy_asteroid)