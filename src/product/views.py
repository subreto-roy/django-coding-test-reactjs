# from django.views.generic import ListView
# from .models import Product
# from django.shortcuts import render
# from product.models import Product, ProductVariant, ProductVariantPrice, ProductImage
# import django_filters
# from django.core.paginator import Paginator

# class ProductListView(ListView):
#     model = Product
#     template_name = 'product/product_list.html'
#     context_object_name = 'products'
#     paginate_by = 6


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         product_list = self.get_queryset()
#         paginator = Paginator(product_list, self.paginate_by)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context['page_obj'] = page_obj
#         return context


#     def summary(request):
#         product_count = Product.objects.count()
#         variant_count = ProductVariant.objects.count()
#         variant_price_count = ProductVariantPrice.objects.count()
#         product_image_count = ProductImage.objects.count()

#     context = {
#         'product_count': product_count,
#         'variant_count': variant_count,
#         'variant_price_count': variant_price_count,
#         'product_image_count': product_image_count,
#     }
# return render(request, 'summary.html', context)

# from django_filters.views import FilterView

# class ProductListView(FilterView):
#     model = Product
#     filterset_class = ProductFilter
#     template_name = 'products/list.html'
#     paginate_by = 12

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['product_variants'] = ProductVariant.objects.all()
        
#         return context
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.annotate(variant_count=Count('productvariant__name'))
#         return queryset

# class ProductFilter(django_filters.FilterSet):
#     title = django_filters.CharFilter(lookup_expr='icontains')
#     sku = django_filters.CharFilter(lookup_expr='icontains')
#     variants__variant__title = django_filters.CharFilter(lookup_expr='icontains')
#     price = django_filters.RangeFilter(field_name='productvariantprice__price')
#     class Meta:
#         model = Product
#         fields = ['title', 'sku', 'variants__variant__title']

from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)
