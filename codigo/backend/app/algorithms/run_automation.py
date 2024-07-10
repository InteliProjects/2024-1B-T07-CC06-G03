from flask import jsonify
from threading import Lock
from app.algorithms.walker import *
from concurrent.futures import ThreadPoolExecutor

"""
Este módulo implementa uma API Flask para gerenciar a automação de tarefas assíncronas em uma aplicação de roteamento otimizado. Ele utiliza um pool de threads para executar tarefas computacionalmente intensivas, como simulações ou cálculos de rotas, sem bloquear o servidor principal. As funções do módulo permitem iniciar, monitorar e resetar automações de forma controlada e segura.

O módulo é projetado para ser integrado em sistemas que necessitam de execução assíncrona de tarefas pesadas, como algoritmos de otimização de rotas ou processamento de grandes volumes de dados. O uso de bloqueios (locks) e a gestão de estado garantem que as tarefas sejam manipuladas corretamente mesmo em ambientes de concorrência.

Funções Incluídas:
- start_automation: Recebe uma requisição para iniciar uma tarefa de automação, verifica o estado atual e, se ocioso, inicia a tarefa solicitada em um thread separado.
- get_automation_status: Fornece o status atual da automação, permitindo que clientes verifiquem se uma tarefa está em andamento, ociosa ou concluída.
- reset_automation: Permite resetar o status da automação para um estado inicial, preparando o sistema para uma nova tarefa.
- run_walker: Função que executa a tarefa assíncrona propriamente dita, usando o algoritmo selecionado para processar os dados fornecidos.

"""


executor = ThreadPoolExecutor(2)
status_lock = Lock()
status = {"state": "idle", "result": None}

def start_automation(request):
    """
    Inicia a automação de uma tarefa assíncrona usando o algoritmo selecionado.

    Args:
        request (Request): Objeto de requisição Flask contendo os dados JSON com as chaves 'select_algo' e 'readers'.

    Returns:
        str: Mensagem indicando se a tarefa foi submetida ou se já está em execução.
    """
    with status_lock:  # Garante que apenas uma thread possa alterar o estado de cada vez
        if status["state"] == "idle":
            data = request.get_json()
            select_algo = data.get('select_algo')
            readers = data.get('readers')
            time_readings = data.get('time_readings')
            hours_work = data.get('hours_work')
            total_days = data.get('total_days')
            
            # Submete a tarefa ao executor e atualiza o estado
            executor.submit(run_walker, select_algo, readers, time_readings, hours_work, total_days)
            status["state"] = "running"
            return jsonify(message='Task submitted!'), 202
        else:
            # Retorna uma mensagem de erro se a simulação já estiver em execução
            return jsonify(message='Simulation already in progress! Please wait.'), 409

def get_automation_status():
    """
    Retorna o status atual da automação.

    Returns:
        Response: Objeto de resposta Flask com o status atual da automação em formato JSON.
    """
    return jsonify(status)

def reset_automation():
    """
    Reseta o status da automação para o estado inicial.

    Returns:
        str: Mensagem indicando que a tarefa foi resetada.
    """
    status["state"] = "idle"
    status["result"] = None
    return "Task reset!"

def run_walker(select_algo, readers, time_readings, hours_work, total_days):
    """
    Executa a tarefa de automação utilizando o algoritmo selecionado e a lista de leitores.

    Args:
        select_algo (str): Nome do algoritmo selecionado.
        readers (list): Lista de leitores para serem processados pelo algoritmo.

    Side Effects:
        Atualiza o status da automação para 'finished' e armazena o resultado ou a mensagem de erro.
    """
    try:
        print("Task started!")
        result = walker(select_algo, readers, time_readings, hours_work, total_days)
        status["result"] = result
        print("Task done!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        status["state"] = "finished"
