<!-- GETTING STARTED -->

## Getting Started

Create app demo for implement features same Django Suit with Django Admin Interface.

### Prerequisites

- [Django project with Pyenv](https://mrdjangoblog.wordpress.com/2016/09/23/how-to-start-django-project-with-pyenv/)
- Django: 3.2

### Installation

_How to setup and run app._

1. Clone the repo

```sh
 git clone git@github.com:hungle-agilityio/django-admin-demo.git
 cd django-admin-demo
```

2. Install requirements

```sh
 pip install --upgrade -r requirements.txt
```

3. Run migrations

```sh
python manage.py migrate
```

4. Create a super user

```sh
python manage.py createsuperuser
```


5. Start the development server

```sh
python manage.py runserver 8080
```
