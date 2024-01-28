alunos = [
    {
    "nome":"Luciana",
    "dt_nascimento":"03/12/1980",
    "sexo":"F",
    "categoria":"Faixa Amarela"
    },
    {
    "nome":"Auridebson",
    "dt_nascimento":"10/07/1977",
    "sexo":"M",
    "categoria":"Faixa Amarela"
    }
]

for aluno in alunos:
    print(f"""
    {aluno["nome"]} - {aluno["dt_nascimento"]}
    """)