from requests import get
import sys

def main():
    baseURL = "http://api.weatherstack.com/current"
    access_key = "4390ee3a0185dec3b780c2059c16bb11"
    cities = sys.argv[1].split(",")
    if len(sys.argv) < 3:
        print("Please enter a city (or list of cities, separated by [,] with no space) with -f or -c as the last arg")
    else:
        for city in cities:
            scale = sys.argv[2][1:2]
            weather = get(baseURL + "?access_key=" + access_key + "&query=" + city)
            if 'request' not in weather.json():
                print("The city",city, "does not exist. A partial list of cities to choose from: Tokyo,London,Montreal...")
            else:
                degreeC = (weather.json()["current"]["temperature"])
                degreeF = 9.0 / 5.0 * degreeC + 32
                if scale == "c":
                    degree = "Celsius"
                    print("The weather in", city, "today is", degreeC, degree)
                if scale == "f":
                    degree = "Fahrenheit"
                    print("The weather in", city, "today is", degreeF, degree)

if __name__ == '__main__':
    main()
