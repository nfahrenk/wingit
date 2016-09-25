# import requests
# import urllib

# go to "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=77pw4f5gqkyepp&redirect_uri=https://github.com/syntactix/wingit&scope=r_basicprofile"
# click
# getURL
# dictionary = {
# 	"grant_type": "authorization_code", 
# 	"code": "AQSKhf2jP3WTA25JEspU8rRbDPdCd_gbNW9NYYvYpjVO4CnnXH9Jp8DRNrejpTmRcWfmi0P3kYWvwV0frVO4le4P0rwf7vAMXaonejDA6M_w8PwAzc8", 
# 	"redirect_uri": 'https://github.com/syntactix/wingit?code=AQQFm87Y3FqFyGYAH-kX04G8KgdY8Sh7cMwMc6stgBICSosZdphOE1DZwft3u7U3uzyd8r5nb7USB594aLlcm_knwXTqIbqBUhypuMtltfxuG7qZvYQ', 
# 	"client_id": "77pw4f5gqkyepp", 
# 	"client_secret": "M3dHgNdwE1EJDmSK"}
# response = requests.post("https://www.linkedin.com/oauth/v2/accessToken", data = dictionary)

# print response.json()


import math
import pdb

def findMatches(peopleOnFlight):

	# Pass in dictionary {"Person": "Industry Name", "Person2": "Industry Name" }
	finalMatches = []
	remainingPeople = peopleOnFlight.copy()
	for person1 in peopleOnFlight:
		if person1 in remainingPeople:
			for person2 in peopleOnFlight:
				if person1 != person2 and person2 in remainingPeople and person1 in remainingPeople:
					if peopleOnFlight[person1] == peopleOnFlight[person2]:
						matchBio = (person1, person2, peopleOnFlight[person1])
						remainingPeople.pop(person1)
						remainingPeople.pop(person2)
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


peopleOnFlight = {"Nick": "Computer Science", "Justin": "Computer Science", "Kyle": "BME", "Gerard": "BME", "Sahil": "Dick Sucking", "Carina": "Corndog eating", "Sidney": "being a bitch about basil"}
print findMatches(peopleOnFlight)