import logging
# import os
# os.makedirs("Log",exist_ok=True)


logging.basicConfig(
    filename="Log/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)

logger=logging.getLogger(__name__)