
[![version](https://img.shields.io/pypi/v/angry-logger)](https://pypi.org/project/angry-logger/)
[![licence](https://img.shields.io/pypi/l/angry-logger)](https://github.com/GitToby/angry-logger)

# Angry Logging Made Easy

Do you want to show your logger to be more passive aggressive? maybe just actual aggressive? This is the library for
you.

## Installation
You can install via pip!
```shell
pip install angry-logger
```

## Usage
When deciding your project needs more aggression, all you have to do is tell the Angry Logger to go to town. Like so.
```python
import angry_logger
angry_logger.start()
```
If you're not a fan of naughty words, you can tell the angry logger to be less of a potty mouth.
```python
import angry_logger
angry_logger.start(potty_mouth=False)
```

From here, use your logging as you normally would.
```python
import angry_logger
import logging

angry_logger.start(potty_mouth=False)
logging.basicConfig(level=logging.DEBUG)

test_logger = logging.getLogger("test_logger")

test_logger.debug("this is a test debug message")
test_logger.info("this is a test info message")
test_logger.warning("this is a test warning message")
test_logger.error("this is a test error message")
```

This will output your new normal, information hidden behind abuse.
```
DEBUG:test_logger:Can I go home now? this is a test debug message
INFO:test_logger:this is a test info message. But what do you mean by that?
WARNING:test_logger:Did you do something stupid? Look: this is a test warning message
ERROR:test_logger:this is a test error message????? Are you *****ING kidding me??
```