# Oura Ring Data Puller

This app is used to pull my oura ring data using the [Oura ring API](https://python-ouraring.readthedocs.io/en/latest/api.html)

**_Disclaimer: This project is currently a work in proggress_**

## Description

This application uses a virtual environment for python packages.

## Setup

### Virtual Enviroment Setup

1. Open the project directory in cmd and then run the following:

```CMD
py -m venv .venv
.venv\Scripts\activate
.venv\Scripts\python.exe  -m pip install --upgrade pip
py -m pip install -r requirements.txt
```

### Config.ini Setup

Create a config.ini file in the src folder and copy the following into the file.

```Python
[config]
client_id =
access_token =
```

1. Add your client ID found in the "My Applications" page on your Oura ring website.

2. Add your Access Token found in the "Personal Access Tokens" page on your Oura ring website.

## Resources

[Oura ring API](https://python-ouraring.readthedocs.io/en/latest/api.html)

[Oura ring Documentation](https://cloud.ouraring.com/docs/)
