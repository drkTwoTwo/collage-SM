import pandas as pd
from django.core.management.base import BaseCommand
from attendence.models import Student, Class
import os

# Function to get class based on roll number
def get_class_from_roll(roll):
    roll_lower = roll.lower()
    if 'cs' in roll_lower:
        return 'CSE6'
    elif 'pt' in roll_lower:
        return 'PT6'
    elif 'el' in roll_lower:
        return 'EL6'
    else:
        return 'UNKNOWN'

# Command to import students from a CSV file
class Command(BaseCommand):
    help = 'Import students from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        if not os.path.isfile(csv_file):
            self.stdout.write(self.style.ERROR(f"File not found: {csv_file}"))
            return

        self.stdout.write(f"Processing {csv_file}...")

        # Read CSV file
        df = pd.read_csv(csv_file)

        for _, row in df.iterrows():
            roll = row['roll'].strip()
            name = row['name'].strip()

            class_name = get_class_from_roll(roll)

            # Fetch or create Class object
            class_obj, _ = Class.objects.get_or_create(id=class_name)

            # Insert student record
            student, created = Student.objects.update_or_create(
                roll=roll,
                defaults={'name': name, 'class_id': class_obj}
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {roll} - {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Updated: {roll} - {name}"))

        self.stdout.write(self.style.SUCCESS("Import complete!"))
