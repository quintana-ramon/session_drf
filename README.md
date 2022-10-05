# session_drf

<div padding="10">
<image width="180" height="60" src="https://user-images.githubusercontent.com/111660643/193990187-35e3235b-0441-4fc2-887d-e45f71f85ab8.png"/>
<image width="180" height="60" src="https://user-images.githubusercontent.com/111660643/193990888-7a3dd3eb-b5b2-418e-9788-a25baf3841af.png" />
</div>


### Prerequisites

requirement | version
---|---
Python 3 | latest
Postgres | latest

- #### Create a database in your postgres called session_drf

<p> </p>

---

### How to use (Linux)

<p>clone this repository into your machine</p>

```shell
git clone https://github.com/quintana-ramon/session_drf/
```

<p>change to the repository folder</p>

```shell
cd session_drf/
```

<p>create a <strong>python virtual environment</strong></p>

```shell
python -m venv venv
```

<p>Use venv</p>

- ##### bash

```shell
source venv/bin/activate
```

- ##### fish

```shell
source venv/bin/activate.fish
```

<p>install requirements from <strong>requirements.txt</strong></p>

```shell
pip install -r requirements.txt
```

<p>modify <strong>backend/drf_permissions/settings.py</strong> file</p>

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "session_drf",
        "USER": "YOUR_USER",
        "PASSWORD": "YOUR_PASSWORD",
        "HOST": "127.0.0.1",
        "PORT": 5432,
    }
}
```

<p>run database migrations commands</p>

```shell
cd backend/
./manage.py makemigrations
```

```shell
./manage.py migrate
```

<p>create a superuser to add users in the API</p>

```shell
./manage.py createsuperuser
```

<p>run server</p>

```shell
./manage.py runserver
```
