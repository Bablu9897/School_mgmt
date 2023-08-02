
import requests
import json

def getNumDraws(year):
    url1 = "https://jsonmock.hackerrank.com/api/football_matches?year=" + str(year)
    response1 = requests.get(url1)
    print(response1.content)
    result1 = json.loads(response1.content)
    # print(result1)
    
    curr_1 = 1
    total_page_url_1 = result1['total_pages']
    total = 0
    for i in range(0,12):
        url1 = "https://jsonmock.hackerrank.com/api/football_matches?year={0}&team1goals={1}&team2goals={1}".format(year,i,i)
        response1 = requests.get(url1)
        result1 = json.loads(response1.content)
        # print(result1['total'])
        total += result1['total']
    # return total
if __name__ == '__main__':
    (getNumDraws(2011))