from collections import OrderedDict
from datetime import date, datetime
from flask import Flask, jsonify, make_response, request, abort
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': "Not found"}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': "Bad Request"}), 400)


@app.route('/api', methods=['GET'], strict_slashes=False)
def get_details():
    try:
        slack_name = request.args['slack_name']
        track = request.args['track']
    except:
        abort(400)

    # details = {
    #     'slack_name': slack_name,
    #     'current_day': date.today().strftime('%A'),
    #     'utc_time': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
    #     'track': track,
    #     'github_file_url': "https://github.com/Henree001/hng/myapp.py",
    #     'github_repo_url': "https://github.com/username/hng",
    #     'status_code': 200
    # }
    

    response_data = [
        ("slack_name", slack_name),
        ("current_day", date.today().strftime('%A')),
        ("utc_time", datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')),
        ("track", track),
        ("github_file_url", "https://github.com/Henree001/hng/myapp.py"),
        ("github_repo_url", "https://github.com/username/hng"),
        ("status_code", 200)
    ]

    # Convert the list of tuples to a dictionary
    details = dict(response_data)
    return jsonify(details)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
