import requests
import json
#User Input
taxon=input('Please enter taxon of interest: ')
print(taxon)
print('    ')

#Using Bold API
data=('http://www.boldsystems.org/index.php/API_Public/combined?taxon=',taxon,'&format=json')
y = str(''.join(data))

response = requests.get(y)
x = response.json()

#Output
with open('data.txt', 'w') as outfile:
    json.dump(x, outfile)

print('Progress: Completed')
