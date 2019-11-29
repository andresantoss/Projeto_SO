import threading as _

class conta:

    def __init__(self,nome="",saldo=0):

        self.nome = nome

        self.saldo = saldo

    def transference(self, valor_transferencia,conta2,trava):



        trava.acquire()

        try:

            if self.saldo >= valor_transferencia:

                self.saldo = self.saldo - valor_transferencia

                conta2.saldo = conta2.saldo + valor_transferencia

                print(self.saldo, self.nome)

                print(conta2.saldo,conta2.nome,"\n")

            else:

                print(self.nome,'nao tem dinheiro\n')

        finally:

            trava.release()

    def thread (self,valor_de_transferencia,conta2,trava):

            thread = _.Thread(target=self.transference, args=(valor_de_transferencia, conta2, trava))

            thread.start()
            thread = _.Thread(target=conta2.transference, args=(valor_de_transferencia, self, trava))

            thread.start()


if __name__ == '__main__':

    contaA = conta("João", 100)

    contaB = conta("Maria", 0)

    trava=_.Lock()

    print(contaA.saldo, contaA.nome)

    print(contaB.saldo, contaB.nome,'\n')

    for a in range (10000):

        contaA.thread(10,contaB,trava)

