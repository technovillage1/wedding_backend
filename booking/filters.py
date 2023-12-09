import django_filters
from .models import Schedule

class ScheduleFilter(django_filters.FilterSet):
    date_from = django_filters.NumberFilter(field_name="date", lookup_expr='gte')
    date_to = django_filters.NumberFilter(field_name="date", lookup_expr='lte')
    region = django_filters.CharFilter(field_name='service__region__name')
    district = django_filters.CharFilter(field_name='service__district__name')
    title = django_filters.CharFilter(field_name="service__title", lookup_expr='icontains')
    people_count_from = django_filters.NumberFilter(field_name="service__people_count", lookup_expr='gte')
    people_count_to = django_filters.NumberFilter(field_name="service__people_count", lookup_expr='lte')
    price_from = django_filters.NumberFilter(field_name="service__price", lookup_expr='gte')
    price_to = django_filters.NumberFilter(field_name="service__price", lookup_expr='lte')
    
    class Meta():
        model = Schedule
        fields = ['is_booked', 'service', 'time', 'date']
