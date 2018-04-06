class Professor: 

    def __init__(self, nome='', email='', ra='',
                 celular=''):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__disciplinas = []

    #gets & sets
    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getRa(self):
        return self.__ra

    def setRa(self, ra):
        self.__ra = ra

    #fim

    def adicionaDisciplina(self, disciplina):
        if disciplina.getProfessor().getRa() == self.__ra:
            self.__disciplinas.append(disciplina)
        else:
            return 'Professor não associado a disciplina'
    
    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += (d.getCargaHoraria() / 20)
        return soma_carga

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])