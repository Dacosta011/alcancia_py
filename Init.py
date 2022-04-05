from Manager.GestorEmpresa import GestorEmpresa
from Manager.GestorModalidad import GestorModalidad
from Manager.GestorPrestamo import GestorPrestamo
from Manager.GestorSocio import GestorSocio


class Menu:
    def __init__(self):
        self.gestorEmpresa = GestorEmpresa()
        self.gestorModalidad = GestorModalidad()
        self.gestorPrestamo = GestorPrestamo()
        self.gestorSocio = GestorSocio()
        self.Menu()

    def Menu(self):
        print("""
            ---------------------------------Gestor tu alcancia preferida ---------------------------------
            1. Gestionar Empresas
            2. Gestionar Modalidades
            3. Gestionar Socios
            4. Gestionar Prestamos
            5. Salir
        """)
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            self.MenuEmpresa()
        elif opcion == "2":
            self.MenuModalidad()
        elif opcion == "3":
            self.MenuSocio()
        elif opcion == "4":
            self.MenuPrestamo()
        elif opcion == "5":
            exit()
        else:
            print("Opcion invalida")
            self.Menu()
    
    def MenuEmpresa(self):
        print("""
            ---------------------------------Gestionar Empresas ---------------------------------
            1. Agregar Empresa
            2. Modificar Empresa
            3. Eliminar Empresa
            4. Listar Empresas
            5. Buscar Empresa
            6. Volver
        """)
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre de la empresa: ")
            direc = input("Ingrese la direccion de la empresa: ")
            numEmp = int(input("Ingrese el numero de empleados de la empresa: "))
            convenio = int(input("Ingrese el convenio de la empresa: "))

            if type(nombre) is not str or type(direc) is not str or type(numEmp) is not int or type(convenio) is not int:
                print("Error: Datos invalidos")
                self.MenuEmpresa()
            else:
                if self.gestorEmpresa.createEmpresa(nombre, direc, numEmp, convenio):
                    print("Empresa agregada")
                else:
                    print("Error: No se pudo agregar la empresa")
                self.MenuEmpresa()

        elif opcion == "2":
            nombreAnt = input("Ingrese el nombre de la empresa que quiere modificar: ")
            nombre = input("Ingrese el nombre de la empresa: ")
            direc = input("Ingrese la direccion de la empresa: ")
            numEmp = int(input("Ingrese el numero de empleados de la empresa: "))
            convenio = int(input("Ingrese el convenio de la empresa: "))

            if type(nombre) is not str or type(direc) is not str or type(numEmp) is not int or type(convenio) is not int:
                print("Error: Datos invalidos")
                self.MenuEmpresa()
            else:
                if self.gestorEmpresa.updateEmpresa(nombreAnt,nombre, direc, numEmp, convenio):
                    print("Empresa modificada")
                else:
                    print("Error: No se pudo modificar la empresa")
                self.MenuEmpresa()

        elif opcion == "3":
            nombre = input("Ingrese el nombre de la empresa que quiere eliminar: ")
            if self.gestorEmpresa.deleteEmpresa(nombre):
                print("Empresa eliminada")
            else:
                print("Error: No se pudo eliminar la empresa")
            self.MenuEmpresa()
        elif opcion == "4":
            self.gestorEmpresa.allEmpresas()
            self.MenuEmpresa()
        elif opcion == "5":
            nombre = input("Ingrese el nombre de la empresa que quiere buscar: ")
            if self.gestorEmpresa.getEmpresa(nombre):
                print("Empresa encontrada")
            else:
                print("Error: No se pudo encontrar la empresa")
            self.MenuEmpresa()
        elif opcion == "6":
            self.Menu()
        else:
            print("Opcion invalida")
            self.MenuEmpresa()

    def MenuModalidad(self):
        print("""
            ---------------------------------Gestionar Modalidades ---------------------------------
            1. Agregar Modalidad
            2. Modificar Modalidad
            3. Eliminar Modalidad
            4. Listar Modalidades
            5. Buscar Modalidad
            6. Volver
        """)
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            id = int(input("Ingrese el id de la modalidad: "))
            nombre = input("Ingrese el nombre de la modalidad: ")
            plazo = int(input("Ingrese el plazo de la modalidad: "))
            tasa = float(input("Ingrese la tasa de la modalidad: "))

            if type(id) is not int or type(nombre) is not str or type(plazo) is not int or type(tasa) is not float:
                print("Error: Datos invalidos")
                self.MenuModalidad()
            else:
                if self.gestorModalidad.createModalidad(id, nombre, plazo, tasa):
                    print("Modalidad agregada")
                else:
                    print("Error: No se pudo agregar la modalidad")
                self.MenuModalidad()
        
        elif opcion == "2":
            idAnt = int(input("Ingrese el id de la modalidad que quiere modificar: "))
            id = int(input("Ingrese el id de la modalidad: "))
            nombre = input("Ingrese el nombre de la modalidad: ")
            plazo = int(input("Ingrese el plazo de la modalidad: "))
            tasa = float(input("Ingrese la tasa de la modalidad: "))

            if type(id) is not int or type(nombre) is not str or type(plazo) is not int or type(tasa) is not float:
                print("Error: Datos invalidos")
                self.MenuModalidad()
            else:
                if self.gestorModalidad.updateModalidad(idAnt, id, nombre, plazo, tasa):
                    print("Modalidad modificada")
                else:
                    print("Error: No se pudo modificar la modalidad")
                self.MenuModalidad()
        
        elif opcion == "3":
            id = int(input("Ingrese el id de la modalidad que quiere eliminar: "))
            if self.gestorModalidad.deleteModalidad(id):
                print("Modalidad eliminada")
            else:
                print("Error: No se pudo eliminar la modalidad")
            self.MenuModalidad()
        
        elif opcion == "4":
            self.gestorModalidad.allModalidades()
            self.MenuModalidad()
        
        elif opcion == "5":
            id = int(input("Ingrese el id de la modalidad que quiere buscar: "))
            if self.gestorModalidad.getModalidad(id):
                print("Modalidad encontrada")
            else:
                print("Error: No se pudo encontrar la modalidad")
            self.MenuModalidad()
        
        elif opcion == "6":
            self.Menu()
        
        else:
            print("Opcion invalida")
            self.MenuModalidad()

    def MenuSocio(self):
        print("""
            ---------------------------------Gestionar Socios ---------------------------------
            1. Agregar Socio
            2. Modificar Socio
            3. Eliminar Socio
            4. Listar Socios
            5. Buscar Socio
            6. Volver
        """)
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            id = int(input("Ingrese el id del socio: "))
            nombre = input("Ingrese el nombre del socio: ")
            direccion = input("Ingrese la direccion del socio: ")
            telefono = input("Ingrese el telefono del socio: ")
            cargo = input("Ingrese el cargo del socio: ")
            empresa = input("Ingrese el nombre de la empresa del socio: ")
        
            if type(id) is not int or type(nombre) is not str or type(direccion) is not str or type(telefono) is not str or type(cargo) is not str or type(empresa) is not str:
                print("Error: Datos invalidos")
                self.MenuSocio()
            else:
                if self.gestorSocio.createSocio(id, nombre, direccion, telefono, cargo, empresa):
                    print("Socio agregado")
                else:
                    print("Error: No se pudo agregar el socio")
                self.MenuSocio()
        
        elif opcion == "2":
            idAnt = int(input("Ingrese el id del socio que quiere modificar: "))
            id = int(input("Ingrese el id del socio: "))
            nombre = input("Ingrese el nombre del socio: ")
            direccion = input("Ingrese la direccion del socio: ")
            telefono = input("Ingrese el telefono del socio: ")
            cargo = input("Ingrese el cargo del socio: ")
            empresa = input("Ingrese el nombre de la empresa del socio: ")
        
            if type(id) is not int or type(nombre) is not str or type(direccion) is not str or type(telefono) is not str or type(cargo) is not str or type(empresa) is not str:
                print("Error: Datos invalidos")
                self.MenuSocio()
            else:
                if self.gestorSocio.updateSocio(idAnt, id, nombre, direccion, telefono, cargo, empresa):
                    print("Socio modificado")
                else:
                    print("Error: No se pudo modificar el socio")
                self.MenuSocio()
        
        elif opcion == "3":
            id = int(input("Ingrese el id del socio que quiere eliminar: "))
            if self.gestorSocio.deleteSocio(id):
                print("Socio eliminado")
            else:
                print("Error: No se pudo eliminar el socio")
            self.MenuSocio()
        
        elif opcion == "4":
            self.gestorSocio.allSocios()
            self.MenuSocio()
        
        elif opcion == "5":
            id = int(input("Ingrese el id del socio que quiere buscar: "))
            if self.gestorSocio.getSocio(id):
                print("Socio encontrado")
            else:
                print("Error: No se pudo encontrar el socio")
            self.MenuSocio()
        
        elif opcion == "6":
            self.Menu()
        
        else:
            print("Opcion invalida")
            self.MenuSocio()
        
    def MenuPrestamo(self):
        print("""
            ---------------------------------Gestionar Prestamos ---------------------------------
            1. Agregar Prestamo
            2. Modificar Prestamo
            3. Eliminar Prestamo
            4. Listar Prestamos
            5. Buscar Prestamo
            6. Volver
        """)
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            modalidad = int(input("Ingrese el id de la modalidad: "))
            socio = int(input("Ingrese el id del socio: "))
            prestamo = int(input("Ingrese el id del prestamo: "))
            fecha = input("Ingrese la fecha del prestamo: ")
            valor = int(input("Ingrese el valor del prestamo: "))
            cuota = int(input("Ingrese la cuota del prestamo: "))

            if type(modalidad) is not int or type(socio) is not int or type(prestamo) is not int or type(fecha) is not str or type(valor) is not int or type(cuota) is not int:
                print("Error: Datos invalidos")
                self.MenuPrestamo()
            else:
                if self.gestorPrestamo.createPrestamo(modalidad, socio, prestamo, fecha, valor, cuota):
                    print("Prestamo agregado")
                else:
                    print("Error: No se pudo agregar el prestamo")
                self.MenuPrestamo()
        
        elif opcion == "2":
            modalidadAnt = int(input("Ingrese el id de la modalidad que quiere modificar: "))
            socioAnt = int(input("Ingrese el id del socio que quiere modificar: "))
            prestamoAnt = int(input("Ingrese el monto del prestamo que quiere modificar: "))
            modalidad = int(input("Ingrese el id de la modalidad: "))
            socio = int(input("Ingrese el id del socio: "))
            prestamo = int(input("Ingrese el monto del prestamo: "))
            fecha = input("Ingrese la fecha del prestamo: ")
            valor = int(input("Ingrese el valor del prestamo: "))
            cuota = int(input("Ingrese la cuota del prestamo: "))

            if type(modalidad) is not int or type(socio) is not int or type(prestamo) is not int or type(fecha) is not str or type(valor) is not int or type(cuota) is not int:
                print("Error: Datos invalidos")
                self.MenuPrestamo()
            
            else:
                if self.gestorPrestamo.updatePrestamo(modalidadAnt, socioAnt, prestamoAnt, modalidad, socio, prestamo, fecha, valor, cuota):
                    print("Prestamo modificado")
                else:
                    print("Error: No se pudo modificar el prestamo")
                self.MenuPrestamo()
        
        elif opcion == "3":
            modalidad = int(input("Ingrese el id de la modalidad que quiere eliminar: "))
            socio = int(input("Ingrese el id del socio que quiere eliminar: "))
            prestamo = int(input("Ingrese el monto del prestamo que quiere eliminar: "))
            if self.gestorPrestamo.deletePrestamo(modalidad, socio, prestamo):
                print("Prestamo eliminado")
            else:
                print("Error: No se pudo eliminar el prestamo")
            self.MenuPrestamo()
        
        elif opcion == "4":
            self.gestorPrestamo.allPrestamos()
            self.MenuPrestamo()
        
        elif opcion == "5":
            modalidad = int(input("Ingrese el id de la modalidad que quiere buscar: "))
            socio = int(input("Ingrese el id del socio que quiere buscar: "))
            prestamo = int(input("Ingrese el monto del prestamo que quiere buscar: "))
            if self.gestorPrestamo.getPrestamo(modalidad, socio, prestamo):
                print("Prestamo encontrado")
            else:
                print("Error: No se pudo encontrar el prestamo")
            self.MenuPrestamo()
        
        elif opcion == "6":
            self.Menu()

m=Menu()
        


