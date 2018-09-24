import random
def drawing_without_replacement_sim(numTrials):
    c = 0
    for i in range(numTrials):
        bucket = ['R', 'R', 'R', 'R', 'G', 'G', 'G', 'G']
        pick = []
        for j in range(3):
            k = random.choice(bucket)
            pick.append(k)
            bucket.remove(k)
        if pick[0] == pick[1] == pick[2]:
            c += 1
    return c/numTrials   
