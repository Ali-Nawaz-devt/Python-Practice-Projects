Students=[['Ali',33.0],['Khan',34.5],['Musa',34.5],['Anzy',35]]

Score_=[]
for Scores in Students:
    Score_.append(Scores[1])
    
Score_.sort()

for lowest in Students:
    if lowest[1]==Score_[1]:
        print('Name : '+ lowest[0]+ '  Score : ',lowest[1])
