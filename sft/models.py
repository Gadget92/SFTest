from django.db import models


class BaseMixin(models.Model):
    rec_id = models.IntegerField(primary_key=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    modify_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class LoanApplication(BaseMixin):
    client_name = models.CharField(max_length=255)
    amount = models.IntegerField()


class Contract(BaseMixin):
    customer_name = models.CharField(max_length=255)
    loan_application = models.OneToOneField(
        LoanApplication, on_delete=models.CASCADE, related_name='loan_application_contract'
    )


class Product(BaseMixin):
    product_name = models.CharField(max_length=255)
    loan_application = models.ForeignKey(
        LoanApplication, on_delete=models.CASCADE, related_name='loan_application_product'
    )


class Manufacturer(BaseMixin):
    name = models.CharField(max_length=255)
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='product'
    )
