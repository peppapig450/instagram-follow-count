# Instagram Followers Scripts

A collection of python scripts that involve monitoring a user or multiple users followers on Instagram.

This means that you have to have a working tor proxy.

You can install tor on macOS with [brew](https://brew.sh)  
Assuming you have brew already setup you can do:
```shell
brew install tor
brew services start tor
```
to install and start the tor proxy

## Setup

#### Installing needed modules
I would recommend using virtualenv to install the modules locally like this:
```shell
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Login Credentials
Put your login info for Instagram into the `.env` file using this format
> login_name="*your username*"  
> psswd="*your password*"
