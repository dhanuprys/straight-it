import os
from functools import wraps
import middleware
from flask import Flask, request, redirect, g

app_key = os.environ.get("STRAIGHT_API_KEY")
director_driver = os.environ.get("STRAIGHT_DIRECTOR_DRIVER", "http")
app_port = int(os.environ.get("PORT", 8080))
flask_app = Flask(__name__)

environment_vars = {
    "app_key": app_key,
    "director_driver": director_driver
}

def set_environment(env):
    def _setter():
        for env_key in env.keys():
            setattr(g, env_key, env[env_key])

    return _setter

flask_app.before_request(set_environment(environment_vars))
flask_app.before_request(middleware.safe_api_request)
flask_app.before_request(middleware.api_key_filter)

@flask_app.route("/")
def index():
    return "STRAIGHT.IT"

@flask_app.route("/api/v1/links")
def links():
    if request.method == "GET":
        # uri: gateway
        # return: success, target
        return { "success": True }
    elif request.method == "POST":
        # body: target
        # return: success, gateway, url
        pass
    elif request.method == "PUT" or request.method == "UPDATE":
        # body: gateway, target
        # return success, gateway, url
        pass
    elif request.method == "DELETE":
        # body: gateway
        # return: success
        pass


if __name__ == "__main__":
    if app_key == None:
        raise Exception(
            "You must provide a key for application API access"
        )

    if not director_driver == "http" and \
        not director_driver == "javascript":
        raise ValueError("Use http or javascript to application director")

    flask_app.run(
        host="0.0.0.0", 
        port=app_port
    )
