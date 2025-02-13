from scoring import *

score = ScoringSystem()

#initiate test file
file_path = "scoring/test.txt"
new_scores = [500, 700, 500, 6, 6, 5, 4, 3, 2, 1]
print(type(new_scores))
with open(file_path, "w") as file:
    json.dump(new_scores, file)


#score.write_high_score(500)


score.write_high_score(5000)
