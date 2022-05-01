from sqlite3 import Fecha


class Cama:
    __idCama = 0
    __habitacion = ''
    __estado = False
    __diagnostico = ''
    __fecha_inter = Fecha
    __fecha_alta = Fecha

    def __init__(self, id, hab, est, diag, fi, fa):
        self.__idCama = id
        self.__habitacion = hab
        self.__estado = est
        self.__diagnostico = diag
        self.__fecha_inter = fi
        self.__fecha_alta = fa

    def __str__(self) -> str:
        return(f'{self.__idCama}\t{self.__habitacion}\t{self.__estado}\t{self.__diagnostico}\t{self.__fecha_inter}\t{self.__fecha_alta}\t')
