from flask import jsonify, make_response


def AdaptControllerToFlask(controller, request):
    response = controller.handle(request.json)
    return make_response(jsonify(response.body), response.status_code)
