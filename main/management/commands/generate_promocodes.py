import json
import random
import string
from django.core.management import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--amount', type=int, help='Amount of new promocodes')
        parser.add_argument('--group', type=str, help='Group name')
        parser.add_argument('--file', type=str, help='File path', default='promo_codes.json')

    def handle(self, *args, **kwargs):
        amount = kwargs['amount']
        group = kwargs['group']
        f = kwargs.get('file')

        old_promo_codes = []
        new_promo_codes = []

        with open(f, 'r', encoding='utf-8') as fp:
            try:
                data = json.load(fp)
            except:
                data = {}

        for i in data.values():
            old_promo_codes += i

        if not data.get(group, ''):
            data[group] = []

        while amount != 0:
            code = ''.join([random.choice(
                string.ascii_letters +
                string.digits +
                string.punctuation) for n in range(8)])
            if code not in old_promo_codes and code not in new_promo_codes:
                data[group].append(code)
                new_promo_codes.append(code)
                amount -= 1

        with open(f, 'w', encoding='utf-8') as fp:
            json.dump(data, fp, indent=2, ensure_ascii=False)
