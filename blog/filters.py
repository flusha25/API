from django_filters import rest_framework as filters
from .models import Blog
import django_filters


class BlogFilter(django_filters.FilterSet):
    categories = django_filters.CharFilter(
        field_name='categories__name',
        lookup_expr='icontains',  
        label='category Name'
    )
 


    class Meta:
        model = Blog
        fields = []