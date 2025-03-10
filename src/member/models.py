from django.db import models
from django.core.validators import MinLengthValidator

class MembershipType(models.Model):
    membership_type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)
    duration = models.IntegerField()  # in months
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.type_name

class Members(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    membership_start_date = models.DateField()
    membership_end_date = models.DateField()
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return self.name

