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
    SQLALCHEMY_DATABASE_URI = "postgresql://hyenxhrfgrqwyg:2c18d6ec2b484eaf209df68c6869fba74a02d054c1ac171d945c087285b966e3@ec2-44-195-169-163.compute-1.amazonaws.com:5433/dafsk8fdljk1nl"
       
class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}