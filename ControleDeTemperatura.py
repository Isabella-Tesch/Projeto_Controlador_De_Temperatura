from pymodbus.client import ModbusSerialClient

class ControleTemperatura():
    def __init__(self):
        self.client = ModbusSerialClient(port="COM6", baudrate=9600, bytesize=8, parity='N', stopbits=1)
    
    def SendMsgForControlador(self, Number):
        self.client.write_register(address=0, value=int(Number)*10, slave=31)

    def ReadTempControlador(self):
        self.Resposta = self.client.read_holding_registers(address=1, count=1, slave=31).registers[0]/10
        
    
    def WriteInHisteria(self, NumHisterese):
        self.client.write_register(address=8, value=int(NumHisterese * 10), slave=31) 
        try:
            ReadHisterese = self.client.read_holding_registers(address=8, count=1, slave=31)
            ValorLidoHisterese = ReadHisterese.registers[0]/10
            print(f"O valor da Histerese é: {ValorLidoHisterese}")

        except:
            print(f"Houve um erro ao ler a Histerese: {ReadHisterese.getErrorMessage()}")



if __name__ == "__main__":
    ClasseControlador = ControleTemperatura()

    ClasseControlador.ReadTempControlador()
    
    ClasseControlador.SendMsgForControlador()

    ClasseControlador.WriteInHisteria()


