import xlrd
import collections
from twitter import *
import os

class MovieRecommender():

    def __init__(self, path):
        self.book = xlrd.open_workbook(path)

    def getData(self):

        sheet = self.book.sheet_by_index(0)

        Movies = sheet.col_slice(start_rowx=0, end_rowx=8, colx=0)
        rating = sheet.col_slice(start_rowx=0, end_rowx=8, colx=2)

        dic = {}
        for x in xrange(8):
            dic[rating[x].value] = Movies[x].value


        return collections.OrderedDict(sorted(dic.items()))



    def getMovie(self, dic, twitter_name):

        tweats = twitter.getRecentTweets(twitter_name)
        flt = twitter.getSentiment(tweats)

        return dic.get(flt, dic[min(dic.keys(), key=lambda k: abs(k-flt))])



if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, "seating/delta_movies.xlsx")
    x = MovieRecommender(path)
    x.getMovie(x.getData(), "justinkrish2")
    x.getData()
