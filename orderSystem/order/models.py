from django.db import models


# Create your models here.
class product(models.Model):
    productId = models.AutoField
    productName = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image= models.ImageField(upload_to='order/media', default="")

    def __str__(self):
        return self.product_name