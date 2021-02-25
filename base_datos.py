import sqlite3, fechas, datetime, os, time
from new_constants import switch_categories, switch_subcategories


conn = sqlite3.connect('movimientos.db')
c = conn.cursor()

def create_table():
    '''Inicializa la tabla de la base de datos, si no existe'''
    c.execute("CREATE TABLE IF NOT EXISTS balance(fecha TEXT, tipo TEXT, movimiento REAL, categoria TEXT, subcategoria TEXT);")

def get_movs(tipo, category, fecha_i="1950-01-01", fecha_f="date('now','+1 day')"):
    c.execute(f"SELECT movimiento, tipo, fecha, categoria FROM balance WHERE categoria = '{category}' AND fecha > {fecha_i} AND fecha < {fecha_f} ORDER BY fecha;")
    movs = []
    for mov in c.fetchall():
        if mov[1] == tipo:
            movs.append(mov)
    return movs

def get_saldo(fecha="date('now','+1 day')"):
    '''Devuelve el saldo que había en la fecha que se le ha indicado por parámetro o 
        el saldo del día de hoy si no se le pasa ninguna fecha
        - fecha: La fecha en la que se quiere el saldo ("hoy" por defecto).'''
    try:
        if fecha != "date('now','+1 day')":
            fecha = fechas.obtener_fecha(fecha).strftime("%Y-%m-%d")
    except:
        print("Error al formatear la fecha en get_saldo()")
        return 0.0
         
    c.execute(f"SELECT movimiento, tipo, fecha FROM balance WHERE fecha > '1950-01-01' AND fecha < {fecha};")
    saldo = 0.0
    for mov in c.fetchall():
        if mov[1] == "gasto":
            saldo = saldo - mov[0]
        else: 
            saldo = saldo + mov[0]

    return saldo

def get_total(tipo, category=None):
    '''Devuelve la suma de gastos, ingresos o devoluciones en el mes actual en función del parámetro que se le pase.
    - tipo: El tipo de movimiento del que se quiere obtener el total ("ingreso", "gasto", "devolución")
    '''
    category_str = ""

    if category:
        category_str = f"AND categoria = '{category}'"

    if tipo in ("ingreso", "gasto", "devolucion"):
        total = 0.0

        c.execute(f"SELECT movimiento, tipo, fecha, categoria, subcategoria FROM balance WHERE fecha >= date('now','start of month') AND fecha <= date('now','start of month','+1 month','-1 day') {category_str} ORDER BY fecha;")

        for mov in c.fetchall():
            if mov[1] == tipo:
                total = total + mov[0]
        return total
    else:
        print(f"Error al obtener el total de {tipo} del mes actual.")
        return None

def data_entry(date, mov_type, quantity, category, subcategory):
    '''Introduce en la base de datos una nueva fila.
    - Parámetros:
        - date: La fecha del movimiento, en formato adecuado para SQLite3, YYYY-MM-DD.
        - type: Tipo de movimiento (ingreso, gasto, devolucion).
        - quantity: Cantidad de dinero, siempre positivo.
        - category: Categoría del movimiento (ver new_constants.py).
        - subcategory: Subcategoría del movimiento (ver new_constants.py).
    - Devuelve:
        - None
    '''
    if quantity < 0:
        quantity = quantity * -1

    try:
        c.execute(f"INSERT INTO balance VALUES('{date}','{mov_type}','{quantity}','{category}','{subcategory}')")
        conn.commit()
    except:
        print("Ha habido un error con la base de datos.")

def close_db():
    '''Cierra la base de datos'''
    c.close()
    conn.close()