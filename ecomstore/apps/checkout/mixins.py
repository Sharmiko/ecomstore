import re
import datetime

from rest_framework.decorators import action


class CreditCartMixin(object):

    CARD_TYPES = (
        ('MasterCard', 'MasterCard'),
        ('VISA', 'VISA'),
        ('AMEX', 'AMEX'),
        ('Discover', 'Discover')
    )

    @action(detail=False, methods=['GET'])
    def get_cc_info(self, request):
        return {
            'expire_years': self.get_cc_expire_years(),
            'expire_months': self.get_cc_expire_months(),
            'card_types': self.CARD_TYPES
        }

    @staticmethod
    def get_cc_expire_years():
        current_year = datetime.datetime.now().year
        return [
            str(x) for x in range(current_year, current_year + 12)
        ]

    @staticmethod
    def get_cc_expire_months():
        months = []
        current_year = datetime.datetime.now().year
        for month in range(1, 13):
            if (len(str(month))) == 1:
                numeric = '0' + str(month)
            else:
                numeric = str(month)

            months.append(
                (numeric, datetime.date(current_year, month, 1).strftime('%B'))
            )

        return months

    @staticmethod
    def strip_non_numbers(data):
        """ get rid of all non-number characters
        """
        non_numbers = re.compile(r'\D')
        return non_numbers.sub('', data)

    @staticmethod
    def card_luhn_check_is_valid_sum(card_number):
        """ Checks to make sure that card passes Luhn mod-10 checksum
        """
        _sum = 0
        num_digits = len(card_number)
        odd_even = num_digits & 1
        for count in range(0, num_digits):
            digit = int(card_number[count])
            if not ((count & 1) ^ odd_even):
                digit = digit * 2
            if digit > 9:
                digit = digit - 9
            _sum += digit

        return (_sum % 10) == 0
