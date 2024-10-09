from django.forms import ModelForm
from main.models import Shop
from django.utils.html import strip_tags

class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ["name", "price", "description", "flower", "quantity"]

    def clean_flower(self):
        flower = self.cleaned_data["flower"]
        return strip_tags(flower)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    