from requests import get

#get("https://www.google.com")
#print(get("https://www.google.com"))

#get("http://api.weatherstack.com/current?access_key=4390ee3a0185dec3b780c2059c16bb11&query=New%20York")
#print(get("http://api.weatherstack.com/current?access_key=4390ee3a0185dec3b780c2059c16bb11&query=New%20York"))

def main():
    baseURL = "http://api.weatherstack.com/current"
    access_key = "4390ee3a0185dec3b780c2059c16bb11"
    city = "Montreal"
    response = get(baseURL+"?access_key="+access_key+"&query="+city)
    print(response.json()['current']["temperature"])

if __name__ == '__main__':
    main()