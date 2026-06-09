def se(condicao, valor_se_verdadeiro, valor_se_falso):
    
    return valor_se_verdadeiro if condicao else valor_se_falso

alunos = [
    ("João", 40),
    ("Maria", 60),
    ("José", 94),
    ("Pedro", 70),
    ("Ricardo", 91),
    ("Bruno", 56),
    ("Bruna", 54),
    ("Silas", 51),
    ("Patrícia", 36),
    ("Tatiana", 82),
    ("Roseane", 36),
    ("Rebeca", 62),
    ("Carlos", 65),
    ("Marcos", 73),
    ("Adriana", 91),
    ("Adriano", 32),
    ("Fabíola", 100)
]

print(f"{'Aluno':^15} {'Nota':^6} {'Situação':^12}")
print("-" *38)

for nome, nota in alunos: 
    situacao = se(nota >= 70, "Aprovado", se (nota >= 50, "Recuperação", "Reprovado"))

    print(f"{nome:15}  {nota:>6} {situacao:^12}")

print("-" *38)

print("\n --- Boletim ---")

aprovados = 0
recuperacao = 0
reprovados = 0

for nome, nota in alunos:
    situacao = se(nota >= 70, "Aprovado", se(nota >= 50, "Recuperação", "Reprovado"))

    if situacao == "Aprovado":
        aprovados +=1
    elif situacao == "Recuperação":
        recuperacao +=1
    else:
        reprovados +=1

#Exibe o resultado
print(f"Total de Aprovados: {aprovados}")
print(f"Total de Recuperação: {recuperacao}")
print(f"Total de Reprovados: {reprovados}")
