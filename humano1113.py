print("actividad 9 clase humano")
print("dorle zuñiga mat: 22308051281113")
#zona de clases
class Humano1113():
    #zona de atributos
    edad=17
    genero=""
    fecha_birth=""
    colordeojos=""
    peso=0
    estatura=0
#zona funciones dentro de la clase
    def correr1113(self,n):
        print(f"{n} está corrindo ahhh....")
        
    def comer1113(self,n):
        print(f"{n} está comiendo ahhh....")
    
    def leer1113(self,n):
        print(f"{n} está leyendo ahhh....")
    
    def cocinar1113(self,n):
        print(f"{n} está cocinando ahhh....")

#zona de creación de objetos
Dorle=Humano1113()
Dorle.edad=17
Dorle.colordeojos="cafes"
Dorle.fecha_birth="agosto 26"
Dorle.genero="mujer"

melisco=Humano1113()
melisco.edad=34
melisco.colordeojos= "verdes"
melisco.fecha_birth="junio 26"
melisco.peso=80
melisco.estatura=178
#zona de usando objetos
print("Resultado para Dorle-------")
print(f"Edad: {Dorle.edad}")
print(f"color de ojos: {Dorle.colordeojos}")
print(f"nacimiento: {Dorle.fecha_birth}")
print(f"generp: {Dorle.genero}")
Dorle.correr1113("Dorle")
Dorle.leer1113("Dorle")
Dorle.cocinar1113("Dorle")
Dorle.comer1113("Dorle")


print("Resultado para melisco-------")
print(f"Edad: {melisco.edad}")
print(f"color de ojos: {melisco.colordeojos}")
print(f"nacimiento: {melisco.fecha_birth}")
print(f"peso: {melisco.peso}")
print(f"altura: {melisco.estatura}")
melisco.correr1113("Melisco")
melisco.leer1113("Melisco")
melisco.cocinar1113("Melisco")
melisco.comer1113("Melisco")





