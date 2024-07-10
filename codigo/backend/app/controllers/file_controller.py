from flask import request
from app.dto.file_dto import FileResponseDTO
from app.services.file_service import FileService

"""
Este módulo define uma API para o upload de arquivos em uma aplicação Flask, utilizando serviços para validar, salvar e processar arquivos recebidos através de requisições HTTP. Ele integra verificações de segurança e validação de dados para garantir que apenas arquivos apropriados sejam aceitos e corretamente manipulados.

A função central, upload_file, gerencia a recepção e o processamento do arquivo enviado pelo usuário. Ela valida a presença e o tipo do arquivo, além de utilizar um serviço dedicado para verificar o conteúdo do arquivo, garantindo que esteja em conformidade com os requisitos do sistema.

Função incluída:
- upload_file: Recebe um arquivo via requisição HTTP, realiza a validação do mesmo e, se apropriado, o salva no servidor. A função retorna um dicionário que informa o resultado da operação, indicando sucesso ou falha, e em caso de falha, fornece uma mensagem de erro específica.

"""


file_service = FileService()

def upload_file():
    """
    Função para fazer upload de um arquivo via requisição HTTP.

    Returns:
        dict: Dicionário contendo o resultado da operação de upload do arquivo.
              Pode conter uma mensagem de sucesso ou de erro.
    """
    if 'file' not in request.files:
        return FileResponseDTO(sucesso=False, erro='Parte do arquivo ausente').to_dict()
    
    file = request.files['file']
    
    if file.filename == '':
        return FileResponseDTO(sucesso=False, erro='Arquivo não selecionado').to_dict()
    
    if file and file_service.allowed_file(file.filename):
        filename = file_service.secure_filename(file.filename)
        file_content = file.read().decode('utf-8')

        valid, message = file_service.validate_columns(file_content)
        if not valid:
            return FileResponseDTO(sucesso=False, erro=message).to_dict()

        try:
            file_service.save_file(filename, file_content)
            return FileResponseDTO(sucesso=True, resultados=f"Arquivo salvo como {filename}").to_dict()
        except Exception as e:
            return FileResponseDTO(sucesso=False, erro=str(e)).to_dict()

    return FileResponseDTO(sucesso=False, erro='Tipo de arquivo não permitido').to_dict()