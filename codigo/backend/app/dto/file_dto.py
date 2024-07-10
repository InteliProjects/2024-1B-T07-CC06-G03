class FileResponseDTO:
    """
    Data Transfer Object (DTO) para encapsular a resposta do upload de arquivos.

    Atributos:
        sucesso (bool): Indica se a operação foi bem-sucedida.
        erro (str, opcional): Mensagem de erro em caso de falha na operação. O padrão é None.
        resultados (str, opcional): Mensagem de sucesso com detalhes da operação. O padrão é None.
    """

    def __init__(self, sucesso, erro=None, resultados=None):
        """
        Inicializa uma nova instância de FileResponseDTO.

        Args:
            sucesso (bool): Indica se a operação foi bem-sucedida.
            erro (str, opcional): Mensagem de erro em caso de falha na operação.
            resultados (str, opcional): Mensagem de sucesso com detalhes da operação.
        """
        self.sucesso = sucesso
        self.erro = erro
        self.resultados = resultados

    def to_dict(self):
        """
        Converte a instância de FileResponseDTO em um dicionário.

        Returns:
            dict: Um dicionário contendo os atributos da instância.
        """
        return {
            'sucesso': self.sucesso,
            'erro': self.erro,
            'resultados': self.resultados
        }
