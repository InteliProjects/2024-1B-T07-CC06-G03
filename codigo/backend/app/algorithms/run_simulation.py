from flask import jsonify
from threading import Lock
from app.algorithms.walker import *
from concurrent.futures import ThreadPoolExecutor

"""
Este módulo implementa uma API Flask para gerenciar a simulação de tarefas assíncronas em uma aplicação de roteamento otimizado. Ele utiliza um pool de threads para executar tarefas computacionalmente intensivas, como simulações ou cálculos de rotas, sem bloquear o servidor principal. As funções do módulo permitem iniciar, monitorar e resetar simulações de forma controlada e segura.

O módulo é projetado para ser integrado em sistemas que necessitam de execução assíncrona de tarefas pesadas, como algoritmos de otimização de rotas ou processamento de grandes volumes de dados. O uso de bloqueios (locks) e a gestão de estado garantem que as tarefas sejam manipuladas corretamente mesmo em ambientes de concorrência.

Funções Incluídas:
- start_simulation: Recebe uma requisição para iniciar uma tarefa de simulação, verifica o estado atual e, se ocioso, inicia a tarefa solicitada em um thread separado.
- get_simulation_status: Fornece o status atual da simulação, permitindo que clientes verifiquem se uma tarefa está em andamento, ociosa ou concluída.
- reset_simulation: Permite resetar o status da simulação para um estado inicial, preparando o sistema para uma nova tarefa.
- run_walker: Função que executa a tarefa assíncrona propriamente dita, usando o algoritmo selecionado para processar os dados fornecidos.

"""

executor = ThreadPoolExecutor(2)
status_lock = Lock()
status = {"state": "idle", "result": None}

def start_simulation(request):
    """
    Inicia uma simulação de caminhada utilizando os parâmetros fornecidos na solicitação.

    A função verifica se já existe uma simulação em andamento. Se não houver, ela extrai
    os parâmetros da solicitação JSON e submete a tarefa ao executor para execução assíncrona.
    O estado da simulação é atualizado para "running" enquanto a simulação está em progresso.

    Args:
        request (flask.Request): A solicitação HTTP contendo os parâmetros da simulação no formato JSON.
            Os parâmetros esperados são:
                - select_algo (str): O algoritmo selecionado para a simulação.
                - readers (int): O número de leitores.
                - time_readings (int): O tempo de leitura em cada ponto.
                - hours_work (int): As horas de trabalho diárias.
                - total_days (int): O total de dias de simulação.

    Returns:
        flask.Response: Uma resposta HTTP indicando o status da submissão da tarefa.
            - 202 Accepted: Se a tarefa foi submetida com sucesso.
            - 409 Conflict: Se uma simulação já está em progresso.

    Notas:
        - A função utiliza um bloqueio (`status_lock`) para garantir que o estado da simulação não seja modificado
          simultaneamente por múltiplas threads.
        - O executor é configurado para permitir um máximo de 2 threads concorrentes.
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

def get_simulation_status():
    """
    Retorna o status atual da simulação.

    Returns:
        Response: Objeto de resposta Flask com o status atual da simulação em formato JSON.
    """
    return jsonify(status)

def reset_simulation():
    """
    Reseta o status da simulação para o estado inicial.

    Returns:
        str: Mensagem indicando que a tarefa foi resetada.
    """
    status["state"] = "idle"
    status["result"] = None
    return "Task reset!"

def run_walker(select_algo, readers, time_readings, hours_work, total_days):
    """
    Executa a tarefa de simulação utilizando o algoritmo selecionado e a lista de leitores.

    Args:
        select_algo (str): Nome do algoritmo selecionado.
        readers (list): Lista de leitores para serem processados pelo algoritmo.

    Side Effects:
        Atualiza o status da simulação para 'finished' e armazena o resultado ou a mensagem de erro.
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
