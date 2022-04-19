import json

from django.core.management import call_command
from django.test import TestCase


class CommandsTestCase(TestCase):
    def test_generate_promocodes(self, *args, **kwargs):
        with open('test_promo_codes.json', 'w') as f:
            f.write('')

        opts = {'amount': 10,
                'group': 'агенства',
                'file': 'test_promo_codes.json'}
        call_command('generate_promocodes', **opts)

        opts = {'amount': 1,
                'group': 'агенства',
                'file': 'test_promo_codes.json'}
        call_command('generate_promocodes', **opts)

        opts = {'amount': 42,
                'group': 'avtostop',
                'file': 'test_promo_codes.json'}
        call_command('generate_promocodes', **opts)

        opts = {'amount': 5,
                'group': 1,
                'file': 'test_promo_codes.json'}
        call_command('generate_promocodes', **opts)

        with open('test_promo_codes.json', 'r') as f:
            data = json.load(f)

        promocodes_count = 0
        groups_count = 0

        for key, value in data.items():
            groups_count += 1
            for code in value:
                promocodes_count += 1

        self.assertEqual(promocodes_count, 58)
        self.assertEqual(groups_count, 3)