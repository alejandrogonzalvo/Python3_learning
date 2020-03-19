class pasajero:
    def _init_(self, codigo, nombre, precioTiquete, porcentaje_impuesto):
        self.codigo = codigo
        self.nombre = nombre
        self.precioTiquete = precioTiquete
        self.porcentaje_impuesto = porcentaje_impuesto
        self.total = (porcentaje_impuesto * precioTiquete) + precioTiquete #al precio neto del tiquete se le suma el porcentaje de impuestos

    def total_pagar(self):
            return total * 0.95 # Se le resta un 5% al total

    def _str_(self):
        b = f" Codigo: {self.codigo} Nombre: {self.nombre} Precio Tiquete: {self.precioTiquete}
    Porcentaje: {porcentaje_impuesto} Impuesto: {descuento} "
        return (b)


class pasajero_frecuente(pasajero):
    def _init_(self, codigo, nombre, precioTiquete, porcentaje_impuesto, descuento):
        super()._init_(codigo, nombre, precioTiquete, porcentaje_impuesto, descuento)
        self.cant_puntos = cant_puntos

    @property

    def cant_puntos(self):
        return "El pasajero tiene la siguiente cantidad de puntos " + str(self.cant_puntos)

    def total_pagar(self):
        return total * 0.8 #se le resta un 20% al total


class pasajero_no_frecuente (pasajero):
    def _init_(self, codigo, nombre, precioTiquete, porcentaje_impuesto, descuento):
        super()._init_(codigo, nombre, precioTiquete, porcentaje_impuesto, descuento)
        self.primer_vuelo = primer_vuelo

    @property

    def primer_vuelo(self):
        return "El pasajero compra este vuelo por primera vez. Codigo del vuelo " + str(self.codigo)


class vuelo:
    def __init__(self, numero, hora_salida, hora_llegada):
        self._numero = numero
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada


    def _str_(self):
        x = f"Numero: {self.numero} Hora salida: {self.hora_salida} Hora llegada
     {self.hora_llegada}"
        return(x)


class vuelo_comercial(vuelo):
    def __init__(self, numero, hora_salida, hora_llegada):
        super()._init_(numero, hora_salida, hora_llegada)
        self.pasajeros = pasajeros

    @property

    def pasajeros(self):
        return "El vuelo comercial tiene la siguiente cantidad de pasajeros " +
    str(self.pasajeros)
    def _str_(self):
        numpasa = super()._str_()+ "\n" + self.pasajeros()
        return numpasa

class vuelo_local(vuelo_comercial):
    def _init_(self, numero, hora_salida, hora_llegada, pasajeros):
        super()._init_(numero, hora_salida, hora_llegada, pasajeros)
        self.minimo_pasajeros = minimo_pasajeros
    @property
    def minimo_pasajeros (self):
        return "El vuelo local tiene un minimo de pasajeros de " + str(self.minimo_pasajeros)
    def _str_(self):
        minpasa = super()._str_() + "\n" + self.minimo_pasajeros()
        return minpasa

class vuelo_internacional(vuelo_comercial):
    def _init_ (self, numero, hora_salida, hora_llegada, pasajeros, minimo_pasajeros):
        super()._init_(numero, hora_salida, hora_llegada, pasajeros, minimo_pasajeros)
        self.pais_destino = pais_destino
    @property
    def pais_destino(self):
        return "El vuelo internacional tiene el siguiente destino " + str(self.pais_destino)
    def _str_(self):
        pades= super().str() + "\n" + self.pais_destino()
        return pades

class vuelo_carga(vuelo):
    def __init__(self, numero, hora_salida, hora_llegada):
        super()._init_(numero, hora_salida, hora_llegada)
        self.carga = carga
    @property
    def carga (self):
        return "El vuelo tiene una carga maxima permitida de " + str (self.carga)
    def _str_(self):
        maxcarga = super()._str_() + "\n" + self.carga
        return maxcarga
