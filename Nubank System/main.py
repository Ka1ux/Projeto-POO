class Cliente:
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf
    def __str__(self):
        return f"Cliente({self.nome}, {self.cpf})"   


class Conta:
    def __init__(self,numero,saldo):
        self.numero = numero 
        self.saldo = saldo
    def __str__(self):
        return f"Conta({self.numero}, {self.saldo})" 

class ContaCorrente:
    def __init__(self,numero,saldo):
        self.numero = numero 
        self.saldo = saldo
    def __str__(self):
        return f"ContaCorrente({self.numero}, {self.saldo})"  

class ContaPoupanca:
    def __init__(self, numero, saldo):
        self.numero = numero 
        self.saldo = saldo    

    def __str__(self):
        return f"ContaPoupanca({self.numero}, {self.saldo})"   


#gabriel
#vinicius 

class Usuario:
    def __init__(self, id, nome, email, telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def _str_(self):
        return f"Usuário({self.id}, {self.nome})"

class Endereco:
    def __init__(self, id, rua, numero, cidade, estado):
        self.id = id
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def _str_(self):
        return f"Endereço({self.rua}, {self.numero})"



class Notificacao:
    def __init__(self, id, mensagem, tipo):
        self.id = id
        self.mensagem = mensagem
        self.tipo = tipo  

    def _str_(self):
        return f"Notificação({self.tipo})"



class Atendimento:
    def __init__(self, id, usuario, descricao, status):
        self.id = id
        self.usuario = usuario
        self.descricao = descricao
        self.status = status 

    def _str_(self):
        return f"Atendimento({self.id}, {self.status})"        


#Matheus 


class LimiteCartao:
    def __init__(self, id, nome_cliente, limite_total, gasto_atual):
        self.id = id
        self.cliente = nome_cliente
        self.total = limite_total
        self.gasto = gasto_atual
        self.disponivel = limite_total - gasto_atual

class HistoricoTransferencia:
    def __init__(self, id, data, valor, recebedor, tipo):
        self.id = id
        self.data = data
        self.valor = valor
        self.recebedor = recebedor
        self.tipo = tipo


cliente1 = Cliente("cliente1" , "000.000.000-20")
cliente2 = Cliente("cliente2" , "111.111.111-21")
cliente3 = Cliente("cliente3" , "222.222.222-22")
cliente4 = Cliente("cliente4" , "333.333.333-23")
cliente5 = Cliente("cliente5" , "444.444.444-24")

conta1 = Conta("00123456-1" , "1700")
conta2 = Conta("00123456-2" , "1800")
conta3 = Conta("12345.67-3" , "1900")
conta4 = Conta("12345.67-4" , "2000")
conta5 = Conta("00012345-5" , "2100")

contaC1 = ContaCorrente("00123456-1" , "2100")
contaC2 = ContaCorrente("00123456-2" , "2200")
contaC3 = ContaCorrente("00123456-3" , "2300")
contaC4 = ContaCorrente("00123456-4" , "2400")
contaC5 = ContaCorrente("00123456-5" , "2500")

contaP1 = ContaPoupanca("000543210-1" , "3300")
contaP2 = ContaPoupanca("000543210-2" , "3400")
contaP3 = ContaPoupanca("000543210-3" , "3500")
contaP4 = ContaPoupanca("000543210-4" , "3600")
contaP5 = ContaPoupanca("000543210-5" , "3700")


##gabriel
#vinicius

u1 = Usuario(1, "João Silva", "joao@email.com", "11999999999")
u2 = Usuario(2, "Maria Souza", "maria@email.com", "11988888888")
u3 = Usuario(3, "Carlos Lima", "carlos@email.com", "11977777777")
u4 = Usuario(4, "Ana Costa", "ana@email.com", "11966666666")
u5 = Usuario(5, "Pedro Alves", "pedro@email.com", "11955555555")

e1 = Endereco(1, "Rua A", 100, "São Paulo", "SP")
e2 = Endereco(2, "Rua B", 200, "Rio de Janeiro", "RJ")
e3 = Endereco(3, "Rua C", 300, "Belo Horizonte", "MG")
e4 = Endereco(4, "Rua D", 400, "Curitiba", "PR")
e5 = Endereco(5, "Rua E", 500, "Porto Alegre", "RS")

n1 = Notificacao(1, "Seu pedido foi enviado", "email")
n2 = Notificacao(2, "Nova mensagem recebida", "push")
n3 = Notificacao(3, "Pagamento aprovado", "sms")
n4 = Notificacao(4, "Atualização disponível", "push")
n5 = Notificacao(5, "Senha alterada com sucesso", "email")

a1 = Atendimento(1, u1, "Problema no login", "aberto")
a2 = Atendimento(2, u2, "Erro no pagamento", "fechado")
a3 = Atendimento(3, u3, "Dúvida sobre produto", "aberto")
a4 = Atendimento(4, u4, "Solicitação de reembolso", "fechado")
a5 = Atendimento(5, u5, "Alteração de dados", "aberto")

#Matheus 

cartao1 = LimiteCartao(1, "João Silva", 5000.0, 1200.0)
cartao2 = LimiteCartao(2, "Maria Oliveira", 2500.0, 2450.0)
cartao3 = LimiteCartao(3, "Carlos Souza", 10000.0, 0.0)
cartao4 = LimiteCartao(4, "Ana Costa", 1500.0, 800.0)
cartao5 = LimiteCartao(5, "Bruno Alves", 3000.0, 3100.0)

transf1 = HistoricoTransferencia(1, "20/03/2026", 150.0, "Mercado Central", "Pix")
transf2 = HistoricoTransferencia(2, "21/03/2026", 45.90, "Netflix", "Crédito")
transf3 = HistoricoTransferencia(3, "22/03/2026", 1200.0, "Aluguel", "TED")
transf4 = HistoricoTransferencia(4, "23/03/2026", 15.00, "Padaria Pão de Mel", "Débito")
transf5 = HistoricoTransferencia(5, "24/03/2026", 350.0, "Posto Combustível", "Crédito")
