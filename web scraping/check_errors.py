import requests

res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc)) #There was a problem: 404 Client
    # Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist

