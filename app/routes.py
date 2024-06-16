from flask import render_template, request, redirect, url_for, flash
from app import app, mysql
import calendar
from datetime import datetime, date, timedelta


@app.context_processor
def utility_processor():
    def custom_enumerate(seq, start=0):
        return enumerate(seq, start)
    return dict(enumerate=custom_enumerate)

def get_calendario(mes, año):
    # Obtener el primer día del mes y el número de días en el mes
    primer_dia = date(año, mes, 1)
    dias_del_mes = (primer_dia + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    # Calcular el primer día de la semana del primer día del mes
    primera_semana = primer_dia.weekday()
    inicio_semana = primer_dia - timedelta(days=primera_semana)

    calendario = {
        'month_name': {
            1: 'Enero',
            2: 'Febrero',
            3: 'Marzo',
            4: 'Abril',
            5: 'Mayo',
            6: 'Junio',
            7: 'Julio',
            8: 'Agosto',
            9: 'Septiembre',
            10: 'Octubre',
            11: 'Noviembre',
            12: 'Diciembre'
        },
        'day_name': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        'calendario_dias': [[] for _ in range(6)]
    }

    # Llenar el calendario con los días del mes
    dia_actual = inicio_semana
    for semana in calendario['calendario_dias']:
        for _ in range(7):
            if dia_actual.month == mes:
                semana.append(dia_actual.day)
            else:
                semana.append(None)
            dia_actual += timedelta(days=1)

    return calendario


# Ruta para la página principal
@app.route('/')
def index():

    # Conexión a la base de datos
    # Consultar la base de datos para obtener las notas del mes y año
    cursor = mysql.connection.cursor()
    
    # Obtener datos de la base de datos
    cursor.execute("SELECT `id`, `fecha`, `semana`, `dia`, `nota` FROM `notas`")
    notas = cursor.fetchall()

    # Cerrar la conexión
    cursor.close()
   
    # Procesar los datos para el calendario y las semanas
    mes_actual = datetime.now().month
    año_actual = datetime.now().year
    calendario = get_calendario(mes_actual, año_actual)

    # Crear una estructura de datos para las semanas y las notas
    semanas = [[] for _ in range(6)]  # Una lista de 6 semanas vacías
    notas_dict = {}  # Un diccionario para almacenar las notas por día

    for nota in notas:
        # Desempaquetar los datos de la nota
        id_nota, fecha, semana, dia, nota_texto = nota

        # Obtener el día del mes desde la fecha
        dia_mes = fecha.day

        # Agregar la nota al diccionario de notas
        notas_dict[dia_mes] = [id_nota, fecha, nota_texto]

        # Agregar el día al calendario de semanas
        semanas[(dia_mes - 1) // 7].append(dia_mes)

    return render_template('index.html', notas=notas, calendario=calendario, semanas=semanas, notas_dict=notas_dict)

@app.route('/add', methods=['POST'])
def add_note():
    dia = int(request.form['dia'])
    semana = int(request.form['semana'])
    mes = int(request.form['mes'])
    año = int(request.form['año'])
    nota = request.form['nota']
    fecha = datetime(año, mes, dia)
    
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO notas (fecha, semana, dia, nota) VALUES (%s, %s, %s, %s)", (fecha, semana, dia, nota))
    mysql.connection.commit()
    cur.close()
    
    flash('Nota agregada exitosamente')
    
    # Redirigir a la página index con los parámetros actualizados
    return redirect(url_for('index', mes=mes, año=año))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_note(id):
    if request.method == 'POST':
        dia = int(request.form['dia'])
        mes = int(request.form['mes'])
        año = int(request.form['año'])
        nota = request.form['nota']
        fecha = datetime(año, mes, dia)
        cur = mysql.connection.cursor()
        cur.execute("UPDATE notas SET fecha=%s, nota=%s WHERE id=%s", (fecha, nota, id))
        mysql.connection.commit()
        cur.close()
        flash('Nota actualizada exitosamente')
        return redirect(url_for('index', mes=mes, año=año))
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM notas WHERE id=%s", [id])
        note = cur.fetchone()
        cur.close()
        return render_template('update.html', note=note)

@app.route('/delete/<int:id>')
def delete_note(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT fecha FROM notas WHERE id=%s", [id])
    fecha = cur.fetchone()[0]
    cur.execute("DELETE FROM notas WHERE id=%s", [id])
    mysql.connection.commit()
    cur.close()
    flash('Nota eliminada exitosamente')
    return redirect(url_for('index', mes=fecha.month, año=fecha.year))
