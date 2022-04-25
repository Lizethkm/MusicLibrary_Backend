# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@4hui73fj5ua#fj^f3o-^hfpk(#f9%ura)_vs2fh6oujj830ba'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_library_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Password'
    }
}
