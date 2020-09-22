import os

class Config:
    '''
    general configuration parent class
    '''
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?q={}&apiKey={}'
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: the parent configuratiion class with general settings
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}