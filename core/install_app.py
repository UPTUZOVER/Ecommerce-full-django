import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')


#install apps
installed_apps=[
    'rest_framework_swagger',
    'jazzmin',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    "djoser",
    'corsheaders',
    "cart",
    'parler',
    'parler_rest',
    "categories",
    'Account',
    "products",
    "contact",
    "checkout",
    "cart_variant_2",
    "drf_yasg",
]




parler_languages = {
    None: (
        {'code': 'ru',},
        {'code': 'uz',},
    ),
    'default': {
        'fallbacks': ['ru'],    
        'hide_untranslated': False,   # Default
    }
}




rest_framework = {
        'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE': 5,
 
        'NON_FIELD_ERRORS_KEY': 'error',
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        )
        
    }






simple_jwt = {"AUTH_HEADER_TYPES":('jwt',),
    
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=100),
    # "ROTATE_REFRESH_TOKENS": False,
    # "BLACKLIST_AFTER_ROTATION": False,
    # "UPDATE_LAST_LOGIN": False,

    # "ALGORITHM": "HS256",
    # "SIGNING_KEY": SECRET_KEY,
    # "VERIFYING_KEY": "",
    # "AUDIENCE": None,
    # "ISSUER": None,
    # "JSON_ENCODER": None,
    # "JWK_URL": None,
    # "LEEWAY": 0,

    # "AUTH_HEADER_TYPES": ("Bearer",),
    # "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    # "USER_ID_FIELD": "id",
    # "USER_ID_CLAIM": "user_id",
    # "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    # "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    # "TOKEN_TYPE_CLAIM": "token_type",
    # "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    # "JTI_CLAIM": "jti",

    # "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    # "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    # "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    # "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    # "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    # "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    # "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    # "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    # "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",

}




jazzmin_settings = {
    'site_title': 'UPT',
    'site_header': 'Your Site Header',
    'site_logo': '/static/logo.png',
    'welcome_sign': 'Welcome to Your Site',
    'search_model': 'auth.User',
    'show_sidebar': True,
    'navigation_expanded': False,
    'hide_apps': [],
    'hide_models': [],
    'related_modal_active': True,
    'custom_css': '/static/path/to/custom.css',
    'custom_js': '/static/path/to/custom.js',
    'icons': {
        'auth': 'icon-lock',
        'sites': 'icon-rocket',
    },
    'topmenu_links': [
        {
            'name': 'Documentation',
            'url': 'https://uptuz.vercel.app/',
            'new_window': True,
        },
        {
            'name': 'Support',
            'url': 'https://uptuz.vercel.app/',
            'new_window': True,
        },
    ],
    'usermenu_links': [
        {
            'name': 'Profile',
            'url': '/admin/profile/',
            'new_window': False,
        },
        {
            'name': 'Logout',
            'url': '/admin/logout/',
            'new_window': False,
        },
    ],
    'show_ui_builder': True,
}



















