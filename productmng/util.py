# productmng/util.py

from functools import wraps
from flask import flash, jsonify, abort, request
from productmng.models import User


def check_session_expired(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            user_id = request.headers.get('user_id')
            session = request.headers.get('session')
            user = User.objects(id=user_id).first()
            if user is None or user.disabled is True or user.current_session != session:
                abort(401)

        except Exception as error:
            abort(401)

        return func(*args, **kwargs)

    return decorated_function
