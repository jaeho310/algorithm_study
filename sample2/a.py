import json
import urllib.request

def do_get(url):
    try:
        response = urllib.request.urlopen(url)
        res = response.read().decode('utf-8')
        data = json.loads(res)
        return data
    except Exception as e:
        return None
def bestUniversityByCountry(country):
    rank_university = [100000, '']
    page = 1
    while True:
        url = 'https://jsonmock.hackerrank.com/api/universities?page=' + str(page)
        res = do_get(url)
        for item in res['data']:
            # print(item['location'])
            if item['location']['country'] == country:
                if not item['rank_display']:
                    continue
                rank = int(item['rank_display'])
                if rank_university[0] > rank:
                    rank_university = [rank, item['university']]
        page += 1
        if int(res['total_pages']) > page:
            break
    return rank_university[1]
if __name__ == '__main__':
    print(bestUniversityByCountry('United Kingdom'))