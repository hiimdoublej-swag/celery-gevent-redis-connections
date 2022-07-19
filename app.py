import os

import celery


app = celery.Celery()
app.conf.update({
    'broker_url': os.environ.get('CELERY_BROKER_URL'),
    'result_backend': os.environ.get('CELERY_RESULT_BACKEND_URL')
})

@celery.shared_task(bind=True)
def nested(task):
    return True


@celery.shared_task(bind=True)
def outer(task):
    result = nested.apply_async().get(timeout=10)
    return result
