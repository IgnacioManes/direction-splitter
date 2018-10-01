# -*- coding: utf-8 -*-
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
        # self.calle = eliminaCaracteresEspeciales(self.calle)
        # self.calle = corregirAcentosF(self.calle)


class DireccionCompleja(Direccion):
    @staticmethod
    def has_numbers(input_string):
        return any(char.isdigit() for char in input_string)

    def analize_depto(self):
        array_calle = self.calle.split(' ')
        if (array_calle[-1].isalpha() and len(array_calle[-1]) == 1) or (array_calle[-2].isalpha() and len(array_calle[-2]) == 1):
            self.datoExtra = array_calle[-2] + " " + array_calle[-1]
            array_calle.pop()
            array_calle.pop()
            self.calle = ""
            for field in array_calle:
                if self.calle == "":
                    self.calle = field
                else:
                    self.calle += " " + field

    def get_puntaje(self,altura,posc):
        puntaje = 10
        if posc != len(self.direccion) - 1:
            posterior = self.direccion[posc+1]
        else:
            posterior = ""
        anterior = self.direccion[posc-1]
        if anterior in ("av", "av.", "avenida", "de", "pb", "calle") :
            puntaje -= 7
        if posterior.isalpha() and len(posterior) == 1:
            puntaje -= 4
        if anterior.isnumeric():
            puntaje -= 3
        if posterior == "":
            puntaje -= 1
        print "----result----"
        print "altura: "+altura
        print "post: "+posterior
        print "ant: "+anterior
        print "ptje: "+str(puntaje)
        return puntaje

    def comparar_alturas(self,candidato,posc_candidato,posc_altura):
        if candidato.isnumeric():
            if self.altura != "":
                if self.get_puntaje(candidato,posc_candidato) > self.get_puntaje(self.altura,posc_altura):
                    return True
            else:
                return True
        return False

    def procesar_direcc(self):
        print "calle compleja"
        primer_iteracion = True
        posc = 0
        posible_calle = ""
        posc_altura=0
        for field in self.direccion:
            es_calle = True
            if not primer_iteracion and self.has_numbers(field) and not field.isnumeric():
                self.datoExtra = field
                es_calle = False
            if not primer_iteracion and self.comparar_alturas(field, posc, posc_altura):
                if self.altura != "":
                    self.calle = posible_calle
                    posible_calle += " " + field
                    es_calle = False
                self.altura = field
                posc_altura = posc
            if primer_iteracion:
                self.calle += " " + field
                posible_calle += " " + field
                primer_iteracion = False
                es_calle = False
            if es_calle:
                self.calle += " " + field
                posible_calle += " " + field
            posc += 1
        self.analize_depto()


class DireccionSimple(Direccion):

    def procesar_direcc(self):
        print "calle simple"
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


direcc = Direccionador(u"7 de septiembre de 1998 123 2 b")
print direcc.procesar_direccion()
