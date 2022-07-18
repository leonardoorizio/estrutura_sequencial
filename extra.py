class Computador:
    def __init__(self,modelo,memoria_ram,placa_de_video):
        self.modelo = modelo
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def exibir_informacoes(self):
        print(self.modelo,self.memoria_ram,self.placa_de_video)

pc = Computador("acer","8gb","nvidia")
pc.exibir_informacoes() 