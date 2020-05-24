from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='order/media', default="")

    def __str__(self):
        return self.productName


class Orders(models.Model):
    orderId = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    accountId = models.ForeignKey(User, on_delete=models.CASCADE)
