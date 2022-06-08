from decouple import config

CHARACTERS_URL = config("CHARACTERS_URL", default="https://www.tibia.com/community/?name=%s")