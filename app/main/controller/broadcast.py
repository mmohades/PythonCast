#  !/usr/bin/env python
#  Copyright © 2019 Mark Mohades.
#  MIT License

from ..model.Response import Error
from ..service.casting_service import broadcast_youtube
from flask import Response, json


def youtube_broadcast(req):

    query = req.args.get('q')

    if query is None:
        error = Error("Query is not provided. Provide it as the q parameter.")
        return Response(
            response=json.dumps(error.dic()),
            status=400,
            mimetype='application/json'
        )

    result = broadcast_youtube(query)
    return Response(
        response=json.dumps(result.dic()),
        status=200,
        mimetype='application/json'
    )
