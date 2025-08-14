salario = float(input("Digite seu salario: "))
emprestimo = float(input("Qual o valor do emprestimo que o senhor(a) deseja? "))

if emprestimo > salario * (20/100):
    print("Emprestimo não concedido!")
else:
    print("Emprestimo concedido.") 