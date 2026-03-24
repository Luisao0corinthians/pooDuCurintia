class Instituição: 
    def __init__(self, nomeCampus, cidadeCampus ):
        self.nomeCampus = ""
        self.cidadeCampus = ""
        
    def __str__(self):
        return f"Instituição: {self.nomeCampus}"
    
class Estudante:
    def __init__(self, nomeEstud, dtNascimento, cpf):
        self.nomeEstud = ""
        self.dtNascimento = ""
        self.cpf = ""

    def __str__(self):
        return f"Estudante: {self.nomeEstud}"
    
    def apresentar(self):
        print(f"O {self.nomeEstud}, nasceu em {self.dtNascimento} e possui o cpf: {self.cpf}")
        if(self.cpf == ""):
            print("O estudante não cadastrou cpf")
        else:
            print("cpf", self.cpf[0:3], ". . .")
    

luis = Estudante()
luis.nomeEstud = "Luís Rafael"
luis.dtNascimento = "26/03/2009"
luis.cpf = "120.531.839-93"
print(f"o {luis.nomeEstud}, nasceu em {luis.dtNascimento} e possui o cpf: {luis.cpf}")

ifprparanavaí = Instituição()
ifprparanavaí.nomeCampus = "Instituto federal do Paraná - campus Paranavaí"
ifprparanavaí.cidadeCampus = "Paranavaí"



