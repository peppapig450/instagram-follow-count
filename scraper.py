# Get instance
import instaloader
from dotenv import load_dotenv
import os

loader = instaloader.Instaloader()

# get .env file
cwd = os.getcwd()
env_path = os.path.join(cwd, '.env')

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
profile = instaloader.Profile.from_username(loader.context, "nordv2")

# print out follower count
print(profile.followers)