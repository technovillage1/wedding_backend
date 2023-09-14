import django_filters

from service.models import Service


class ServiceFilter(django_filters.FilterSet):
    # start_date = django_filters.DateFilter(field_name='books__booking_date', lookup_expr='lte')
    # end_date = django_filters.DateFilter(field_name='books__booking_date', lookup_expr='gte')
    # date = django_filters.DateFilter(field_name='books__booking_date')
    region = django_filters.CharFilter(field_name='region__name')
    district = django_filters.CharFilter(field_name='district__name')
    title = django_filters.CharFilter(lookup_expr='icontains')
    people_count_from = django_filters.NumberFilter(field_name="people_count", lookup_expr='gte')
    people_count_to = django_filters.NumberFilter(field_name="people_count", lookup_expr='lte')
    price_from = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Service
        fields = []
