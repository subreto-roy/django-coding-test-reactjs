import django_filters
from .models import Product, ProductVariant, ProductVariantPrice


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='productvariantprice__price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['title', 'productvariant__variant_title', 'productvariantprice__price']
