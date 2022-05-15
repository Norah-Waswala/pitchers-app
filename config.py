import os
# from dotenv import load_dotenv
# load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://norah:12345we@localhost/pitches'
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SECRET_KEY=os.environ.get('SECRET_KEY')
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://gpcqvpewhjteaz:a77f52443aceea65a52b3efac95875e8dece983bdd9565ab64b7df15ba7bc50a@ec2-52-86-56-90.compute-1.amazonaws.com:5432/d3p6iphvpopfl2"
       
class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}