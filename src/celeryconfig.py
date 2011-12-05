BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "herald_user"
BROKER_PASSWORD = "dlareh"
BROKER_VHOST = "herald_queue"

CELERY_RESULT_BACKEND = "amqp"
CELERY_AMQP_TASK_RESULT_EXPIRES = 300

CELERY_IMPORTS = ("workers.fest.workers", )
