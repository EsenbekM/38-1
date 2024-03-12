from pathlib import Path


# BASE_DIR - Путь к каталогу проекта 
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY - Секретный ключ проекта
SECRET_KEY = 'django-insecure-2@hy_p@3-671jv&q6e2rybok+qnko9ol1&kh^6z*=-6r&*0dhb'

# TODO: 
DEBUG = True

# TODO
ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    # Приложения по умолчанию
    'django.contrib.admin', # Приложение административной панели
    'django.contrib.auth', # Приложение аутентификации
    'django.contrib.contenttypes', # Приложение для работы с контентом
    'django.contrib.sessions',  # Приложение для работы с сессиями
    'django.contrib.messages', # Приложение для работы с сообщениями
    'django.contrib.staticfiles', # Приложение для работы со статическими файлами

    # Пользовательские приложения
    'post',
]

# TODO: MIDDLWARE - Промежуточное ПО 
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TODO
ROOT_URLCONF = 'blog.urls'

# Templates - Настройки шаблонов
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# TODO
WSGI_APPLICATION = 'blog.wsgi.application'


# DATABASES - Настройки базы данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# AUTH_PASSWORD_VALIDATORS - Валидаторы пароля
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# TODO
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# TODO
STATIC_URL = 'static/'


# TODO
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
