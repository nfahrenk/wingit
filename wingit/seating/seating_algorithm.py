import math

# peopleOnFlight = {
# 	"nick": [("band1", "001", 1000)], # 0 match with 2
# 	"kyle": [("band2", "002", 100000)], # 1 match with 2, 3, 6
# 	"justin": [("band1", "001", 1000), ("band2", "002", 100000)], # 2 match with 0, 1, 3, 6
# 	"pear": [("band2", "002", 100000), ("band3", "003", 100), ("band6", "006", 1000000000)], # 3 match with 1, 2, 4, 6
# 	"gerard": [("band3", "003", 100), ("band6", "006", 1000000000)], # 4 match with 3
# 	"krippa": [("band4", "004", 10)], # 5 match with []
# 	"sahil": [("band2", "002", 100000)], # 6 match with 1, 2, 3
# 	"grant": [("band7", "007", 103)], # 5 match with []
# }

# [("nick", "kyle", "band2"), ("justin", None, None)]

def findMatches(peopleOnFlight):
	#Create matchMatrix of zeros for comparing people on flight
	matchMatrix = []
	for x in range(0, len(peopleOnFlight)):
		subList = []
		for x in range(0, len(peopleOnFlight)):
			subList.append(0)
		matchMatrix.append(subList)



	for person in peopleOnFlight:
		personInd = peopleOnFlight.keys().index(person)
		for interest, interestID, likes in peopleOnFlight[person]:
			for potentialMatch in peopleOnFlight:
				matchInd = peopleOnFlight.keys().index(potentialMatch)
				if personInd != matchInd:
					for interest2, interestID2, likes2 in peopleOnFlight[potentialMatch]:
						if (interestID == interestID2):
							matchVal = 1/(math.log(likes))
							matchMatrix[personInd][matchInd] += matchVal


	priorityVals = []
	for y in range (0, len(peopleOnFlight)):
		for x in range (y + 1, len(peopleOnFlight)):
			if matchMatrix[y][x] != 0:
				priorityVals.append(matchMatrix[y][x])

	priorityVals = sorted(priorityVals);

	#Create matchList
	remainingPeople = peopleOnFlight.copy()
	matchMadeIndexes = []
	# matchList = []
	finalMatches = []
	for matchVal in reversed(priorityVals):
		# Search list for matchVal and match the two people
		for y in range (0, len(matchMatrix)):
			if y not in matchMadeIndexes:
				for x in range (y + 1, len(matchMatrix[0])):
					if x not in matchMadeIndexes and y not in matchMadeIndexes:
						if matchMatrix[y][x] == matchVal:
							person1 = peopleOnFlight.keys()[y]
							person2 = peopleOnFlight.keys()[x]
							# newLine = person1 + " sitting with " + person2
							# matchList.append(newLine)
							# pdb.set_trace()
							remainingPeople.pop(person1)
							remainingPeople.pop(person2)
							matchMadeIndexes.append(y)
							matchMadeIndexes.append(x)

							bestInterest = ""
							bestVal = 0
							for interest, interestID, likes in peopleOnFlight[person1]:
								for interest2, interestID2, likes2 in peopleOnFlight[person2]:
									if interestID == interestID2:
										interestVal = 1/(math.log(likes))
										if interestVal > bestVal:
											bestVal = interestVal
											bestInterest = interest
							
							matchBio = (person1, person2, bestInterest)
							finalMatches.append(matchBio)

	
	while len(remainingPeople) >= 2:
		person1 = remainingPeople.keys()[0]
		person2 = remainingPeople.keys()[1]
		matchBio = (person1, person2, None)
		remainingPeople.pop(person1)
		remainingPeople.pop(person2)
		finalMatches.append(matchBio)
	if len(remainingPeople) == 1:
		finalMatches.append((remainingPeople.keys()[0], None, None))

	return finalMatches