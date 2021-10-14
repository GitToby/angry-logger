def test_version():
    assert angry_logger.__version__ == "0.1.0"


import angry_logger
import logging

angry_logger.go_to_town(potty_mouth=False)
logging.basicConfig(level=logging.DEBUG)

test_logger = logging.getLogger("test_logger")

test_logger.debug("this is a test debug message")
test_logger.info("this is a test info message")
test_logger.warning("this is a test warning message")
test_logger.error("this is a test error message")
