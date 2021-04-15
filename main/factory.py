from flask import Flask , g, render_template, request, url_for, send_from_directory,jsonify, send_file
from main import config
from main.database import db
from main.user import user
#from main.fadmin import admin

from main.extensions import lm,  mail, migrate,limiter, ck_editor,thum
from flask_login import login_required
# Arrow - это модуль Python для работы с датой и временем
# import arrow
# import time
# from main.utils import url_for_other_page
# import requests
from main.front import front

# from main.api import api_bp
# from main.pages import page
# from main.articles import article
# from main.commands import create_db, drop_db, create_user, recreate_db
# import os
# from flask_ckeditor import upload_fail, upload_success


def create_app(config=config.base_config):   #  basedir_not_main=config.basedir_not_main  2-ой  аругмент
    """Returns an initialized Flask application."""
    node = Flask(__name__, template_folder="templates")
    node.config.from_object(config)
    register_extensions(node)
    register_blueprints(node)
    return node

def register_extensions(node):
    """Register extensions with the Flask application."""
    db.init_app(node)
    migrate.init_app(node, db)
    lm.init_app(node)
#    admin.init_app(node)
# mail.init_app(node)

    # register_errorhandlers(node)
    # limiter.init_app(node)
    # ck_editor.init_app(node)
    # thum.init_app(node)


def register_blueprints(node):
    """Register blueprints with the Flask application."""
    node.register_blueprint(front, url_prefix='/')
    node.register_blueprint(user, url_prefix='/')
#     node.register_blueprint(page, url_prefix='/page')
#     node.register_blueprint(article, url_prefix='/articles')
#     node.register_blueprint(api_bp, url_prefix='/api')
#
#
#
#
# def register_errorhandlers(app):
#     """Register error handlers with the Flask application."""
#
#     def render_error(e):
#         return render_template('errors/%s.html' % e.code), e.code
#
#     for e in [
#         requests.codes.INTERNAL_SERVER_ERROR,
#         requests.codes.NOT_FOUND,
#         requests.codes.UNAUTHORIZED,
#     ]:
#         app.errorhandler(e)(render_error)
#
# def register_jinja_env(app):
#     """Configure the Jinja env to enable some functions in templates."""
#     app.jinja_env.globals.update({
#         'timeago': lambda x: arrow.get(x).humanize(),
#         'url_for_other_page': url_for_other_page,
# })
#
#
# def register_commands(app):
#     """Register custom commands for the Flask CLI."""
#     for command in [create_db, drop_db, create_user, recreate_db]:
#         app.cli.command()(command)