import os
from datetime import timedelta
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent



databases = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite91",
    }
}



# databases = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('NAME'),
#         'USER': 'data_ecommerce',
#         'PASSWORD': os.environ.get('PASSWORD'),

#         'HOST': os.environ.get('HOST'),
#         'PORT': os.environ.get('PORT'),
#     }
# }











































