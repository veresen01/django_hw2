from django.core.management.base import  BaseCommand
from app1.models import Product

class Command(BaseCommand):
    help = "Delete product by ID"

    def add_arguments(self, parser):
        parser.add_argument("pk", type=int, help="User ID")
    def handle (self, *args, **kwargs):

        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'{product}')