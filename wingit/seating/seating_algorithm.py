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

	linkedInFlyers = {}
	facebookFliers = {}

	#Start with linkedIn (much easier)
	for person in peopleOnFlight:
		if isinstance(peopleOnFlight[person], basestring):
			linkedInFlyers[person] =  peopleOnFlight[person]
		else:
			facebookFliers[person] = peopleOnFlight[person]

	finalMatches = []
	remainingLinkers = linkedInFlyers.copy()
	for person1 in linkedInFlyers:
		if person1 in remainingLinkers:
			for person2 in linkedInFlyers:
				if person1 != person2 and person2 in remainingLinkers and person1 in remainingLinkers:
					if linkedInFlyers[person1] == linkedInFlyers[person2]:
						matchBio = (person1, person2, linkedInFlyers[person1])
						remainingLinkers.pop(person1)
						remainingLinkers.pop(person2)
						finalMatches.append(matchBio)

	#LinkedIn Done, now faceook
	#Create matchMatrix of zeros for comparing people on flight
	matchMatrix = []
	for x in range(0, len(facebookFliers)):
		subList = []
		for x in range(0, len(facebookFliers)):
			subList.append(0)
		matchMatrix.append(subList)

	for person in facebookFliers:
		personInd = facebookFliers.keys().index(person)
		for interest, interestID, likes in facebookFliers[person]:
			for potentialMatch in facebookFliers:
				matchInd = facebookFliers.keys().index(potentialMatch)
				if personInd != matchInd:
					for interest2, interestID2, likes2 in facebookFliers[potentialMatch]:
						if (interestID == interestID2):
							matchVal = 1/(math.log(likes))
							matchMatrix[personInd][matchInd] += matchVal


	priorityVals = []
	for y in range (0, len(facebookFliers)):
		for x in range (y + 1, len(facebookFliers)):
			if matchMatrix[y][x] != 0:
				priorityVals.append(matchMatrix[y][x])

	priorityVals = sorted(priorityVals);

	#Create matchList
	remainingFacebookers = facebookFliers.copy()
	matchMadeIndexes = []
	# matchList = []
	for matchVal in reversed(priorityVals):
		# Search list for matchVal and match the two people
		for y in range (0, len(matchMatrix)):
			if y not in matchMadeIndexes:
				for x in range (y + 1, len(matchMatrix[0])):
					if x not in matchMadeIndexes and y not in matchMadeIndexes:
						if matchMatrix[y][x] == matchVal:
							person1 = facebookFliers.keys()[y]
							person2 = facebookFliers.keys()[x]
							# newLine = person1 + " sitting with " + person2
							# matchList.append(newLine)
							# pdb.set_trace()
							remainingFacebookers.pop(person1)
							remainingFacebookers.pop(person2)
							matchMadeIndexes.append(y)
							matchMadeIndexes.append(x)

							bestInterest = ""
							bestVal = 0
							for interest, interestID, likes in facebookFliers[person1]:
								for interest2, interestID2, likes2 in facebookFliers[person2]:
									if interestID == interestID2:
										interestVal = 1/(math.log(likes))
										if interestVal > bestVal:
											bestVal = interestVal
											bestInterest = interest
							
							matchBio = (person1, person2, bestInterest)
							finalMatches.append(matchBio)

	# Put all the lonely hearts in one pool so they can live their sad lives next to each other on the plane
	remainingPeople = {}
	for person in remainingFacebookers:
		remainingPeople[person] = remainingFacebookers[person]
	for person in remainingLinkers:
		remainingPeople[person] = remainingLinkers[person]

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