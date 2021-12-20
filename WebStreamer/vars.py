# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    API_ID = 3796974
    API_HASH = '9511d0112631f9990337eb724d1a7d0d'
    BOT_TOKEN = '5005485389:AAEHIWantBXQ5LOg9yHgz68KnkbiCu4mrYk'
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = -1001771465683     
    PORT = int(getenv('PORT', 8080))
    BIND_ADDRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '1200')) # 20 minutes
    HAS_SSL = getenv('HAS_SSL', False)
    HAS_SSL = True if str(HAS_SSL).lower() == 'true' else False
    NO_PORT = getenv('NO_PORT', False)
    NO_PORT = True if str(NO_PORT).lower() == 'true' else False
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = 'mjfiletolinkbot'
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADDRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME + '.herokuapp.com'
    if ON_HEROKU:
        URL = f"https://{FQDN}/"     
    else:
        URL = "http{}://{}{}/".format('s' if HAS_SSL else '', FQDN, '' if NO_PORT else ':'+ str(PORT))
