class Contacto:

    def __init__(self, nombre, apellido, direccion, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.telefonos = []
        self.palabras = []

    def darNombre(self):
         return self.nombre
    
    def darApellido(self):
        return self.apellido

    def darDireccion(self):
        return self.direccion
    
    def darCorreo(self):
        return self.correo
    
    def darTelefonos(self):
        return self.telefonos
    
    def darPalabras(self):
        return self.palabras
         
    def cambiarDireccion(self, Ndireccion):
        self.direccion = Ndireccion
        return "La direccion se ha actualizado" + self.direccion

    def cambiarCorreo(self, Ncorreo):
        self.correo = Ncorreo
        return "el correo se ha actualizado" + self.correo
     
    def agregarTelefono(self, telefono):
        self.telefonos.append(telefono)

    def eliminarTelefono(self, telefonoEliminar):
        self.telefonos.remove(telefonoEliminar)

    def agregarPalabra(self, palabra):
        self.palabras.append(palabra)

    def eliminarPalabra(self, palabraEliminar):
        self.palabras.remove(palabraEliminar)

    def contienePalabraClave(self, palabra):
        return palabra in self.palabras
    