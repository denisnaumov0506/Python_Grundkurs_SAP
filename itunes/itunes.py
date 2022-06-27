import requests

search_term = input("Please enter a search term: ")

url = 'https://itunes.apple.com/search?term=' + search_term + '&entity=album'
request = dict(requests.get(url).json())

print(f"The search returned {request['resultCount']} results.")
for result in request['results']:
    print(f"Artist: {result['artistName']} - Album: {result['collectionName']} - Track Count: {result['trackCount']}")


