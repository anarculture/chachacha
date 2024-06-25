import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Define templates content for each app
templates_content = {
    'users': {
        'list': """\
<!DOCTYPE html>
<html>
<head>
    <title>Usuarios</title>
</head>
<body>
    <h1>Usuarios</h1>
    <a href="{% url 'user_create' %}">Crear nuevo usuario</a>
    <ul>
        {% for user in users %}
            <li>
                <a href="{% url 'user_detail' user.pk %}">{{ user.username }}</a>
                <a href="{% url 'user_update' user.pk %}">Editar</a>
                <a href="{% url 'user_delete' user.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
""",
        'detail': """\
<!DOCTYPE html>
<html>
<head>
    <title>Detalle del Usuario</title>
</head>
<body>
    <h1>Detalle del Usuario</h1>
    <p>Nombre de usuario: {{ user.username }}</p>
    <p>Correo electrónico: {{ user.email }}</p>
    <p>Es empleado: {{ user.is_staff }}</p>
    <p>Es administrador: {{ user.is_admin }}</p>
    <p>Es huésped: {{ user.is_guest }}</p>
    <a href="{% url 'user_update' user.pk %}">Editar</a>
    <a href="{% url 'user_delete' user.pk %}">Eliminar</a>
</body>
</html>
""",
        'form': """\
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Usuario</title>
</head>
<body>
    <h1>Formulario de Usuario</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
""",
        'confirm_delete': """\
<!DOCTYPE html>
<html>
head>
    <title>Confirmar Eliminación</title>
</head>
<body>
    <h1>Confirmar Eliminación</h1>
    <p>¿Estás seguro de que quieres eliminar "{{ user.username }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirmar</button>
    </form>
</body>
</html>
"""
    },
    'reservations': {
        'list': """\
<!DOCTYPE html>
<html>
<head>
    <title>Reservaciones</title>
</head>
<body>
    <h1>Reservaciones</h1>
    <a href="{% url 'reservation_create' %}">Crear nueva reservación</a>
    <ul>
        {% for reservation in reservations %}
            <li>
                <a href="{% url 'reservation_detail' reservation.pk %}">{{ reservation.guest.username }} - {{ reservation.room.number }}</a>
                <a href="{% url 'reservation_update' reservation.pk %}">Editar</a>
                <a href="{% url 'reservation_delete' reservation.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
""",
        'detail': """\
<!DOCTYPE html>
<html>
<head>
    <title>Detalle de Reservación</title>
</head>
<body>
    <h1>Detalle de Reservación</h1>
    <p>Huésped: {{ reservation.guest.username }}</p>
    <p>Habitación: {{ reservation.room.number }}</p>
    <p>Fecha de entrada: {{ reservation.check_in_date }}</p>
    <p>Fecha de salida: {{ reservation.check_out_date }}</p>
    <p>Registrado: {{ reservation.checked_in }}</p>
    <a href="{% url 'reservation_update' reservation.pk %}">Editar</a>
    <a href="{% url 'reservation_delete' reservation.pk %}">Eliminar</a>
</body>
</html>
""",
        'form': """\
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Reservación</title>
</head>
<body>
    <h1>Formulario de Reservación</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
""",
        'confirm_delete': """\
<!DOCTYPE html>
<html>
<head>
    <title>Confirmar Eliminación</title>
</head>
<body>
    <h1>Confirmar Eliminación</h1>
    <p>¿Estás seguro de que quieres eliminar "{{ reservation.guest.username }} - {{ reservation.room.number }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirmar</button>
    </form>
</body>
</html>
"""
    },
    'billing': {
        'list': """\
<!DOCTYPE html>
<html>
<head>
    <title>Facturas</title>
</head>
<body>
    <h1>Facturas</h1>
    <a href="{% url 'invoice_create' %}">Crear nueva factura</a>
    <ul>
        {% for invoice in invoices %}
            <li>
                <a href="{% url 'invoice_detail' invoice.pk %}">{{ invoice.reservation.guest.username }} - {{ invoice.amount }}</a>
                <a href="{% url 'invoice_update' invoice.pk %}">Editar</a>
                <a href="{% url 'invoice_delete' invoice.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
""",
        'detail': """\
<!DOCTYPE html>
<html>
<head>
    <title>Detalle de Factura</title>
</head>
<body>
    <h1>Detalle de Factura</h1>
    <p>Reservación: {{ invoice.reservation.guest.username }} - {{ invoice.reservation.room.number }}</p>
    <p>Monto: {{ invoice.amount }}</p>
    <p>Pagado: {{ invoice.paid }}</p>
    <a href="{% url 'invoice_update' invoice.pk %}">Editar</a>
    <a href="{% url 'invoice_delete' invoice.pk %}">Eliminar</a>
</body>
</html>
""",
        'form': """\
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Factura</title>
</head>
<body>
    <h1>Formulario de Factura</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
""",
        'confirm_delete': """\
<!DOCTYPE html>
<html>
<head>
    <title>Confirmar Eliminación</title>
</head>
<body>
    <h1>Confirmar Eliminación</h1>
    <p>¿Estás seguro de que quieres eliminar la factura de "{{ invoice.reservation.guest.username }} - {{ invoice.amount }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirmar</button>
    </form>
</body>
</html>
"""
    },
    'reporting': {
        'list': """\
<!DOCTYPE html>
<html>
<head>
    <title>Reportes</title>
</head>
<body>
    <h1>Reportes</h1>
    <a href="{% url 'report_create' %}">Crear nuevo reporte</a>
    <ul>
        {% for report in reports %}
            <li>
                <a href="{% url 'report_detail' report.pk %}">{{ report.title }}</a>
                <a href="{% url 'report_update' report.pk %}">Editar</a>
                <a href="{% url 'report_delete' report.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
""",
        'detail': """\
<!DOCTYPE html>
<html>
<head>
    <title>Detalle del Reporte</title>
</head>
<body>
    <h1>Detalle del Reporte</h1>
    <p>Título: {{ report.title }}</p>
    <p>Contenido: {{ report.content }}</p>
    <a href="{% url 'report_update' report.pk %}">Editar</a>
    <a href="{% url 'report_delete' report.pk %}">Eliminar</a>
</body>
</html>
""",
        'form': """\
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Reporte</title>
</head>
<body>
    <h1>Formulario de Reporte</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
""",
        'confirm_delete': """\
<!DOCTYPE html>
<html>
head>
    <title>Confirmar Eliminación</title>
</head>
<body>
    <h1>Confirmar Eliminación</h1>
    <p>¿Estás seguro de que quieres eliminar "{{ report.title }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirmar</button>
    </form>
</body>
</html>
"""
    }
}

# Create directories and files for templates
for app, templates in templates_content.items():
    for template_name, content in templates.items():
        path = f'{app}/templates/{app}/{template_name}.html'
        full_path = os.path.join(project_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content)

print("Templates for each app have been created.")
