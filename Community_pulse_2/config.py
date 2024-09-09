class Config:
    DEBUG = False
    TESTING = False
    #SQLALCHEMY_DATABASE_URI = ('sqlite:///:memory:example')
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:parhat1994@localhost:3306/Community_pulse'
    SQLALCHEMY_DATABASE_URI = "sqlite:///C:/Users/Parkhat Bazakov/PycharmProjects/Community_pulse_2/your_database_name.db"

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    DEBUG = True
    TESTING = True