from flask import jsonify

# request response auto generate function
def request_response(message=None, error=False):
    return jsonify({
        'isSuccess': False if error else  True,
        'message': message
    })
