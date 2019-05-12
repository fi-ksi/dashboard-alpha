from sqlalchemy import func, distinct, or_, desc

from db import session
import model
import util


def points_per_module_all_years():
    return session.query(
        model.Wave.year.label('year_id'),
        model.Evaluation.user.label('user_id'),
        model.Evaluation.module.label('module_id'),
        func.max(model.Evaluation.points).label('points'),
    ).\
        join(model.Evaluation.r_module).join(model.Module.r_task).\
        join(model.Task.r_wave).\
        group_by(model.Wave.year, model.Evaluation.user,
                 model.Evaluation.module)


def points_per_module(year_id):
    return session.query(
        model.Evaluation.user.label('user_id'),
        model.Evaluation.module.label('module_id'),
        func.max(model.Evaluation.points).label('points'),
    ).\
        join(model.Evaluation.r_module).join(model.Module.r_task).\
        join(model.Task.r_wave).\
        filter(model.Wave.year == year_id).\
        group_by(model.Evaluation.user, model.Evaluation.module)


def _max_points_per_wave(bonus=False):
    points_per_task = session.query(
        model.Module.task.label('id'),
        func.sum(model.Module.max_points).label('points')
    )
    if not bonus:
        points_per_task = points_per_task.filter(model.Module.bonus == False)
    points_per_task = points_per_task.group_by(model.Module.task).subquery()

    return session.query(model.Wave.id.label('id'),
                         func.sum(points_per_task.c.points).label('points'),
                         func.count(model.Task.id).label('tasks_count')).\
        outerjoin(model.Task, model.Task.wave == model.Wave.id).\
        outerjoin(points_per_task, points_per_task.c.id == model.Task.id).\
        group_by(model.Wave)


def max_points_per_year(bonus=False):
    """{year_id: (max_points, tasks_count)}"""
    points_per_wave = _max_points_per_wave(bonus).subquery()
    points_per_year = session.query(
        model.Year.id.label('id'),
        func.sum(points_per_wave.c.points).label('points'),
        func.sum(points_per_wave.c.tasks_count).label('tasks_count')
    ).\
        outerjoin(model.Wave, model.Wave.year == model.Year.id).\
        outerjoin(points_per_wave, points_per_wave.c.id == model.Wave.id).\
        group_by(model.Year).all()

    return {
        year.id: (year.points if year.points else 0.0,
                  int(year.tasks_count) if year.tasks_count else 0)
        for year in points_per_year
    }


def large_tasks():
    """[task]"""
    return session.query(model.Task).\
        join(model.Task.modules).\
        filter(model.Module.type == model.ModuleType.GENERAL)
