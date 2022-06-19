from django_filters import rest_framework as filters


class ServiceRequestFilter(filters.FilterSet):

    done_request=filters.BooleanFilter(method='get_prev_request')
    ongoing_request=filters.BooleanFilter(method='get_ongoing_request')

    class Meta:
        fields = ['done_request', 'ongoing_request']
    def get_prev_request(self, queryset, name, value):
        return queryset.filter(status='done')

    def get_ongoing_request(self, queryset, name, value):
        return queryset.filter(status__in=['created', 'waiting payment','in process','waiting pricing'])

