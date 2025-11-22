import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

from qualification import qualification_list, professional_list, sertificates_list
from flask import Flask, render_template


application = Flask(__name__)
application.config.from_pyfile("app.config")


@application.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@application.errorhandler(405)
def page_not_found(e):
    return render_template("404.html"), 405


@application.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        professional_list=professional_list,
        qualification_list=qualification_list,
        sertificates_list=sertificates_list,
    )


if __name__ == "__main__":
    application.run(host="0.0.0.0")
