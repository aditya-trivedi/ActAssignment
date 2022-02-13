import json
 
# Opening JSON file
f = open('input_ios.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Closing file
f.close()


#The basic idea is to store the total sales of each product country-wise
dictionary = {}
for i in data['sales']:
    if i['prod'] not in dictionary:
        dictionary[i['prod']] = {}
        dictionary[i['prod']][i['country']] = i['price']
    else:
        if i['country'] not in dictionary[i['prod']]:
            dictionary[i['prod']][i['country']] = i['price']
        else:
            dictionary[i['prod']][i['country']] += i['price']


prod = input('Enter the Product : ')
prod = prod.upper()

ma = -1;
countryAns = ''
if prod not in dictionary:
    print('Product does not exist')
else:
    for country in dictionary[prod]:
        if dictionary[prod][country] > ma:
            ma = dictionary[prod][country] 
            countryAns = country
    print("Country with max sales : " + countryAns)


