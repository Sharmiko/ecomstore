from django.db import models


class SearchTerm(models.Model):
    q = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()
    tracking_id = models.CharField(max_length=50, default='')
    # TODO - add user field

    def __str__(self):
        return self.q
