import json
def filter_data_by_date_and_reader(day, reader):
    """
    Filtra os dados por dia e leiturista.

    Args:
        dia (int): O dia para filtrar os dados.
        leiturista (int): O ID do leiturista para filtrar os dados.

    Returns:
        list: Lista de dados filtrados.
    """
    with open('./output/detailed_data.json') as file:
        data = json.load(file)
    
    filtered_data = [entry for entry in data if entry['dia'] == str(day) and entry['leiturista'] == str(reader)]
    
    return filtered_data