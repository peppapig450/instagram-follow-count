#!/usr/bin/env python

import argparse
import datetime
import os
import smtplib, ssl
import subprocess
import time
import logging

import instaloader
from dotenv import load_dotenv

# Create the argument parser
parser = argparse.ArgumentParser(
    description="Monitor how many followers multiple users gain in an amount of time."
)

# Parse users to monitor
parser.add_argument(
    "-u",
    "--users",
    nargs="*",
    type=str,
    default=[],
    metavar="username",
    help="usernames you want to monitor the followers of",
)

# Parse the time interval
parser.add_argument(
    "-t",
    "--time",
    type=int,
    default=10,
    metavar="minutes",
    help="time interval to check followers at",
)

# Create logger
logging.basicConfig(
    filename="log.txt",
    filemode="a",
    format="%(asctime)s | %(message)s",
    datefmt="%y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

# Get relative path of .env file
env_path = os.path.join(os.getcwd(), ".env")
# load .env into environment
load_dotenv(env_path)

# Setup email to send when botting is detected
port = 465  # for ssl
smtp_server = "smtp.gmail.com"
sender_email = os.getenv("sender_email")
receiver_email = os.getenv("receiver_email")
password = os.getenv("email_pass")

# Create a secure SSL context
context = ssl.create_default_context

# Parse the arguments
args = parser.parse_args()

# Parse list of usernames to monitor
users = args.users

# Set time_interval to the time interval argument converted to seconds
time_interval = args.time * 60

# Get Instaloader instance
loader = instaloader.Instaloader()

# Get login info from .env file
login_name = os.getenv("login_name")
passwd = os.getenv("psswd")

# Set tor proxy info
proxies = {"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}

# Login into the session
loader.login(login_name, passwd, proxies)


# Function to check users followers
# def check_followers():
#    for user in users:
#        # Get users profile
#        user_profile = instaloader.Profile.from_username(loader.context, user)
#        # Get the amount of followers the user has
#        user_followers = user_profile.followers
#
#        # Log users follower amount to file
#        logging.info(f"{user} has {user_followers} followers")
#
#        return user_followers, user


def parse_log_python():
    file = open("log.txt", "r")
    lines = file.readlines()
    result = []
    for x in lines:
        result.append(x.split(" ")[5])
    file.close()
    print(result)


def parse_log_awk():
    cmd = r"""awk '{print $6}' log.txt"""
    follow_count = subprocess.check_output(cmd, shell=True).decode("utf-8")
    print(follow_count)


def main():
    while True:
        for user in users:
            # Get users profile
            user_profile = instaloader.Profile.from_username(loader.context, user)
            # Get the amount of followers the user has
            user_followers = user_profile.followers

            # Log users follower amount to file
            logging.info(f"{user} has {user_followers} followers")

            time.sleep(time_interval)
            # Get the follower amount again
            old_followers = user_followers
            user_profile = instaloader.Profile.from_username(loader.context, user)
            user_followers = user_profile.followers

            logging.info(f"{user} has {user_followers} followers")

            # find the gained follower amount
            gained = user_followers - old_followers

            # set threshold to 5 followers per minute
            threshold = args.time * 5

            # if gained is past threshold send email
            if gained >= threshold:
                message = """\
                Subject: Botting Detected!!!


                {user} is botting."""
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls(context=context)
                    server.ehlo()
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, message)

                exit()


if __name__ == "__main__":
    main()
