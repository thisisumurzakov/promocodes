import json
from django.core.management import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('code', type=str, help='Promocode')
        parser.add_argument('--file', type=str, help='File path', default='promo_codes.json')

    def handle(self, *args, **kwargs):
        code = kwargs['code']
        f = kwargs.get('file')

        with open(f, 'r', encoding='utf-8') as fp:
            try:
                data = json.load(fp)
            except:
                data = {}
            for key, value in data.items():
                if code in value:
                    self.stdout.write('код существует группа = "%s"' % key)
                    return
            self.stdout.write('код не существует')
