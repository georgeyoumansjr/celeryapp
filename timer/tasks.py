# myapp/tasks.py
from celery import shared_task
import logging

# Create a logger instance for the current module
logger = logging.getLogger(__name__)

@shared_task
def add(x, y):
    logger.info("This task is running!")
    return x + y

