import _thread
import threading as _
class conta:
    def __init__(self,nome="",saldo=0):
        self.nome = nome
        self.saldo = saldo
    def transference(self, valor_transferencia,conta2,trava):
        global ct
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
                ct=ct+1
                trava.release()
ct=0
if __name__ == '__main__':
    contaA = conta("João", 100)
    contaB = conta("Maria", 0)
    trava=_.Lock()
    print(contaA.saldo, contaA.nome)
    print(contaB.saldo, contaB.nome,'\n')
    for a in range(50):
        _thread.start_new_thread(contaA.transference, (10, contaB,trava))
        _thread.start_new_thread(contaB.transference, (10, contaA,trava))
    while ct<100:
            pass
