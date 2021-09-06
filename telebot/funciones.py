import datetime

def asignador_de_fechas(fecha):
    date = datetime.datetime(
        int(fecha[0]),
        int(fecha[1]),
        int(fecha[2]),
        int(fecha[3]),
        int(fecha[4]),
        int(fecha[5]),
        int(fecha[6]))
    return date



	