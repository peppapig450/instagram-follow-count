import instaloader
from dotenv import load_dotenv
import os
import sys

# Get instance
loader = instaloader.Instaloader()

# get relative path of .env file
env_path = os.path.join(os.getcwd(), '.env')

# get user to get follow count of
target = ' '.join(sys.argv[1:])

# load secrets from file
load_dotenv(env_path)

# load login info from secret file
login_name = os.getenv('login_name')
psswd = os.getenv('psswd')

# Set tor proxy
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

# Login or load session
loader.login(login_name, psswd, proxies)

# Obtain profile metadata
profile = instaloader.Profile.from_username(loader.context, target)

# print out follower count
print(profile.followers)
