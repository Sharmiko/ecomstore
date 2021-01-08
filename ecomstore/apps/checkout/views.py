import re
import datetime

from rest_framework import viewsets
from rest_framework.decorators import action

class CreditCartInfoViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['GET'])
    def get_cc_expire_years(self):
        current_year = datetime.datetime.now().year
        return [
            str(x) for x in range(current_year, current_year + 12)
        ]

    @action(detail=False, methods=['GET'])
    def get_cc_expire_months(self):
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

    CARD_TYPES = (
        ('MasterCard', 'MasterCard'),
        ('VISA', 'VISA'),
        ('AMEX', 'AMEX'),
        ('Discover', 'Discover')
    )

    def strip_non_numbers(self, data):
        """ get rid of all non-number characters
        """
        non_numbers = re.compile('\D')
        return non_numbers.sub('', data)

    def card_Luhn_check_is_valid_sum(self, card_number):
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
