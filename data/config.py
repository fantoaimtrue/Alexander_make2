import os

from dotenv import load_dotenv
from pyngrok import ngrok

load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

admins = [
    571104053, 176280312
]

ip = os.getenv('IP')
PGUSER = str(os.getenv('PGUSER'))
PGPASSWORD = str(os.getenv('PGPASSWORD'))
DATABASE = str(os.getenv('DATABASE'))

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'

# подключение к серверу NGROK
ngrok.set_auth_token(os.getenv('NGROK_TOKEN'))
http_tunnel = ngrok.connect(5000, bind_tls=True)

# webhook settings
WEBHOOK_HOST = http_tunnel.public_url
WEBHOOK_PATH = ''
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = 5000
