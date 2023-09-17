from .tasks import add
import logging

# Create a logger instance for the current module
logger = logging.getLogger(__name__)

count = 10

while count > 1:
    result = add.delay(count, 4)
    logger.info(f"Task {result} sent to the queue.")

    count -= 1
    # Check if task is ready (i.e., if it has finished execution)
    if result is not None:
        print("Task has finished execution.")
        print("Task result:", result)
    else:
        print("Task has not finished execution yet.")