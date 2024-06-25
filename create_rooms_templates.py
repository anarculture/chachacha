import os

# Set project directory
project_dir = '/home/anarculture/code/anarculture/chachacha/hotel_pms'
os.chdir(project_dir)

# Define templates content for rooms app
rooms_templates = {
    'rooms/templates/rooms/room_list.html': """\
<!DOCTYPE html>
<html>
<head>
    <title>Habitaciones</title>
</head>
<body>
    <h1>Habitaciones</h1>
    <a href="{% url 'room_create' %}">Crear nueva habitación</a>
    <ul>
        {% for room in rooms %}
            <li>
                <a href="{% url 'room_detail' room.pk %}">{{ room.numero }}</a>
                <a href="{% url 'room_update' room.pk %}">Editar</a>
                <a href="{% url 'room_delete' room.pk %}">Eliminar</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
""",
    'rooms/templates/rooms/room_detail.html': """\
<!DOCTYPE html>
<html>
<head>
    <title>Detalle de la Habitación</title>
</head>
<body>
    <h1>Detalle de la Habitación</h1>
    <p>Número: {{ room.numero }}</p>
    <p>Tipo de habitación: {{ room.tipo_habitacion }}</p>
    <p>Está disponible: {{ room.esta_disponible }}</p>
    <a href="{% url 'room_update' room.pk %}">Editar</a>
    <a href="{% url 'room_delete' room.pk %}">Eliminar</a>
</body>
</html>
""",
    'rooms/templates/rooms/room_form.html': """\
<!DOCTYPE html>
<html>
<head>
    <title>Formulario de Habitación</title>
</head>
<body>
    <h1>Formulario de Habitación</h1>
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Guardar</button>
    </form>
</body>
</html>
""",
    'rooms/templates/rooms/room_confirm_delete.html': """\
<!DOCTYPE html>
<html>
<head>
    <title>Confirmar Eliminación</title>
</head>
<body>
    <h1>Confirmar Eliminación</h1>
    <p>¿Estás seguro de que quieres eliminar la habitación "{{ room.numero }}"?</p>
    <form method="post">
        {% csrf_token %}
        <button type="submit">Confirmar</button>
    </form>
</body>
</html>
"""
}

# Create directories and files for templates
for path, content in rooms_templates.items():
    full_path = os.path.join(project_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

print("Templates for the rooms app have been created.")
