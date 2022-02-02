"""
Django settings for mesport project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+tk7ajdow_s+(ei2mh3t0-)%%+hn-l_w%+%_3=b0hy*@tef60n'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*',]

# Application definition

INSTALLED_APPS = [
    # 'admin_shortcuts',
    'django_jalali',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sportsprogram.apps.SportsprogramConfig',
    'phonenumber_field',
    'multiselectfield',
    'rest_framework',
    # 'jalali_date',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mesport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["{}/media/templates/".format(BASE_DIR)],
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

WSGI_APPLICATION = 'mesport.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': 'mesport',
        'PASSWORD': '123456789',
        'USER': 'postgres',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

import locale

locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#
STATIC_URL = '/static/'
# # STATIC_ROOT = BASE_DIR / 'static'
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
#     ]
#
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSIONS_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    )

}

# Admin Shortcuts
#
# ADMIN_SHORTCUTS = [
#     {
#         'shortcuts': [
#             {
#                 'url': '/',
#                 'open_new_window': True,
#             },
#             {
#                 'url_name': 'admin:logout',
#             },
#             {
#                 'title': 'Users',
#                 'url_name': 'admin:auth_user_changelist',
#                 'count': 'mesport.utils.count_users',
#             },
#             {
#                 'title': 'Groups',
#                 'url_name': 'admin:auth_group_changelist',
#                 'count': 'mesport.sportsprogram.count_groups',
#             },
#             {
#                 'title': 'Add user',
#                 'url_name': 'admin:auth_user_add',
#                 'has_perms': 'mesport.sportsprogram.has_perms_to_users',
#             },
#         ]
#     },
#     {
#         'title': 'برنامه انالیز بدن',
#         'shortcuts': [
#             {
#                 'title': 'Pages',
#                 'url_name': 'sportsprogram:ApiListPersonInfo',
#                 'count': 'mesport.sportsprogram.PersonInfo',
#
#             },
#             {
#                 'title': 'Files',
#                 'url_name': 'admin:index',
#             },
#             {
#                 'title': 'Contact forms',
#                 'icon': 'columns',
#                 'url_name': 'admin:index',
#                 'count_new': '3',
#             },
#             {
#                 'title': 'Products',
#                 'url_name': 'admin:index',
#             },
#             {
#                 'title': 'test',
#                 'url_name': 'admin:index',
#                 'count_new': '12',
#             },
#         ]
#     },
# ]
# ADMIN_SHORTCUTS_SETTINGS = {
#     'show_on_all_pages': True,
#     'hide_app_list': True,
#     'open_new_window': True,
# }