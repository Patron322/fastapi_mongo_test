import os
from os.path import dirname, join

from dotenv import load_dotenv

load_dotenv()
dotenv_path = join(dirname(__file__), '.env')


class Settings:
    def __init__(self):
        self.MONGO_HOST: str = self.get_argument('MONGO_HOST')
        self.MONGO_PORT: str = self.get_argument('MONGO_PORT')

    def get_argument(self, arg):
        argument = os.environ.get(arg)
        if not argument:
            raise ValueError(f'Argument: {arg} not defined in Settigs')
        if argument.isdigit():
            argument = int(argument)
        return argument

SETTINGS = Settings()
