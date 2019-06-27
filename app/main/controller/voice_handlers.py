from flask_assistant import tell
from ..service.casting_service import cast_youtube


def cast_intent(q):

    result = cast_youtube(q)

    if result.confirmation == "Failed":
        return tell("Failed to broadcast because {}".format(result.reason))

    return tell("Casting {} on the TV".format(result.data["name"]))
