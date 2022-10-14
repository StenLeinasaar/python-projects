from weather import Weather




def get_forecast():
    weather = Weather(temperature_unit=None) # Celsius (or) Kelvin (or) Fahrenheit
    current_weather = weather.fetch_weather(city='Saratoga Springs', only_temp=False) # if only_temp is set To True It Will Only return The current temperature in given unit
    # Returns Dictionary with City name, Temperature, Humidity, Pressure, Description
    # [+] OUTPUT IF TEMPERATURE_UNIT IS NONE
    # {'City: ': 'Kadiri', 'Temperature In Kelvin: ': '304°K', 'Temperature In Celsius: ': '31°C', 'Temperature In Fahrenheit: ': '88°F', 'Pressure: ': 1008, 'Humidity: ': 42, 'Description: ': 'overcast clouds'}
    # [+] OUTPUT IF TEMPERATURE UNIT IS SET CELSIUS OR KELVIN OR FAHRENHEIT
    # {'City: ': 'Kadiri', 'Temperature: ': '{TEMPERATURE IN C OR K OR F}', 'Pressure: ': 1008, 'Humidity: ': 42, 'Description: ': 'overcast clouds'}
    # [+] OUTPUT IF ONLY_TEMP IS SET TO TRUE
    # 31°C
    return current_weather