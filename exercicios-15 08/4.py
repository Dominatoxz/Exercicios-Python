print("Seja Bem-vindo ao Banco")
class Banco:

    def _init_(self, cliente):
        self.cliente = cliente

    
    def adicionar(self):
        self.cliente = input("Digite seu nome para que eu possa adiciona-lo na nossa lista de clientes: ")
        print("Vou encaminha-lo para listagem")
    
        
    def listar(self):
        clientes = []
        print("Você está aprovado para ser nosso cliente")
        clientes.append(self.cliente)
        print(f"A lista de clientes é {clientes}")

banco = Banco()
banco.adicionar()
banco.listar()

        