from ControleDeTemperatura import ControleTemperatura

class ConfiguracaoControlador(ControleTemperatura):
    def __init__(self):
        super().__init__()
    
    def Opcao(self):

        print("""
            [1] Enviar número para o controlador de temperatura
            [2] Verificar a temperatura do controlador de temperatura
            [3] Configurar a histerese
            """)
        
        while True:
            NumOpcao = input("Digite uma das opções acima:")
            try:
                if NumOpcao.isnumeric() and NumOpcao in ['1','2','3']:
                    IntNumOpcao = int(NumOpcao)
                    
                    if IntNumOpcao == 1:
                        while True:
                            Number = input("Digite um número para enviar para o controlador de temperatura: ")
                            if Number.isnumeric():
                                    self.SendMsgForControlador(Number)
                                    break

                            else:
                                print("Digite um número válido!")
                        break

                    elif IntNumOpcao == 2:
                        self.ReadTempControlador()
                        print(ConfigControlador.Resposta)
                        break
                    
                    elif IntNumOpcao == 3:
                        while True:
                            Histerese = input("Digite um valor entre 0.1 à 50 para a histerese: ").replace(',','.')
                            try:
                                NumHisterese = float(Histerese)
                                if 0.1 <= NumHisterese <= 50:
                                    self.WriteInHisteria(NumHisterese)
                                    break
                                else:
                                    print(f"Por favor, digite um número entre 0.1 e 50!")
                            except ValueError:
                                    print("Por favor, digite um número válido!")
                        break
                    
                else:
                    print("Digite uma opção válida!")
            
            except:
                return f"Houve um erro! Por favor, tente novamente."


if __name__ == "__main__":
    ConfigControlador = ConfiguracaoControlador()
    ConfigControlador.Opcao()
        