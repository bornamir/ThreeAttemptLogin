
# Three Attempt Login

This project is created for a job interview. The project description is:

> Create an authentication system where if a user fails to enter password 3 times, it bans the user login attempts for 1 hour .
>
> Also same rule applies if the user wants to recover account with SMS verification.

Backend is developed with django and python. Django default authentication system is used for controlling the login and signup process. 

Limiting login attempts is done with the help of [django-axes](https://pypi.org/project/django-axes/) app. The combination of username and IP address is used for defining a user attempt. 

Since this is not a real world applicable project, the default database - sqlite3 - is used and the project is deployed in [http://bornamir.pythonanywhere.com](http://bornamir.pythonanywhere.com) . 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development.

### Prerequisites

There should be python 3.7 installed on the machine.

### Installing

clone the project

```shell
git clone https://github.com/bornamir/ThreeAttemptLogin.git
```

create and start a a virtual environment

```shell
projects/ThreeAttemptsLogin $ virtualenv venv
projects/ThreeAttemptsLogin $ source venv/bin/activate
```

Install the project dependencies:

```shell
pip install -r requirements.txt
```

then run

```shell
python manage.py migrate
```

to start the development server

```py
python manage.py runserver
```

and open localhost:8000 on your browser to view the app.

## Built With

* [Django 2.2](https://www.djangoproject.com/) - The web framework 
* [django-axes](https://pypi.org/project/django-axes/) - Limiting login attempts
* [Python 3.7](https://www.python.org/downloads/release/python-370/) 

## Authors

* **Borna Mir Arabshahi**  - [github](https://github.com/bornamir)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
