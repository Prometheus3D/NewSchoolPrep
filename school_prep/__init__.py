from flask import Flask, render_template, jsonify, flash, make_response, request, Blueprint


def create_app():
    from school_prep.main.routes import main
    from school_prep.math.routes import math
    from school_prep.test.routes import test
    static_folder = "../static/"
    template_folder = "../templates/"
    app = Flask(__name__, static_folder=static_folder, static_url_path="/static", template_folder=template_folder)
    app.config['SECRET_KEY'] = 's3cr3t'
    app.config['PER_PAGE'] = 1
    app.register_blueprint(main)
    app.register_blueprint(test)
    app.register_blueprint(math)
    return app
