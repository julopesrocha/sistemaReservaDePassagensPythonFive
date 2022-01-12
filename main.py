import logging

from Usuario import Usuario
from Rota import Rota


def msg_boas_vindas():
    print("**************************************")
    print("Sistema de Reserva de Passagens Aéreas")
    print("**************************************")


def cadastro():
    print("Cadastre-se e faça sua reserva!")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    cliente = Usuario(nome, cpf)
    return cliente


def get_rotas(self, r1, r2):
    self.log.info("Exibe Rotas")
    self.get_rota()
    r1.get_rota()
    r2.get_rota()


def nova_reserva(usuario):
    print(" **********************  Nova Reserva ***********************")
    passagem = input("Informe o número da passagem que gostaria reservar: ")

    if passagem == "1":
        usuario.reserva_passagem("1")
    elif passagem == "2":
        usuario.reserva_passagem("2")
    elif passagem == "3":
        usuario.reserva_passagem("3")
    else:
        print("Número inválido! Tente Novamente")

    menu(usuario)

def cancelar(usuario):
    print(" **********************  Cancelar Reserva ***********************")
    passagem = input("Informe o número da passagem que gostaria cancelar: ")

    if passagem in usuario.get_reservas:
        usuario.cancela_reserva(passagem)
    else:
        print("Número inválido! Tente Novamente")
    menu(usuario)


def menu(usuario):
    print(" **********************  Menu ***********************")
    passo = input("(1) Nova Reserva (2) Cancelar Reserva (3) Finalizar Operação: ")

    if passo == "1":
        nova_reserva(usuario)
    elif passo == "2":
        cancelar(usuario)
    elif passo == "3":
        print("\n Volte Sempre, {}!".format(usuario.get_nome))
    else:
        print("Número inválido! Tente Novamente")
        menu(usuario)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
        filename='./transacoes.log',
        filemode='w'
    )
    msg_boas_vindas()

    r1 = Rota("RJ", "SP", "21-08-2022", "1")
    r2 = Rota("PR", "RJ", "21-03-2022", "2")
    r3 = Rota("RJ", "ES", "05-01-2022", "3")

    get_rotas(r1, r2, r3)
    print("**************************************")

    usuario = cadastro()
    menu(usuario)
