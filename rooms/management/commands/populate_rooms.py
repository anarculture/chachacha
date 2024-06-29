from django.core.management.base import BaseCommand
from rooms.models import Room

class Command(BaseCommand):
    help = 'Populate the database with initial rooms'

    def handle(self, *args, **kwargs):
        rooms = [
            {'number': f'F{num}', 'room_type': 'Familiar'} for num in range(1, 7)
        ] + [
            {'number': f'T{num}', 'room_type': 'Terraza'} for num in range(1, 8)
        ] + [
            {'number': f'S{num}', 'room_type': 'Sencilla'} for num in range(1, 8)
        ]

        for room_data in rooms:
            room, created = Room.objects.get_or_create(
                number=room_data['number'],
                defaults={'room_type': room_data['room_type']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Room {room.number} created"))
            else:
                self.stdout.write(self.style.WARNING(f"Room {room.number} already exists"))
