import re
from typing import List

NAUGHTY_SUBS: List[re.Pattern] = [
    re.compile(word, re.IGNORECASE)
    for word in [
        "shit",
        "fuck",
        "crap",
        "ass",
        "dick",
    ]
]

DEBUG_SUBS: List[str] = [
    "{} - any more detail for you, my LORD?",
    "Can I go home now? {}",
]

INFO_SUBS: List[str] = [
    "Ok, so I was told to tell you '{}' but whatever...",
    "You really went and did it, huh... {}",
    "I don't get paid enough for this. here: {}",
    "Ok, ok.. I get it you want some details, hold your horses... {}",
    "You have now been subscribed to Cat Facts Daily. Please text '{}' to 55055 to STOP.",
    "Whats that coming over the hill? Is it a monster? No, its your logging again ffs - {}",
    "Knock knock. Who's there? your stupid log event: {}",
    "{}. But what do you mean by that?",
    "\N{pile of poo}\N{pile of poo}\N{pile of poo} {}",  # todo: add full emojification
]

WARNING_SUBS: List[str] = [
    "{} - do something about it, asshole.",
    "Right, this right here? Its shit. Fix it: {}",
    "Did you do something stupid? Look: {}",
    "And one. And two. And.. wait that's not meant to happen... {}",
]

ERROR_PRE_LOGS: List[str] = [
    "SHIT! SHIT! SHIT!",
    "CRAP! CRAP! CRAP!",
    "FUCK! FUCK! FUCK!",
    "What the fuck just happened?!",
]

ERROR_SUBS: List[str] = [
    "Look at this shit! {}",
    "{}????? Are you FUCKING kidding me??",
    "You fucked it: {}",
    "God damn it! you dickhead! it happened: {}",
]
