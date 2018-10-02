# -*- coding: utf-8 -*-


def corregirNombreDireccion(nombre):
    nombre = nombre.lower()
    # nombre = eliminaNumeros(nombre)
    nombre = eliminaCaracteresEspeciales(nombre)
    # nombre = self.corregirAcentos(nombre)
    nombre = nombre.encode('utf8')

    nombre = corregirAcentosF(nombre)
    nombre = nombre.capitalize()
    while '  ' in nombre:
        nombre = nombre.replace('  ', ' ')
    nombre = nombre.lstrip(' ')
    spliteo = nombre.split(' ')
    nombre = ''
    for a in spliteo:
        nombre = nombre + a.capitalize() + ' '
    nombre = nombre[0:len(nombre) - 1]
    # print nombre.decode('utf8')

    return nombre


def eliminaCaracteresEspeciales(palabra):  # Elimina los caracteres especiales como $&/()...
    for letra in palabra:
        if not letra.isalnum() and letra <> " ":
            palabra = palabra.replace(letra, "")
    return palabra


def corregirAcentosF(cadena):  # Remplaza en campos como nombre y apellido las letras con acento por sin acento
    try:
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('è', "e")
        cadena = cadena.replace('ì', "i")
        cadena = cadena.replace('ò', "o")
        cadena = cadena.replace('ù', "u")
        cadena = cadena.replace('á', "a")
        cadena = cadena.replace('é', "e")
        cadena = cadena.replace('í', "i")
        cadena = cadena.replace('ó', "o")
        cadena = cadena.replace('ú', "u")
        cadena = cadena.replace('â', "a")
        cadena = cadena.replace('ê', "e")
        cadena = cadena.replace('î', "i")
        cadena = cadena.replace('ô', "o")
        cadena = cadena.replace('û', "u")
        cadena = cadena.replace('ä', "a")
        cadena = cadena.replace('ë', "e")
        cadena = cadena.replace('ï', "i")
        cadena = cadena.replace('ö', "o")
        cadena = cadena.replace('ü', "u")
        cadena = cadena.replace('ð', "o")
        cadena = cadena.replace('õ', "o")
        cadena = cadena.replace('ç', "c")
        cadena = cadena.replace('ē', "e")
        cadena = cadena.replace('ę', "e")
        cadena = cadena.replace('å', "a")
        cadena = cadena.replace('ã', "a")
        cadena = cadena.replace('æ', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('à', "a")
        cadena = cadena.replace('ñ', "n")
    except:
        print 'rompe'
        cadena = ''
    return cadena


def corregirAcentos(cadena):  # Remplaza en campos como nombre y apellido las letras con acento por sin acento
    nueva_cadena = ''
    try:
        cadena = cadena.encode('utf8')

        print cadena
        d = {'\xed': 'i', '\xf3': 'o', '\xf1': 'n', '\xe7': 'c', '\xba': '', '\xb0': '', '\x3a': '', '\xe1': 'a',
             '\xe2': 'a', '\xe3': 'a', '\xe4': 'a', '\xe5': 'a', '\xe8': 'e', '\xe9': 'e', '\xea': 'e', '\xeb': 'e',
             '\xec': 'i', '\xed': 'i', '\xee': 'i', '\xef': 'i', '\xf2': 'o', '\xf3': 'o', '\xf4': 'o', '\xf5': 'o',
             '\xf0': 'o', '\xf9': 'u', '\xfa': 'u', '\xfb': 'u', '\xfc': 'u', '\xe5': 'a', '\xf6': 'o', 'ó': 'o',
             'é': 'e', 'á': 'a', 'ú': 'u', 'í': 'i', 'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u', 'â': 'a',
             'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u', 'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u', 'í': 'i',
             'í': 'æ', 'a': 'ç', 'c': 'ã', 'a': 'å', 'ą': 'a', 'õ': 'o', 'ð': 'o'}
        ##d = {'\00c0':'a','\00e8':'e','\u00ec':'i','\00f2':'o','\00f9':'u'}
        print 'Crudo'
        nueva_cadena = cadena
        for c in d.keys():
            nueva_cadena = nueva_cadena.replace(c, d[c])
    except:
        print 'rompe'
        pass
    return nueva_cadena


class Direccion(object):
    def __init__(self, array_direccion):
        self.direccion = array_direccion
        self.altura = ""
        self.calle = ""
        self.datoExtra = ""
        self.localidad = ""

    def get_data(self):
        return {'Direccion': self.calle, 'Extra': self.datoExtra, 'Altura': self.altura, 'Localidad': self.localidad}

    def emprolijar_data(self):
        self.calle = self.calle.lower()
        self.calle = self.calle.encode('utf8')
        self.calle = eliminaCaracteresEspeciales(self.calle)
        self.calle = corregirAcentosF(self.calle)


class DireccionCompleja(Direccion):
    @staticmethod
    def has_numbers(input_string):
        return any(char.isdigit() for char in input_string)

    @staticmethod
    def concatenar_string(str1, str2):
        if str1 == "":
            str1 = str2
        else:
            str1 += " " + str2
        return str1

    @staticmethod
    def analize_field(field):
        return field.lower() in ("casa", "bis", "nro", "esq", "s/n", "pb", "e", "y")

    def analize_depto(self):
        array_calle = self.calle.split(' ')
        ultimo = array_calle[-1]
        anteultimo = array_calle[-2]
        if ((ultimo.isalpha() and len(ultimo) == 1) or (anteultimo.isalpha() and len(anteultimo) == 1))\
                and (not self.analize_field(ultimo) and not self.analize_field(anteultimo)):
            self.datoExtra = self.concatenar_string(self.datoExtra, array_calle[-2] + " " + array_calle[-1])
            array_calle.pop()
            array_calle.pop()
            self.calle = ""
            for field in array_calle:
                self.calle = self.concatenar_string(self.calle, field)
        tiene_pb_or_E_or_y = False
        array_calle = self.calle.split(' ')
        self.calle = ""
        for field in array_calle:
            if self.analize_field(field) or tiene_pb_or_E_or_y:
                tiene_pb_or_E_or_y = True
                self.datoExtra = self.concatenar_string(self.datoExtra, field)
            else:
                self.calle = self.concatenar_string(self.calle, field)
        if field.lower() == "e" or field.lower() == "y":
            self.datoExtra = self.concatenar_string(self.datoExtra, self.altura)
            self.altura = ""

    def get_puntaje(self, altura, posc):
        puntaje = 10
        if posc != len(self.direccion) - 1:
            posterior = self.direccion[posc+1]
        else:
            posterior = ""
        anterior = self.direccion[posc-1]
        if anterior.lower() in ("av", "av.", "avenida", "de", "pb", "calle", "e", "y"):
            puntaje -= 7
        if posterior.isalpha() and len(posterior) == 1:
            puntaje -= 4
        if posterior == "":
            puntaje -= 1
        if anterior.isnumeric():
            puntaje += 1
        """print "----result----"
        print "altura: "+altura
        print "post: "+posterior
        print "ant: "+anterior
        print "ptje: "+str(puntaje)"""
        return puntaje

    def comparar_alturas(self, candidato, posc_candidato, posc_altura):
        if candidato.isnumeric():
            if self.altura != "":
                if self.get_puntaje(candidato,posc_candidato) > self.get_puntaje(self.altura, posc_altura):
                    return True
            else:
                return True
        return False

    def procesar_direcc(self):
        primer_iteracion = True
        posc = 0
        posible_calle = ""
        posc_altura=0
        saltear=False
        for field in self.direccion:
            es_calle = True

            if not saltear:

                if not primer_iteracion and self.has_numbers(field) and not field.isnumeric():
                    if posc != len(self.direccion) - 1 and self.direccion[posc+1].isalpha() \
                            and len(self.direccion[posc+1]) == 1:
                        self.datoExtra += field + self.direccion[posc+1]
                        saltear = True
                    else:
                        self.datoExtra += field
                    es_calle = False

                if not primer_iteracion and self.comparar_alturas(field, posc, posc_altura):
                    if self.altura != "":
                        self.calle = posible_calle
                        posible_calle += " " + field
                        es_calle = False
                    self.altura = field
                    posc_altura = posc

                if primer_iteracion:
                    self.calle = field
                    posible_calle += field
                    primer_iteracion = False
                    es_calle = False

                if es_calle:
                    self.calle += " " + field
                    posible_calle += " " + field

            elif saltear:
                saltear = False

            posc += 1
        self.analize_depto()


class DireccionSimple(Direccion):

    def procesar_direcc(self):
        for field in self.direccion:
            if len(field) > 0:
                if field.isnumeric():
                    self.altura = field
                else:
                    self.calle += " " + field


class Direccionador(object):
    def __init__(self, direccion):
        self.direccion = direccion

    @staticmethod
    def has_numbers(input_string):
        return any(char.isdigit() for char in input_string)

    @staticmethod
    def eliminar_espacios(string):
        string = string.replace('.', ' ')
        string = string.replace('  ', ' ')
        string = string.replace('  ', ' ')
        return string

    def definir_complejidad(self, array_direccion):
        contador = 0
        for campo in array_direccion:
            if self.has_numbers(campo):
                contador += 1
        if contador > 1:
            return DireccionCompleja(array_direccion)
        else:
            return DireccionSimple(array_direccion)

    def procesar_direccion(self):
        self.direccion = self.eliminar_espacios(self.direccion)
        array_localidad = self.direccion.split(',')
        array_direction = array_localidad[0].split(' ')
        direccion = self.definir_complejidad(array_direction)
        direccion.procesar_direcc()
        direccion.emprolijar_data()
        return direccion.get_data()


def printCalle(calle):
    print calle
    direcc = Direccionador(calle)
    print direcc.procesar_direccion()



