import os
import io
import pandas as pd

class FileService:
    """
    Classe responsável por gerenciar operações relacionadas a arquivos, como validação,
    salvamento e verificação de permissões de extensão.

    Atributos:
        ALLOWED_EXTENSIONS (set): Extensões de arquivos permitidas.
        DATABASE_DIR (str): Diretório onde os arquivos serão salvos.
    """

    ALLOWED_EXTENSIONS = {'csv'}
    DATABASE_DIR = 'database'

    def __init__(self):
        """
        Inicializa uma nova instância de FileService.
        Cria o diretório de banco de dados se ele não existir.
        """
        if not os.path.exists(self.DATABASE_DIR):
            os.makedirs(self.DATABASE_DIR)

    def allowed_file(self, filename):
        """
        Verifica se a extensão do arquivo é permitida.

        Args:
            filename (str): Nome do arquivo a ser verificado.

        Returns:
            bool: True se a extensão for permitida, False caso contrário.
        """
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def secure_filename(self, filename):
        """
        Garante que o nome do arquivo seja seguro para ser salvo no sistema de arquivos.

        Args:
            filename (str): Nome original do arquivo.

        Returns:
            str: Nome seguro do arquivo.
        """
        from werkzeug.utils import secure_filename
        return secure_filename(filename)
    
    def validate_columns(self, file_content):
        """
        Valida se o conteúdo do arquivo possui as colunas esperadas.

        Args:
            file_content (str): Conteúdo do arquivo CSV.

        Returns:
            tuple: (bool, str) onde o primeiro valor indica se a validação foi bem-sucedida
                   e o segundo valor é uma mensagem de sucesso ou erro.
        """
        expected_columns = ["INDICE", "LATITUDE", "LONGITUDE", "CODIGO_ROTA", "SEQUENCIA", "LOGRADOURO", "NUMERO"]
        try:
            df = pd.read_csv(io.StringIO(file_content), delimiter=';')
            if list(df.columns) == expected_columns:
                return True, "Colunas validadas com sucesso"
            else:
                missing_columns = [col for col in expected_columns if col not in df.columns]
                return False, f"Colunas ausentes: {', '.join(missing_columns)}"
        except Exception as e:
            return False, f"Erro ao ler o arquivo: {str(e)}"

    def save_file(self, filename, file_content):
        """
        Salva o conteúdo do arquivo no diretório especificado após verificar se a extensão é permitida.

        Args:
            filename (str): Nome do arquivo a ser salvo.
            file_content (str): Conteúdo do arquivo a ser salvo.

        Returns:
            str: Caminho do arquivo salvo.

        Raises:
            ValueError: Se a extensão do arquivo não for permitida.
        """
        if self.allowed_file(filename):
            filename = self.secure_filename(filename)
            filepath = os.path.join(self.DATABASE_DIR, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(file_content)
            self.last_saved_filename = filename
            return filepath
        else:
            raise ValueError("Arquivo não permitido")