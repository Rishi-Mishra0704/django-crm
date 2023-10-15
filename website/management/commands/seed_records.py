from django.core.management.base import BaseCommand
from website.models import Record
import random
import string

class Command(BaseCommand):
    help = 'Seed the database with 8 unique records'

    def handle(self, *args, **options):
        # Your data seeding logic here
        for i in range(1, 9):
            first_name = f'First_{i}'
            last_name = f'Last_{i}'
            email = f'email{i}@example.com'
            phone = ''.join(random.choice(string.digits) for _ in range(10))  # Generates a random 10-digit number
            address = f'{i} Main St'
            city = f'City_{i}'
            state = f'State_{i}'
            zipcode = f'1000{i}'

            Record.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                state=state,
                zipcode=zipcode
            )

        self.stdout.write(self.style.SUCCESS('Data seeding complete.'))
