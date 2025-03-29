import logging
import queue
from logging import Logger
from logging.handlers import QueueHandler, QueueListener
from pythonjsonlogger.json import JsonFormatter


que = queue.Queue(-1)  # no limit on size
queue_handler = QueueHandler(que)
handler = logging.StreamHandler()
listener = QueueListener(que, handler)
root = logging.getLogger()
root.addHandler(queue_handler)
root.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(threadName)s: %(message)s')
handler.setFormatter(formatter)
formatter = JsonFormatter(
        "{asctime}{levelname}{message}{exc_info}{name}",
        style="{"
    )
handler.setFormatter(formatter)