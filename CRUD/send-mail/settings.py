MAILQUEUE_LIMIT = 100
MAILQUEUE_QUEUE_UP = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse'
         }
     },
    'handlers': {
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'include_html': True,
        },
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'os.path.join(BASE_DIR, "project.log")'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        'mailqueue': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': False
        },
    },
}


EMAIL_USE_TLS = True 
EMAIL_HOST = '**************' #SMTP server of the mail server
EMAIL_HOST_USER = '***********' # Username of the mail server
EMAIL_HOST_PASSWORD = '************' # Password of mail server
EMAIL_PORT = 587 #Email post of TLS (Normally 587)
DEFAULT_FROM_EMAIL = 'hello@example.com'
SERVER_EMAIL = 'hello@example.com'
ADMIN_EMAIL = 'hello@example.com'
DEFAULT_CC_EMAIL = 'hello@example.com'
DEFAULT_REPLY_TO_EMAIL = "hello@example.com"