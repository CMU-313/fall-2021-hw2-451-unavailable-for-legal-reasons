import logging

from mayan.celery import app

from .classes import Statistic

logger = logging.getLogger(name=__name__)


@app.task(ignore_result=True)
def task_execute_statistic(slug):
    logger.info('Executing')

    Statistic.get(slug=slug).execute()

    logger.info('Finshed')
