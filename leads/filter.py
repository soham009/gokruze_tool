import django_filters
from leads.models import Leads

class LeadsFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(lookup_expr='Kochi')

	class Meta:
		model = Leads
        fields = {'City': ['Kochi'],
                  }