class aluno_modelo:
    def __init__(self):
        
        self.__id_hash = None #string
        self.__matricula_aluno = None #int
        self.__nome_aluno = None #string
        self.__turma = None #string
        self.__serie = None #int
        self.__matriculado = None #bool
        self.__email_aluno = None #string

    @property
    def id_hash(self):
        return self.__id_hash

    @id_hash.setter
    def id_hash(self, value):
        if value is None:
            raise ValueError("Id nulo")

        if not isinstance(value, str):
            raise TypeError("Id deve ser uma string")

        value = value.strip()
        self.__id = value


    @property
    def matricula_aluno(self):
        return self.__matricula_aluno

    @matricula_aluno.setter
    def matricula_aluno(self, value):
        if value is None:
            raise ValueError("Matrícula do aluno nula")

        if not isinstance(value, int):
            raise TypeError("Matrícula do aluno deve ser int")

        self.__matricula_aluno = value


    @property
    def nome_aluno(self):
        return self.__nome_aluno

    @nome_aluno.setter
    def nome_aluno(self, value):
        if value is None:
            raise ValueError("Nome do aluno nulo")

        if not isinstance(value, str):
            raise TypeError("Nome do aluno deve ser uma string")

        value = value.strip()
        self.__nome_aluno = value


    @property
    def turma(self):
        return self.__turma

    @turma.setter
    def turma(self, value):
        if value is None:
            raise ValueError("Turma nula")

        if not isinstance(value, str):
            raise TypeError("Turma deve ser uma string")

        value = value.strip()
        self.__turma = value


    @property
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, value):
        if value is None:
            raise ValueError("Série nula")

        if not isinstance(value, int):
            raise TypeError("Série deve ser int")

        self.__serie = value


    @property
    def matriculado(self):
        return self.__matriculado

    @matriculado.setter
    def matriculado(self, value):
        if value is None:
            raise ValueError("Matriculado nulo")

        if not isinstance(value, bool):
            raise TypeError("Matriculado deve ser bool")

        self.__matriculado = value


    @property
    def email_aluno(self):
        return self.__email_aluno

    @email_aluno.setter
    def email_aluno(self, value):
        if value is None:
            raise ValueError("Email do aluno nulo")

        if not isinstance(value, str):
            raise TypeError("Email do aluno deve ser uma string")

        value = value.strip()
        self.__email_aluno = value