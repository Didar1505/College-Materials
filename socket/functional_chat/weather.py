from pyowm import OWM

class Weather:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return 
        
        self.owm = OWM('2f5f6064a2e7b417bb9d4ab541d12666')
        self.mgr = self.owm.weather_manager()

        self._initialized = True

    def get_weather(self, city):
        # Search for current weather in London (Great Britain) and get details
        observation = self.mgr.weather_at_place(city)
        w = observation.weather

        w.detailed_status         # 'clouds'
        w.wind()                  # {'speed': 4.6, 'deg': 330}
        w.humidity                # 87
        temp = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
        w.rain                    # {}
        w.heat_index              # None
        w.clouds                  # 75
        return temp['temp']