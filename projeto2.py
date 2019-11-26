import _thread
import threading as _
class conta:
    def __init__(self,nome="",saldo=0):
        self.nome = nome
        self.saldo = saldo
    def get_nome(self):
        return self.nome
    def get_saldo(self):
        return self.saldo
    def transference(self, valor_transferencia,conta2,x):
        x.acquire()
        try:
            if self.saldo >= valor_transferencia:
                self.saldo = self.saldo - valor_transferencia
                conta2.saldo = conta2.saldo + valor_transferencia
                print(self.saldo, self.nome)
                print(conta2.saldo,conta2.nome,"\n")
            else:
                print(self.nome,'nao tem dinheiro\n')
        finally:
            x.release()

if __name__ == '__main__':
    contaA = conta("João", 100)
    contaB = conta("Maria", 0)


    trava=_.Lock()


    print(contaA.get_saldo(), contaA.get_nome())
    print(contaB.get_saldo(), contaB.get_nome(),'\n')


    for i in range (100):
        thread = _.Thread(target=contaA.transference, args=(10, contaB, trava))
        thread.start()
        thread = _.Thread(target=contaB.transference, args=(10, contaA, trava))
        thread.start()


      #  th.append(_thread.start_new_thread(contaB.transference, (10, contaA, trava)))
      #  th.append(_thread.start_new_thread(contaA.transference, (10, contaB, trava)))
