from flask import Flask, request, abort
from functools import wraps

app = Flask(__name__)


def validate_json(*expected_args):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            json_object = request.get_json()
            for expected_arg in expected_args:
                if expected_arg not in json_object:
                    abort(400)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# curl -H "Content-Type: application/json" -X POST -d '{"student_id":1}' http://localhost:5000/grade

@app.route('/grade', methods=['POST'])
@validate_json('student_id')
def update_grade():
    json_data = request.get_json()
    print(json_data)
    # update database
    return "success!"


if __name__ == "__main__":

    app.run()
