
import threading as _  #biblioteca usada para importar as threads.
class conta:
    def __init__(self,nome="",saldo=0):
        self.nome = nome
        self.saldo = saldo
    def transference(self, valor_transferencia,conta2,trava): #criamos um def para realizar as transferencias entre contas. Essa função é chamda pela conta que ira enviar o dinhero, essa função também
                                                              # recebe o valor de transferencia, a conta que ira receber o dinheiro e a variavel onde está a trava(lock).
        trava.acquire() #controla o acesso restringindo o uso a uma thread.
        try:
            if self.saldo >= valor_transferencia:
                self.saldo = self.saldo - valor_transferencia
                conta2.saldo = conta2.saldo + valor_transferencia
                print(self.saldo, self.nome)
                print(conta2.saldo,conta2.nome,"\n")
            else:
                print(self.nome,'nao tem dinheiro\n')
        finally:
            trava.release() #libera o acesso para as outra thread.

if __name__ == '__main__':
    contaA = conta("João", 100)
    contaB = conta("Maria", 0)


    trava=_.Lock() #variavel que armazena o lock.


    print(contaA.saldo, contaA.nome)
    print(contaB.saldo, contaB.nome,'\n')


    for i in range (100):
        thread = _.Thread(target=contaA.transference, args=(10, contaB, trava)) #chama a função transference usando a conta que ira enviar o dinheiro  e passa pra ela os valores da transferencia,
                                                                                #a conta que ira receber e a variavel que armazena o lock.
        thread.start()
        thread = _.Thread(target=contaB.transference, args=(10, contaA, trava))
        thread.start()
        thread = _.Thread(target=contaA.transference, args=(10, contaB, trava))
        thread.start
        thread = _.Thread*target=contaB. transference, args=(10,contaA, trava))
        thread.start
