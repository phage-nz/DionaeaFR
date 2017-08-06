import django_filters as filters

from Web.models.connection import Connection


class ConnectionFilter(filters.FilterSet):
    connection_type = filters.CharFilter(
        lookup_expr='contains'
    )

    connection_transport = filters.CharFilter(
        lookup_expr='contains'
    )

    connection_protocol = filters.CharFilter(
        lookup_expr='contains'
    )

    local_port = filters.NumberFilter()

    remote_host = filters.CharFilter(
        lookup_expr='contains'
    )

    remote_port = filters.NumberFilter()

    class Meta:
        model = Connection
        fields = [
            'connection_type',
            'connection_transport',
            'connection_protocol',
            'local_port',
            'remote_host',
            'remote_port',
        ]

# vim: set expandtab:ts=4
