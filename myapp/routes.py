from flask import Blueprint, redirect, url_for

from .extensions import db
from .models import User
from .models import Stage

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = Stage.query.all()
    users_list_html = [f"<li>{ user.current_stage }</li>" for user in users]
    return f"<ul>{''.join(users_list_html)}</ul>"

@main.route('/add/<stage>')
def add_stage(stage):
    db.session.add(Stage(current_stage=stage))
    db.session.commit()
    return redirect(url_for("main.index"))