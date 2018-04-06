from disciplina import Disciplina
from professor import Professor
from alunos import Aluno


p1 = Professor(nome='Fernando', ra='123456')
p2 = Disciplina(nome='LP2', cargaHoraria=80, mensalidade=200, professor=p1)

p1.adicionaDisciplina(p2)

al = Aluno(nome = 'alvaro',email='alvi._alvaro@hotmail.com',ra='1701718',celular ='11952210677',desconto = 10)
al.adicionaDisciplina(p2)
al.adicionaDisciplina(Disciplina(nome='LP3', cargaHoraria=40, mensalidade=120, professor=p1))

print(al.retornaCargaHoraria())
print(al.retornaValorMensalidade())

