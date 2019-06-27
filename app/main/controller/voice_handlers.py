#  !/usr/bin/env python
#  Copyright © 2019 Mark Mohades.
#  MIT License

from flask_assistant import tell
from ..service.casting_service import broadcast_youtube


def cast_intent(q):

    result = broadcast_youtube(q)

    if result.confirmation == "Failed":
        return tell("Failed to broadcast because {}".format(result.reason))

    return tell("Casting {} on the TV".format(result.data["name"]))
