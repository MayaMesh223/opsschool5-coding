from requests import get
import sys
import click

@click.command()

@click.option("--token", prompt=True)
@click.option("--city", prompt=True)
@click.option("--T", 'degree')
def main(token, city, degree):
    baseURL = "http://api.weatherstack.com/current?"
    cities = city.split(",")
    for current_city in cities:
        weather_response = get(baseURL + "access_key={}&query={}".format(token, current_city))
        weather = weather_response.json()
        if "error" in weather:
            if "invalid_access_key" in weather["error"]["type"]:
                print("Token is incorrect. Please enter a valid token.")
            elif "request_failed" in weather["error"]["type"]:
                    print("The city", current_city, "does not exist. A partial list of cities to choose from: Tokyo,London,Montreal...")
        else:
            degreeC = weather["current"]["temperature"]
            degreeF = 9.0 / 5.0 * degreeC + 32
            if degree.lower() == "celsius":
                print("The weather in", current_city, "today is", degreeC, degree)
            if degree.lower() == "fahrenheit":
                print("The weather in", current_city, "today is", degreeF, degree)

if __name__ == '__main__':
    main()
