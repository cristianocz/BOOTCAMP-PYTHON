import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class ContaIterador:
    def __init__(self, contas):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        pass

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)








def menu():
    menu = """\n


    ****************** MENU *********************
    *                                           *
    *            [1]\tDepositar                 *
    *            [2]\tSacar                     *                  
    *            [3]\tExtrato8                  *
    *            [4]\tNova conta                *
    *            [5]\tListar contas             *
    *            [6]\tNovo usuário              *
    *                                           *
    *                                           *
    *            [9]\tSair                      *
    *                                           *
    *********************************************
    => """
    return input(textwrap.dedent(menu))

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return


    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


 #    if valor > 0:
 #        saldo += valor
 #        extrato += f"Depósito:\tR$ {valor:.2f}\n"
 #        print("\n=== Depósito realizado com sucesso! ===")
 #    else:
 #        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

 #    return saldo, extrato

def sacar(clientes):
#    excedeu_saldo = valor > saldo
#    excedeu_limite = valor > limite
#    excedeu_saques = numero_saques >= limite_saques
#    if excedeu_saldo:
#        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
#    elif excedeu_limite:
#        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
#    elif excedeu_saques:
#        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
#    elif valor > 0:
#        saldo -= valor
#        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
#        numero_saques += 1
#        print("\n=== Saque realizado com sucesso! ===")
#    else:
#        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
#    return saldo, extrato

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
 #   print("\n================ EXTRATO ================")
 #   print("Não foram realizadas movimentações." if not extrato else extrato)
 #   print(f"\nSaldo:\t\tR$ {saldo:.2f}")
 #   print("==========================================")

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_usuario(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    # TODO: atualizar a implementação para utilizar o gerador definido em Historico
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_usuario(clientes):

    cpf_digitado = input("Digite o CPF (apenas números): ")

    while not validar_cpf(cpf_digitado):
        print ("CPF inválido!")
        cpf_digitado = input("Digite o CPF (apenas números): ")
    
    usuario = filtrar_usuario(cpf_digitado, clientes)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf_digitado, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]
  
def criar_conta(numero_conta, clientes, contas):
    # cpf = input("Informe o CPF do cliente: ")

     # COLoCADO no programa o validador de cpf     
    cpf_digitado = input("Digite o CPF (apenas números): ")

    while not validar_cpf(cpf_digitado):
        print ("CPF inválido!")
        cpf_digitado = input("Digite o CPF (apenas números): ")
    cliente = filtrar_usuario(cpf_digitado, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
 #       linha = f"""\
 #           Agência:\t{conta['agencia']}
 #           C/C:\t\t{conta['numero_conta']}
 #           Titular:\t{conta['usuario']['nome']}
 #      """
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))        

def validar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Verifica o primeiro dígito verificador
    if int(cpf[9]) != digito1:
        return False

    # Calcula o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verifica o segundo dígito verificador
    if int(cpf[10]) != digito2:
        return False

    return True

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "6":
            criar_usuario(clientes)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
     
        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "9":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()