import requests


def opt_api(token, search):
    url = 'https://rest-api-pr.allbestbets.com/api/v1/arbs/bot_search'
    data = {'per_page': '30', 'search_filter': search, 'sort_by': 'percent',
            'access_token': token}

    x = requests.post(url, data=data)
    return x
