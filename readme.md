# Fabelio Price Tracker

This is a web page to put product url from [fabelio](https://fabelio.com/) and watch the price every hours.

## Spesification

Written in Django 3.0 with postgresql.

## Installation

* create your own virtualenv, [documentation](https://virtualenv.pypa.io/en/stable/installation.html)
* activate your virtualenv

   depends on your OS, activating virtualenv could be different

   on windows
   ```shell script
      $ .venv/Scripts/activate.bat
    ```

   on linux
   ```shell script
      $ source .venv/bin/activate
    ```
* install requirements to your virtualenv

    ```shell script
      $ pip install -r requirements.txt
    ```

* migrate database

    ```shell script
      $ invoke migrate // used pyinvoke command
    ```

* running in local

    ```shell script
      $ python fabelio_price_tracker/manage.py runserver
    ```
