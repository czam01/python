import requests
# field to search
# https://www.zoho.com/crm/help/api/v2/#ra-search-records
"""
Only one of the above four parameters would work at one point of time.
Furthermore, if two parameters are given simultaneously, preference will be given in the order criteria,
email, phone and word, and only one of them would work.
"""


url = "https://www.zohoapis.com/crm/v2/Contacts/search"

querystring = {"email":"mail@gmail.com"}

headers = {
    'Authorization': "Authorization code here",
    'Cache-Control': "no-cache",
    'Postman-Token': "Postman token here"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
