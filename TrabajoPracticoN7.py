# Trabajo Practico N°7
# Axel Agustin Astorga Vecchio
# Comision martes - Virtual

class Alumno:
    def __init__(self, nombre, apellido, edad, notas=None, faltas=0, amonestaciones=0, direccion=""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas if notas else []
        self.faltas = faltas
        self.amonestaciones = amonestaciones
        self.direccion = direccion

    def agregar_nota(self, nota):
        """Agrega una nueva nota al registro de notas del alumno."""
        self.notas.append(nota)

    def asignar_falta(self):
        """Incrementa en uno el contador de faltas del alumno."""
        self.faltas += 1

    def asignar_amonestacion(self):
        """Incrementa en uno el contador de amonestaciones del alumno."""
        self.amonestaciones += 1

    def cambiar_direccion(self, nueva_direccion):
        """Cambia la dirección del alumno."""
        self.direccion = nueva_direccion

    def obtener_promedio(self):
        """Calcula y devuelve el promedio de notas del alumno."""
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def __str__(self):
        """Devuelve una representación en texto de los datos del alumno."""
        return (f"Nombre: {self.nombre} {self.apellido}\n"
                f"Edad: {self.edad} años\n"
                f"Notas: {self.notas}\n"
                f"Promedio: {self.obtener_promedio():.2f}\n"
                f"Faltas: {self.faltas}\n"
                f"Amonestaciones: {self.amonestaciones}\n"
                f"Dirección: {self.direccion}\n")

class RegistroAlumnos:
    def __init__(self, archivo="registro_alumnos.txt"):
        self.archivo = archivo

    def guardar_alumnos(self, alumnos):
        """Guarda la información de varios alumnos en el archivo de texto."""
        with open(self.archivo, "a") as file:
            for alumno in alumnos:
                file.write(str(alumno) + "\n")

    def cargar_alumnos(self):
        """Carga y muestra los alumnos registrados en el archivo."""
        try:
            with open(self.archivo, "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("No hay registros guardados.")

alumno1 = Alumno("Esteban", "Pérez", edad=15, notas=[8, 6, 10], direccion="España 210")
alumno2 = Alumno("Marcela", "Garnica", edad=16, notas=[7, 9, 9], direccion="Italia 190")
alumno3 = Alumno("Lucas", "Martínez", edad=14, notas=[6, 7, 10], direccion="Francia 789")

# Para modificar valores a los alumnos

alumno1.agregar_nota(0)
alumno1.asignar_falta()
alumno1.asignar_amonestacion()
alumno1.cambiar_direccion("Italia 220")

# Lista de alumnos
alumnos = [alumno1, alumno2, alumno3]

# Crear instancia de RegistroAlumnos y guardar la lista de alumnos
registro = RegistroAlumnos()
registro.guardar_alumnos(alumnos)

# Cargar y mostrar los alumnos guardados
print("Alumnos registrados:")
registro.cargar_alumnos()

"""Profe no se como hacer para que se registren los cambios unicamente y no vuelva a copiarse todos los datos de los demas alumnos"""