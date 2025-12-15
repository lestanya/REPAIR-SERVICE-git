from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())
SECRET_KEY = os.getenv('SECRET_KEY')