#!/usr/bin/env python

import argparse
import os

import instaloader
from dotenv import load_dotenv

# Create parser
parser = argparse.ArgumentParser(
    description="Get the exact number of followers a user has."
)

parser.add_argument(
    "username", type=str, help="username you want to check followers of"
)

# Parse the arguements
args = parser.parse_args()

# set target username to parsed argument
target = args.username

# Get insance
loader = instaloader.Instaloader()

# get relative path of .env file
env_path = os.path.join(os.getcwd(), ".env")

# load secrets from file
load_dotenv(env_path)

# get login info from secret file
login_name = os.getenv("login_name")
psswd = os.getenv("psswd")

# Set tor proxy
proxies = {"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}

# Login or load session
loader.login(login_name, psswd, proxies)

# Get the users profile
profile = instaloader.Profile.from_username(loader.context, target)

# get followers
followers = profile.followers

print(f"The user {target} has {followers} followers.")
