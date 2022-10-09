class Siswa:

    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def serang(self, lawan):
        print(self.name + ' Menyerang ' + lawan.name )
        lawan.diserang(self, self.power)
        
    def diserang(self, lawan, power_lawan):
        print(self.name + ' Diserang ' + lawan.name)
        power_diterima = power_lawan/self.armor
        print('Serangan terasa : ' + str(power_diterima))
        self.health -= power_diterima
        print('Health ' + self.name + ' Tersisa ' + str(self.health))


cina = Siswa('Kevin',100,20,10)
sunda = Siswa('Lingga',100,50,10)

cina.serang(sunda)
print("\n")
sunda.serang(cina)
cina.serang(sunda)
print("\n")
sunda.serang(cina)
cina.serang(sunda)
print("\n")
sunda.serang(cina)
cina.serang(sunda)
print("\n")
sunda.serang(cina)
cina.serang(sunda)
print("\n")
sunda.serang(cina)
cina.serang(sunda)
print("\n")
sunda.serang(cina)
