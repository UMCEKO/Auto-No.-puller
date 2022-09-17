import requests

token = ''
country = 'usa'
operator = 'any'
product = 'telegram'

headers = {
    'Authorization': 'Bearer ' + token,
    'Accept': 'application/json',
}

response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product + '?forwarding=$forwarding&number=$number&reuse=$reuse&voice=$voice&ref=$ref', headers=headers)
print(response)