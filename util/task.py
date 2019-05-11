from sqlalchemy import func, distinct, or_, desc

from db import session
import model
import util


def points_per_module_all_years():
    return session.query(
        model.Wave.year.label('year_id'),
        model.Evaluation.user.label('user_id'),
        func.max(model.Evaluation.points).label('points'),
    ).\
        join(model.Evaluation.r_module).join(model.Module.r_task).\
        join(model.Task.r_wave).\
        group_by(model.Wave.year, model.Evaluation.user,
                 model.Evaluation.module)
