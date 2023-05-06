import logging as original_logging
import random
from typing import Any

from ._const import *

_config = {"potty_mouth": True}


class _AngryLogger(original_logging.Logger):
    @staticmethod
    def clean_up(message: str) -> str:
        if not _config["potty_mouth"]:
            for pattern in NAUGHTY_SUBS:
                message = pattern.sub("*****", message)
        return message

    def debug(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        wrapper = random.choice(DEBUG_SUBS)
        wrapper = self.clean_up(wrapper)
        super().debug(wrapper.format(msg), *args, **kwargs)

    def info(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        wrapper = random.choice(INFO_SUBS)
        wrapper = self.clean_up(wrapper)
        super().info(wrapper.format(msg), *args, **kwargs)

    def warning(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        wrapper = random.choice(WARNING_SUBS)
        wrapper = self.clean_up(wrapper)
        super().warning(wrapper.format(msg), *args, **kwargs)

    def error(self, msg: Any, *args: Any, **kwargs: Any) -> None:
        if random.random() > 0.5:
            first_line = random.choice(ERROR_PRE_LOGS)
            first_line = self.clean_up(first_line)
            super().error(first_line)
        wrapper = random.choice(ERROR_SUBS)
        wrapper = self.clean_up(wrapper)
        super().error(wrapper.format(msg), *args, **kwargs)


def start(potty_mouth=True):
    _config["potty_mouth"] = potty_mouth
    my_regular_logger = original_logging.getLogger("regular_logger")
    my_regular_logger.info("Gosh this is going to be fun...")
    original_logging.setLoggerClass(_AngryLogger)
    my_angry_logger = original_logging.getLogger("angry_logger")
    my_angry_logger.info("You should be all set up now.")
