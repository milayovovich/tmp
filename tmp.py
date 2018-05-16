import requests

# r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
# print(r.json()['bpi']['USD']['rate'])

class MarketPlace:

    def __init__(self, name, zero_day):
        self.name = name
        self.zero_day = zero_day

    def count_of_day(self):
        import datetime
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        delta =self.zero_day - now
        return delta.days