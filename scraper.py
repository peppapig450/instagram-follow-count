#!/usr/bin/env python

import os
import time
import argparse

import instaloader
from dotenv import load_dotenv

# Create the parser
parser = argparse.ArgumentParser(
    description="Determine how many Instagram followers a user gains in an amount of time."
)

# Add the arguments
parser.add_argument(
    "-t",
    "--time",
    type=float,
    default=1,
    metavar="minute(s)",
    help="amount of time in which to see how many followers the user gains",
)
parser.add_argument(
    "username", type=str, help="username you want to check followers of"
)

# Parse the arguements
args = parser.parse_args()

# set target username to parsed argument
target = args.username

# set time_interval to the time argument converted to seconds
time_interval = args.time * 60

# Get instance
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

# Get initial profile metadata
initial_profile = instaloader.Profile.from_username(loader.context, target)

# get the initial amount of followers the user has
initial_followers = initial_profile.followers

# wait the specified amount of time
time.sleep(time_interval)

# Get profile metadata again
new_profile = instaloader.Profile.from_username(loader.context, target)

# get the amount of followers the user has after the set amount of time
new_followers = new_profile.followers

# get the amount of followers gained in the set amount of time
followers_gained = new_followers - initial_followers

# print out how many followers the user gained
print(
    f"The user {target} gained {followers_gained} followers in {args.time} minutes."
)
