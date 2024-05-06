FROM    python:3.8

RUN     apt update && \
        apt install -y default-libmysqlclient-dev gcc git pkg-config libxml2-dev libxmlsec1-dev libxmlsec1-openssl

RUN     pip install \
                clickhouse-driver \
                Django==3.2 \
                django-anymail \
                django-constance \
                django-countries \
                django-dbtemplates==4.0 \
                django-extensions \
                django-fancy-cache \
                django-multiselectfield \
                django-mysql \
                django-redis \
                django-rq \
                django-silk \
                django-taggit \
                Faker \
                moment \
                mysqlclient \
                phonenumbers \
                Pillow \
                pycryptodome \
                python-dateutil \
                pytz \
                redis==4.5.4 \
                requests \
                six \
                djangorestframework==2.3.13 \
