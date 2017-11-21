# -*- coding: utf-8 -*-
from lingo24.business_documents.pricing import Price, TotalPrice

from .base import BaseTestCase


class PriceTestCase(BaseTestCase):
    def test_equality(self):
        self.assertEqual(Price('GBP', 123, 456), Price('GBP', 123, 456))
        self.assertNotEqual(Price('GBP', 123, 456), Price('USD', 123, 456))
        self.assertNotEqual(Price('GBP', 123, 456), Price('GBP', 111, 456))
        self.assertNotEqual(Price('GBP', 123, 456), Price('GBP', 123, 111))

    def test_tax(self):
        price = Price('GBP', 123, 456)
        self.assertEqual(price.tax, 333)

    def test_formatted_net(self):
        self.assertEqual(Price('GBP', 123, 456).formatted_net, u'£123')
        self.assertEqual(Price('EUR', 123, 456).formatted_net, u'€123')
        self.assertEqual(Price('USD', 123, 456).formatted_net, u'$123')
        self.assertEqual(Price('AUD', 123, 456).formatted_net, u'AUD 123')

    def test_formatted_gross(self):
        self.assertEqual(Price('GBP', 123, 456).formatted_gross, u'£456')
        self.assertEqual(Price('EUR', 123, 456).formatted_gross, u'€456')
        self.assertEqual(Price('USD', 123, 456).formatted_gross, u'$456')
        self.assertEqual(Price('AUD', 123, 456).formatted_gross, u'AUD 456')

    def test_formatted_tax(self):
        self.assertEqual(Price('GBP', 123, 456).formatted_tax, u'£333')
        self.assertEqual(Price('EUR', 123, 456).formatted_tax, u'€333')
        self.assertEqual(Price('USD', 123, 456).formatted_tax, u'$333')
        self.assertEqual(Price('AUD', 123, 456).formatted_tax, u'AUD 333')


class TotalPriceTestCase(BaseTestCase):
    def test_equality(self):
        self.assertEqual(
            TotalPrice(Price('GBP', 111, 222), Price('GBP', 333, 444)),
            TotalPrice(Price('GBP', 111, 222), Price('GBP', 333, 444)),
        )
        self.assertNotEqual(
            TotalPrice(Price('GBP', 111, 222), Price('GBP', 333, 444)),
            TotalPrice(Price('USD', 111, 222), Price('GBP', 333, 444)),
        )
        self.assertNotEqual(
            TotalPrice(Price('GBP', 111, 222), Price('GBP', 333, 444)),
            TotalPrice(Price('GBP', 111, 222), Price('USD', 333, 444)),
        )
