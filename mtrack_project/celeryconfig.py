from celery.schedules import crontab

## Broker settings.
BROKER_URL = "amqp://guest:guest@localhost:5672//"

CELERY_RESULT_BACKEND = "amqp"

# List of modules to import when celery starts.
CELERY_IMPORTS = ("dhis2.reports_submission_tasks", )

CELERYBEAT_SCHEDULE = {
    'submit-reports-from-monday-to-thursday': {
            'task': 'dhis2.reports_submission_tasks.weekly_report_submissions_task',
            'schedule': crontab(hour=23, minute=59, day_of_week=[1,2,3,4]),
            'args': ()
        },
}

CELERY_TIMEZONE = 'UTC'