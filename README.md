# Little URL REST API

Rest API for shortening URL
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/jurkowski-emil/little_url.git
$ cd little_url
```

Create a virtual environment to install dependencies:

```sh
$ python -m venv venv
```

On Windows, to activate run:

```sh
$ venv\Scripts\activate.bat
```

On Unix or MacOS, to activate run:

```sh
$ source venv/bin/activate
```

Then install the dependencies:

```sh
(venv)$ pip install -r requirements.txt
```
Note the `(venv)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:

```sh
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate
```

To start server on http://127.0.0.1:8000/ run:

```sh
(venv)$ python manage.py runserver
```


## Usage example with 'curl'

To generate or get previously generated short url

```sh
$ curl -i -X POST -H 'Content-Type: application/json' -d '{"url": "<url to shorten>"}' http://127.0.0.1:8000/little_url_api/short/

{"url":"http://localhost:8000/<random 6 character generated string>"}

```

To retrieve generated short url

```sh
$ curl -i -X POST -H 'Content-Type: application/json' -d '{"url": "http://localhost:8000/<random 6 character generated string>"}' http://127.0.0.1:8000/little_url_api/long/

{"url":"<long url or null if doesn't exist>"}

```



