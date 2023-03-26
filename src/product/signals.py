from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product, ProductVariant, ProductVariantPrice, ProductImage


@receiver(post_save, sender=Product)
def create_related_objects(sender, instance, created, **kwargs):
    if created:
        # Create ProductVariant object
        variant = ProductVariant.objects.create(
            variant_title='Default',
            variant=None,
            product=instance
        )

        # Create ProductVariantPrice object
        ProductVariantPrice.objects.create(
            product_variant_one=variant,
            product_variant_two=None,
            product_variant_three=None,
            price=instance.price,
            stock=instance.stock,
            product=instance
        )

        # Create ProductImage object
        ProductImage.objects.create(
            product=instance,
            file_path=instance.image_url
        )
