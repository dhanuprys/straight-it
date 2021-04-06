import os
from flask import Flask, request, redirect, g, render_template
import middleware
import response_builder
from model.jsonstorage import jsonstorage
import orjson
import generator

# FIXME: Add response code

app_key = os.environ.get("STRAIGHT_API_KEY")
http_referrer = os.environ.get("STRAIGHT_HTTP_REFERRER", "http")
app_port = int(os.environ.get("PORT", 8080))
current_host = os.environ.get("CURRENT_HOST", "http://localhost" + str(app_port)) + "/r/"
flask_app = Flask(__name__)

environment_vars = {
    "app_key": app_key,
    "http_referrer": http_referrer,
    "current_host": current_host
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
    return render_template("index.html")

@flask_app.route("/r/<gateway>")
def redirect_user(gateway):
    target = jsonstorage.get_target(gateway)

    if not target:
        return "404 Not Found"

    if g.get("http_referrer") in ["javascript", "js"]:
        return render_template("js_director.html", target=target)
    elif g.get("http_referrer") == "http":
        return redirect(target, code=301)

@flask_app.route("/api/v1/links", methods=[
    "GET", "POST", "UPDATE", "PUT", "DELETE"
])
def links():
    request_payload = None

    try:
        request_payload = orjson.loads(request.get_data())
    except:
        if request.method in ["POST", "UPDATE", "PUT", "DELETE"]:
            return response_builder.fail("unknown:middleware", "Request body is not JSON")

        request_payload = {}

    if request.method == "GET":
        # uri: gateway
        # return: success, target
        
        gateway = request.args.get("gateway")

        if not gateway:
            return response_builder.fail("read", "No gateway specified")

        gateway_target = jsonstorage.get_target(gateway)

        if not gateway_target:
            return response_builder.fail("read", "Gateway not found")

        return response_builder.success("read", {
            "target": gateway_target
        })
    elif request.method == "POST":
        # body: target, gateway (custom gateway)
        # return: success, gateway, url
        link_target = request_payload.get("target")
        
        if not link_target:
            return response_builder.fail("create", "'target' is not available.")
        
        gateway = request_payload.get("gateway") or generator.generate_id()

        if jsonstorage.store(gateway, link_target, throw_exception=False):
            return response_builder.success("create", {
                "gateway": gateway,
                "url": generator.shorted_url(gateway)
            })

        return response_builder.fail("create", "Failed to store link target.")
    elif request.method == "PUT" or request.method == "UPDATE":
        # body: gateway, target
        # return success, gateway, url

        gateway = request_payload.get("gateway")
        new_target = request_payload.get("target")
        
        if not gateway or not new_target:
            return response_builder.fail(
                "update", 
                "'gateway' or 'target' is not avalaible on request body"
            )

        if jsonstorage.update(gateway, new_target):
            return response_builder.success("update", {
                "gateway": gateway,
                "target": new_target
            })

        return response_builder.fail("update", "Failed to update links")
    elif request.method == "DELETE":
        # body: gateway
        # return: success, gateway
        gateway = request_payload.get("gateway")

        if not gateway:
            return response_builder.fail(
                "delete", 
                "'gateway' not avalaible on request body"
            )
        
        if jsonstorage.delete(gateway, throw_exception=False):
            return response_builder.success("delete", {
                "gateway": gateway
            })
        
        return response_builder.fail("delete", "Failed to delete selected gateway")

if __name__ == "__main__":
    if app_key == None:
        raise Exception(
            "You must provide a key for application API access"
        )

    if not http_referrer in ["javascript", "js", "http"]:
        raise ValueError("Use http or javascript to application director")

    flask_app.run(
        host="0.0.0.0", 
        port=app_port,
        debug=True
    )
