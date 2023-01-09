#EasyService
# MarketPlace Project


## --Description

Welcome to EasyService.

It is a website for finding workers for your problems
# Installation

## First you need to download files to your computer

```
git clone https://github.com/ruhinshukurlu/marketPlace.git
```

## Install and activate Vitual Environment

```
sudo apt install python3-pip
```
```
sudo apt install python3-venv
```
```
python3.7 -m venv my_env
```
```
source my_env/bin/activate
```

## Install dependencies 

```
pip install -r requirements.txt

```

## Run docker

After successfuly installed dependecies you need to Build docker bellow command:

```
cd marketPlace/_development/
```
```
docker-compose up -d
```
```
cd ../
```

## Superuser

Create superusers using the createsuperuser command and you need to include email and password for superuser:

```
python manage.py createsuperuser
```

## Run server

```
./manage.py runserver
```

Now you can run server and include EasyService using this url address http://127.0.0.1:8000/

