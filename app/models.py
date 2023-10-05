from cassandra.cluster import Cluster
from flask import jsonify

cluster = Cluster(['localhost'])
session = cluster.connect()
session.set_keyspace('task_manager')


def listar_tarefas():
    tasks = session.execute('SELECT * FROM Task')
    return tasks


def adicionar_tarefa(task_description):
    descricao = task_description
    if descricao:
        session.execute('INSERT INTO Task (id, description) VALUES (uuid(), %s)', [task_description])
        return jsonify({'message': 'Tarefa adicionada com sucesso!'})
    else:
        return jsonify({'error': 'A descrição da tarefa é obrigatória.'}), 400


def remover_tarefa(task_id):
    session.execute('DELETE FROM Task WHERE id = %s', [task_id])
    return jsonify({'message': 'Tarefa removida com sucesso!'})