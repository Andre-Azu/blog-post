# template in charge of working withthe API
import requests
import json



def get_quote():
    reg=requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    data=json.loads(reg.content)
    return data
