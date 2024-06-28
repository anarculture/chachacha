import os

# Define the base path for the templates
BASE_DIR = 'hotel_pms/templates'

# Define the templates and their contents
templates = {
    'base.html': """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <title>{% block title %}Hotel Management System{% endblock %}</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">Hotel Management</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link" href="{% url 'reservation_list' %}">Reservations</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>
</body>
</html>
    """,
    'reservations/reservation_list.html': """
{% extends 'base.html' %}
{% block title %}Reservations{% endblock %}
{% block content %}
<h1>Reservations</h1>
<a href="{% url 'reservation_create' %}" class="btn btn-primary mb-2">Create new reservation</a>
<table class="table">
    <thead>
        <tr>
            <th>Guest</th>
            <th>Room</th>
            <th>Check-in Date</th>
            <th>Check-out Date</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for reservation in reservations %}
        <tr>
            <td>{{ reservation.guest.username }}</td>
            <td>{{ reservation.room.number }}</td>
            <td>{{ reservation.check_in_date }}</td>
            <td>{{ reservation.check_out_date }}</td>
            <td>
                <a href="{% url 'reservation_detail' reservation.pk %}" class="btn btn-info btn-sm">View</a>
                <a href="{% url 'reservation_update' reservation.pk %}" class="btn btn-warning btn-sm">Edit</a>
                <a href="{% url 'reservation_delete' reservation.pk %}" class="btn btn-danger btn-sm">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
{% endblock %}
    """,
    'reservations/reservation_detail.html': """
{% extends 'base.html' %}
{% block title %}Reservation Detail{% endblock %}
{% block content %}
<h1>Reservation Detail</h1>
<p><strong>Guest:</strong> {{ reservation.guest.username }}</p>
<p><strong>Room:</strong> {{ reservation.room.number }}</p>
<p><strong>Check-in Date:</strong> {{ reservation.check_in_date }}</p>
<p><strong>Check-out Date:</strong> {{ reservation.check_out_date }}</p>
<a href="{% url 'reservation_update' reservation.pk %}" class="btn btn-warning">Edit</a>
<a href="{% url 'reservation_delete' reservation.pk %}" class="btn btn-danger">Delete</a>
<a href="{% url 'reservation_list' %}" class="btn btn-secondary">Back to list</a>
{% endblock %}
    """,
    'reservations/reservation_form.html': """
{% extends 'base.html' %}
{% block title %}Reservation Form{% endblock %}
{% block content %}
<h1>Reservation Form</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-primary">Save</button>
    <a href="{% url 'reservation_list' %}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}
    """,
    'reservations/reservation_confirm_delete.html': """
{% extends 'base.html' %}
{% block title %}Confirm Delete{% endblock %}
{% block content %}
<h1>Confirm Delete</h1>
<p>Are you sure you want to delete this reservation?</p>
<form method="post">
    {% csrf_token %}
    <button type="submit" class="btn btn-danger">Confirm</button>
    <a href="{% url 'reservation_list' %}" class="btn btn-secondary">Cancel</a>
</form>
{% endblock %}
    """
}

# Function to create the directories and files
def create_template_files(base_dir, templates):
    for path, content in templates.items():
        full_path = os.path.join(base_dir, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w') as f:
            f.write(content.strip())
    print(f"Templates created successfully in {base_dir}")

# Run the function to create the templates
create_template_files(BASE_DIR, templates)
