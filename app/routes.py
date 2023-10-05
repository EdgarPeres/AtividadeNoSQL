from uuid import UUID

from flask import Blueprint, render_template, request, redirect, url_for
import app.models as tarefa_model

task_routes = Blueprint('task_routes', __name__)


@task_routes.route('/')
def index():
    task = tarefa_model.listar_tarefas()
    return render_template('index.html', tasks=task)


@task_routes.route('/add_Task', methods=['POST'])
def add_task():
    task_description = request.form['task_description']
    tarefa_model.adicionar_tarefa(task_description)
    return redirect(url_for('task_routes.index'))


@task_routes.route('/delete_task/<task_id>')
def delete_task(task_id):
    task_id = UUID(task_id)
    tarefa_model.remover_tarefa(task_id)
    return redirect(url_for('task_routes.index'))
