import socket
import os
from dotenv import load_dotenv

load_dotenv()

# KEYS
OPENAI_API_KEY = os.environ.get("OPENAI_ACCESS_KEY")
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

# PORT INFORMATION
PORT = 8010
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)

# WORD SPECIFIC GLOBALS
AVOIDED_WORDS = [
    "MBC",
    "뉴스",
    "이덕영입니다."
    "지금까지",
    "신선한",
    "경제였습니다."
]
