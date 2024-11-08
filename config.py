##OPEN API STUFF
OPENAI_API_KEY = 'sk-seCCW9VAGdTGGOM8qvrfyO1_OR8lwjw4FibHpVkfIsT3BlbkFJOMpN1k714vWBH7EYI2LrSr3ZDHeAI-STo1QH5dO9sA'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
