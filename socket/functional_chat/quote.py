import requests

class Quote:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        
        self.api_url = 'https://quoteapi.pythonanywhere.com/random'
        self._initialized = True
        
    def get_random_quote(self):
        response = requests.get(self.api_url)
        data = response.json()
        return data['Quotes'][0]
