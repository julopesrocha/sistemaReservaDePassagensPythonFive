import logging

class Usuario:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        self.__reservas = []
        print("\n {}, seu cadastro foi bem sucedido! \n".format(self.__nome))

        self.log = logging.getLogger(__name__)
        self.log.debug("Usuario inicializado")

    @property
    def get_nome(self):
        return self.__nome

    @property
    def get_cpf(self):
        return self.__cpf

    @property
    def get_reservas(self):
        self.log.info("Lista de reservas")
        return self.__reservas

    def exibe_reservas(self):
        self.log.info("Exibe lista de reservas")
        quantidade = self.__reservas.__len__()
        print("*********************** Reservas ***********************")
        print("Você possui {} reserva(s): ".format(quantidade))

        contador = 1
        for i in self.__reservas:
            print("- Viagem " + i)
            contador += 1

    def reserva_passagem(self, id_rota):
        self.log.info("Efetua reserva")
        self.__reservas.append(id_rota)
        print("Reserva concluída!")
        self.exibe_reservas()

    def cancela_reserva(self, id_rota):
        self.log.info("Cancela reserva")
        self.__reservas.remove(id_rota)
        print("Reserva cancelada!")
        self.exibe_reservas()