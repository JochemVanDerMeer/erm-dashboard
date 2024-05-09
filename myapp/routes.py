from flask import Blueprint, redirect, url_for, render_template
from .extensions import db
from .models import User
from .models import RowStage
from werkzeug.security import generate_password_hash
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash

auth = HTTPBasicAuth()

main = Blueprint('main', __name__)

user = 'erm'
pw = 'erm'
users = {
    user: generate_password_hash(pw)
}

@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False

@main.route('/')
def mainpage():
    stage = RowStage.query.all()
    if stage:
        if int(stage[0].stage_number) == 21:
            stage = stage[0]
            return render_template("./finished.html", stage=stage)
        else:
            stage = min(stage, key=lambda x: int(x.stage_number))
            #print((int(stage[0].stage_number)))
            #stage = stage[0]
            return render_template("./index.html", stage=stage )
    else:
        return render_template("./waiting.html")

@main.route('/current_stages')
def index():
    users = RowStage.query.all()
    sorted_users = sorted(users, key=lambda x: int(x.stage_number))
    users_list_html = [f"<li>{ user.stage_number }</li>" for user in sorted_users]
    #return f"<h3>Etappes beschikbaar:</h3><ul>{''.join(users_list_html)}</ul>"
    return f"<p>Klik <a href='/'>hier</a> om terug te gaan naar het dashboard.</p><h3>Etappes beschikbaar:</h3><ul>{''.join(users_list_html)}</ul>"

@main.route('/add/<stage_number>/<start>/<finish>/<distance>/<cox>/<stroke>/<bow>/<next_cox>/<next_stroke>/<next_bow>')
@auth.login_required
def add_stage(stage_number, start, finish, distance, cox, stroke, bow, next_cox, next_stroke, next_bow):
    db.session.add(RowStage(stage_number=stage_number, start=start, finish=finish, distance=distance, cox=cox, stroke=stroke, bow=bow, next_cox=next_cox, next_stroke=next_stroke, next_bow=next_bow,))
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route('/delete/<stage_number>')
@auth.login_required
def delete_user(stage_number):
    to_delete = RowStage.query.filter_by(stage_number = stage_number).first()
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route('/go_to_next_stage', methods=['GET', 'POST'])
@auth.login_required
def next_stage():
    stage = RowStage.query.all()
    stage = min(stage, key=lambda x: int(x.stage_number))
    to_delete = RowStage.query.filter_by(stage_number = stage.stage_number).first()
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for("main.mainpage"))

@main.route('/status')
@auth.login_required
def status():
    return render_template("./status.html")