import re
import requests

class FacebookQuery():
    host_url = 'https://graph.facebook.com/v2.5/'
    facebook_id = '145634995501895'

    def getRequest(self, ext, params={}):
        params.update({
            'access_token': 'EAACEdEose0cBAKWnn2rkmhQasdFpfLBvvAAyoPKgIdXfz9exHwBvf7ZB26yGrwFfsOQkQZBGZC5TN1ZAqHRD1y4TRKiCUYKIeqZCbOQUZCrD77IQPQ2deZAh9FlYhwiqqDhGRwSdvJZAteKyTFwpAhlo1ZAqM2mw99i0fyNOMuFlceQZDZD',
            'method': 'get',
            'format': 'json',
            'pretty': 0,
            'suppress_http_code': 1,
        })
        response = requests.get(self.host_url+ext, params=params)
        return response.json()

    def getFacebookId(self):
        return self.getRequest('me')['id']

    def getUserLikesOfKind(self, kind):
        response = self.getRequest("me/%s/" % kind)
        return response

    def getAllRelevantUserLikes(self):
        possibilities = [
            'books',
            'likes',
            'games',
            'movies',
            'music',
            'television',
        ]
        outcome = []
        for poss in possibilities:
            outcome += [x['id'] for x in self.getUserLikesOfKind(poss)['data']]
        return outcome

    def getPageLikes(self, pageId):
        fields = ["likes", "name"]
        return self.getRequest(pageId, {"fields": ",".join(fields)})

    def getPersonLocation(self):
        response = self.getRequest(self.facebook_id, {"fields": "hometown,location"})
        h = response["hometown"] if "hometown" in response else response.get("location")
        return [(h["id"], h["name"])]

    def getPersonEvents(self):
        fields = ["name", "start_time", "id"]
        response = self.getRequest("me/events/", {"fields": ",".join(fields)})
        return response["data"]

    def getPersonEducation(self):
        fields = ["school", "concentration", "year", "degree"]
        fieldstr = "education.fields(%s)" % ",".join(fields)
        response = self.getRequest(self.facebook_id, {"fields": fieldstr})
        pattern = re.compile(r'^(.+)?(?= Class) Class of ([0-9]{4})$')
        schoolDict = {}
        for school in response["education"]:
            year = -1
            schoolId = school['school']['id']
            name = school['school']['name']
            reresponse = pattern.match(name)
            if reresponse:
                name = reresponse.group(1)
                year = reresponse.group(2)
            if "year" in school:
                year = school['year']
            degree = school["degree"]["name"] \
                if "degree" in school \
                else ", ".join([x["name"] for x in school.get("concentration", [])])
            schoolDict[schoolId] = (name, year, degree)
        return schoolDict

    def getPersonLanguages(self):
        response = self.getRequest(self.facebook_id, {"fields": "languages"})
        h = response["languages"]
        return [(h["id"], h["name"])]

fq = FacebookQuery()
out = {
    like: fq.getPageLikes(like)["likes"]
    for like in fq.getAllRelevantUserLikes()
}
print out

