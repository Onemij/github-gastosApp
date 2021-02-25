import datetime

def obtener_fecha(date_str = "Introduce una fecha o '0':"):
    '''Muestra por pantalla el texto que se le pasa o uno por defecto
    y devuelve la fecha que se introduce por teclado en formato DATE o 0 (int)'''
    if date_str == "0":
            date = 0
    else:
        try:
            date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        except:
            try:
                date = datetime.datetime.strptime(date_str, "%d/%m/%y")
            except:
                try:
                    date = datetime.datetime.strptime(date_str, "%d-%m-%y")
                except:
                    try:
                        date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
                    except:
                        try:
                            date = datetime.datetime.strptime(date_str, "%d.%m.%y")
                        except:
                            try:
                                date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
                            except:
                                input("No ha introducido una fecha válida, pulse una tecla para salir.")
                                return 
        if date > datetime.datetime.today(): date = datetime.datetime.today()
    return date

def obtener_fecha_terminal(st = "Introduce una fecha o '0':"):
    '''Muestra por pantalla el texto que se le pasa o uno por defecto
    y devuelve la fecha que se introduce por teclado en formato DATE o 0 (int)'''
    date_str = input(st)
    if date_str == "0":
            date = 0
    else:
        try:
            date = datetime.datetime.strptime(date_str, "%x")
        except:
            try:
                date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            except:
                try:
                    date = datetime.datetime.strptime(date_str, "%d-%m-%y")
                except:
                    try:
                        date = datetime.datetime.strptime(date_str, "%d-%m-%Y")
                    except:
                        try:
                            date = datetime.datetime.strptime(date_str, "%d.%m.%y")
                        except:
                            try:
                                date = datetime.datetime.strptime(date_str, "%d.%m.%Y")
                            except:
                                input("No ha introducido una fecha válida, pulse una tecla para salir.")
                                return 
        if date > datetime.datetime.today(): date = datetime.datetime.today()
    return date

def today_db(dias=0):
    '''Devuelve la fecha de hoy, con el formato DATE'''
    date = datetime.date.today() + datetime.timedelta(days=dias)
    return date
