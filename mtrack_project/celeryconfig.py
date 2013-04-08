from celery.schedules import crontab

## Broker settings.
BROKER_URL = "amqp://guest:guest@localhost:5672//"

CELERY_RESULT_BACKEND = "amqp"

# List of modules to import when celery starts.
CELERY_IMPORTS = ("dhis2.reports_submission_tasks", "fred_consumer.tasks")

USE_TZ = True
CELERY_TIMEZONE = 'Africa/Kampala'

CELERY_TIME_TO_WAIT_BEFORE_RETRYING_SUBMISSION = 600 # wait 10 mins for supervisor or other to relaunch celery and retry
CELERY_NUMBER_OF_RETRIES_IN_CASE_OF_FAILURE = 1 # only retry once on the same day... the following day submission will pick up the rest.

CELERYBEAT_SCHEDULE = {
    'submit-reports-everyday_at_10PM': {
            'task': 'dhis2.reports_submission_tasks.weekly_report_submissions_task',
            'schedule': crontab(hour=21, minute=59, day_of_week='*'),
            'args': ()
        },
    'run-fred-sync-everyday_at_9PM': {
            'task': 'fred_consumer.tasks.run_fred_sync',
            'schedule': crontab(hour=20, minute=59, day_of_week='*'),
            'args': ()
        },
}

