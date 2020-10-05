from django.core.management.base import BaseCommand
from api.models import Weather
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Generate random data'

    def add_arguments(self, parser):
        parser.add_argument('--n',
                            dest='number',
                            type=int,
                            default=10,
                            help='Indicates the number of records to be created. 10 records by default.')

    def handle(self, *args, **kwargs):
        fake = Faker()
        num = kwargs['number']
        records = []
        for _ in range(num):
            kwargs = {
                'datetime': fake.date_time(),
                'temperature': round(random.uniform(0.0, 40.0), 1)
            }
            record = Weather(**kwargs)
            records.append(record)
        Weather.objects.bulk_create(records)
        self.stdout.write(self.style.SUCCESS('{} weather records saved successfully.'.format(num)))
