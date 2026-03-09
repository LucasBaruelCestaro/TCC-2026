import aluno

class questao_modelo:
    def __init__(self):
        
        self.__id_hash = None
        self.__nome_responsavel = None
        self.__email_responsavel = None
        self.__aluno = None
        self.__telefone_responsavel = None

    @property
    def id_hash(self):
        return self.__id_hash
    
    @id_hash.setter
    def id_hash(self, value):
        if value is None:
            raise ValueError("Id hash nulo")
        
        if not isinstance(value, str):
            raise TypeError("Id deve ser uma string")
        
    @property
    def nome_responsavel(self):
        return self.__nome_responsavel

    @nome_responsavel.setter
    def nome_responsavel(self, value):
        if value is None:
            raise ValueError("Nome responsável nulo")

        if not isinstance(value, str):
            raise TypeError("Nome responsável deve ser uma string")

        value = value.strip()
        self.__nome_responsavel = value

    @property
    def email_responsavel(self):
        return self.__email_responsavel

    @email_responsavel.setter
    def email_responsavel(self, value):
        if value is None:
            raise ValueError("Email responsável nulo")

        if not isinstance(value, str):
            raise TypeError("Email responsável deve ser uma string")

        value = value.strip()
        self.__email_responsavel = value

    @property
    def aluno(self):
        return self.__aluno
    
    @aluno.setter
    def aluno(self, value):
        if not isinstance(value, aluno):
            raise ValueError("Aluno deve ser uma instância válida")
        return self.__aluno
    
    @property
    def telefone_responsavel(self):
        return self.__telefone_responsavel
    
    @telefone_responsavel.setter
    def telefone_responsavel(self, value):
        if value is None:
            raise ValueError("Telefone do responsável nulo")

        if not isinstance(value, str):
            raise TypeError("Telefone do responsável deve ser uma string")

        value = value.strip()
        self.__telefone_responsavel = value