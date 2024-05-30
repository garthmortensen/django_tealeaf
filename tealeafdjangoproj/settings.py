"""
Django settings for tealeafdjangoproj project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
from django.middleware.security import SecurityMiddleware

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# this works when .env is in parent directory of settings.py
dotenv_path = BASE_DIR / ".env"
load_dotenv(dotenv_path)
SECRET_KEY = os.getenv("SECRET_KEY")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

if "PYTHONANYWHERE_DOMAIN" in os.environ:
    print("PYTHONANYWHERE environment is detected")
    remote_hosted = True
else:
    remote_hosted = False

# Detect if running on PythonAnywhere
if remote_hosted:
    ALLOWED_HOSTS = [
        "webdevpony.pythonanywhere.com",
        # "www.yourcustomdomain.com"
    ]
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
else:
    print("PYTHONANYWHERE environment is not detected")
    ALLOWED_HOSTS = ["*"]
    DEBUG = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "firstapp",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # enforces Content Security Policy to prevent XSS attacks by specifying trusted content sources. more settings below
    "csp.middleware.CSPMiddleware",  # Manages Content Security Policy to prevent XSS attacks
    "django.middleware.security.SecurityMiddleware",  # Manages various security-related HTTP headers
    ]


ROOT_URLCONF = "tealeafdjangoproj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "firstapp.context_processors.website_name",  # variable becomes universally available
                "firstapp.context_processors.categories",  # for dynamically populating the navigation bar
            ],
        },
    },
]

WSGI_APPLICATION = "tealeafdjangoproj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

################### EMAIL SETTINGS ###################
# email settings for contact.html form
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS = True  # security: encrypt data from django to email
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv(
    "EMAIL_HOST_PASSWORD"
)  # enable gmail 2-factor auth then https://myaccount.google.com/apppasswords


################### SECURITY SETTINGS ###################

# https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/#https
# Configure Django Settings for Secure Cookies

# Use a secure CSRF cookie
# Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally.
# This setting ensures that the CSRF (Cross-Site Request Forgery) cookie is only sent over HTTPS connections.
# CSRF attacks involve a malicious site or email tricking a user's browser into making an unwanted request on another site where they are authenticated.
# By making the CSRF cookie secure, it can't be sent over unencrypted HTTP, which prevents attackers who are eavesdropping on network traffic from capturing the cookie.
CSRF_COOKIE_SECURE = True  

# Use a secure session cookie
# Set this to True to avoid transmitting the session cookie over HTTP accidentally.
# This setting ensures that session cookies are also only sent over HTTPS.
# Session cookies often contain sensitive data or identifiers that maintain the state of a user session.
# If sent over HTTP, an attacker could perform a 'session hijacking' attack by intercepting the cookie through a man-in-the-middle technique, gaining unauthorized access to the user's session.
SESSION_COOKIE_SECURE = True  

# validate:
# To ensure these settings are effective, visit http://webdevpony.pythonanywhere.com/ and check if it redirects to https://webdevpony.pythonanywhere.com/
# This helps verify that your site is properly configured to redirect HTTP traffic to HTTPS, protecting all data transmitted between the client and server.


###### django-csp Content Security Policy settings to prevent XSS ######
CSP_DEFAULT_SRC = ("'self'",)  # Restricts all content sources to the same origin, preventing the inclusion of malicious content.
# Specifies trusted sources for styles, preventing the inclusion of untrusted stylesheets.
CSP_STYLE_SRC = (
    "'self'", 
    "https://cdnjs.cloudflare.com",  # Allows stylesheets from cdnjs
    "https://cdn.jsdelivr.net",  # Allows stylesheets from jsdelivr
    "https://fonts.googleapis.com"  # Allows stylesheets from Google Fonts
)
# Specifies trusted sources for scripts, preventing the inclusion of untrusted scripts.
CSP_SCRIPT_SRC = (
    "'self'", 
    "https://cdn.jsdelivr.net"  # Allows scripts from jsdelivr
)
CSP_FONT_SRC = ("'self'", "https://fonts.googleapis.com", "https://fonts.gstatic.com")  # Specifies trusted sources for fonts, ensuring only fonts from trusted sources are loaded.
CSP_IMG_SRC = ("'self'", "data:")  # Allows images from the same origin and inline images (data URIs).
CSP_CONNECT_SRC = ("'self'",)  # Restricts connections to the same origin, preventing unauthorized data exfiltration.
CSP_FRAME_SRC = ("'none'",)  # Prevents the site from being embedded in a frame, further protecting against clickjacking.


###### django-secure Security Enhancements ######
# Protects against XSS attacks by enabling the browser's XSS filter. Without it, users could potentially inject JavaScript that steals cookies.
# Secure browser protection against XSS where the browser will try to block detected attacks.
SECURE_BROWSER_XSS_FILTER = True

# Prevent the browser from interpreting files as a different MIME type, which could be exploited by uploading a malicious script with a fake MIME type.
# Prevent MIME type sniffing, which can cause security risks if a user can upload a malicious file disguised with an incorrect MIME.
# Multipurpose Internet Mail Extensions tell browsers what kind of data a file contains. 
# They help the browser understand how to handle files it gets from a server. 
# e.g. when a server sends a file with the MIME type image/jpeg, the browser knows it's dealing with a JPEG image and displays it as an image instead of as text or downloading it.
# SECURE_CONTENT_TYPE_NOSNIFF option stops the browser from guessing the MIME type
# If someone tricks the server into serving a malicious script as something harmless like an image, a browser that tries to guess the MIME types might execute the script
SECURE_CONTENT_TYPE_NOSNIFF = True

if remote_hosted:
    # Redirect all HTTP requests to HTTPS (ensure Django is behind a proxy that sets the 'X-Forwarded-Proto' header on PythonAnywhere).
    SECURE_SSL_REDIRECT = True  # Ensures that all traffic is sent over HTTPS. Without this, attackers could intercept data sent over HTTP.

    # HTTP Strict Transport Security (HSTS) is a security policy mechanism that helps protect websites from man-in-the-middle attacks like protocol downgrade attacks and cookie hijacking. 
    # By setting `SECURE_HSTS_SECONDS` to 31,536,000, you instruct browsers to enforce HTTPS connections to your site for one year. 
    # This prevents accidental HTTP access and increasing security, especially on insecure networks. 
    # This setting helps shield users from SSL stripping attacks, where attackers downgrade HTTPS to HTTP, by ensuring that the browser continuously uses HTTPS. 
    # A longer duration for HSTS is recommended to maintain this protective measure without frequent renewals.
    SECURE_HSTS_SECONDS = 31536000  

    # This setting extends the HSTS policy to all subdomains of the main site. 
    # It's essential to secure not just the main domain but all associated subdomains because attackers might target less secure subdomains to exploit security weaknesses.
    # A subdomain? It's a prefix added to the domain name that helps organize different parts of a website or indicates a separate site under the same brand. 
    # `google.com` has `mail.google.com`, `docs.google.com`. 
    # Subdomains allow companies to separate distinct functionalities and manage them under the same larger domain umbrella.
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True  

    # This tells the browser to include your site in its preload list of sites that are only accessible over HTTPS. 
    # Preloading is a measure that can prevent initial HTTP access before the HSTS header is ever received. 
    # Websites can be submitted to a preload list that browsers use to enforce HTTPS connections before any contact has been made with the servers. 
    # this effectively prevents the first connection from being over HTTP.
    SECURE_HSTS_PRELOAD = True  
