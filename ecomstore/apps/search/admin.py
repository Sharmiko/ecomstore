from django.contrib import admin
from ecomstore.apps.search.models import SearchTerm


class SearchTermAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'ip_address', 'search_date')
    list_filter = ('ip_address', 'q')  # TODO - add user
    # TODO - exclude user


admin.site.register(SearchTerm, SearchTermAdmin)
