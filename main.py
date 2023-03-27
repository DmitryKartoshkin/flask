from flask import Flask, request, jsonify
from error import HttpError
from service import Advertisement

app = Flask("flask")


@app.errorhandler(HttpError)
def error_handler(error: HttpError):
    responce = jsonify({"status": "error", "description": error.description})
    responce.status_code = error.status_code
    return responce


app.add_url_rule(
    "/advertisement/<int:advertisement_id>/",
    view_func=Advertisement.as_view("advertisement"),
    methods=['GET', "DELETE"]
)

app.add_url_rule(
    "/advertisement/",
    view_func=Advertisement.as_view("advertisement_create"),
    methods=['POST']
)

if __name__ == '__main__':
    app.run()

