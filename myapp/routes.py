from flask import Blueprint, redirect, url_for, render_template

from .extensions import db
from .models import User
from .models import RowStage

main = Blueprint('main', __name__)

@main.route('/')
def mainpage():
    stage = RowStage.query.all()
    if stage:
        if int(stage[0].stage_number) > 20:
            stage = stage[0]
            return render_template("./finished.html", stage=stage)
        else:
            stage = stage[0]
            return render_template("./index.html", stage=stage )
    else:
        return render_template("./waiting.html")

@main.route('/current_stages')
def index():
    users = RowStage.query.all()
    users_list_html = [f"<li>{ user.stage_number }</li>" for user in users]
    return f"<h3>Etappes beschikbaar:</h3><ul>{''.join(users_list_html)}</ul>"

@main.route('/add/<stage_number>/<start>/<finish>/<distance>/<cox>/<stroke>/<bow>/<next_cox>/<next_stroke>/<next_bow>')
def add_stage(stage_number, start, finish, distance, cox, stroke, bow, next_cox, next_stroke, next_bow):
    db.session.add(RowStage(stage_number=stage_number, start=start, finish=finish, distance=distance, cox=cox, stroke=stroke, bow=bow, next_cox=next_cox, next_stroke=next_stroke, next_bow=next_bow,))
    db.session.commit()
    return redirect(url_for("main.index"))

@main.route('/delete/<stage_number>')
def delete_user(stage_number):
    to_delete = RowStage.query.filter_by(stage_number = stage_number).first()
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for("main.index"))