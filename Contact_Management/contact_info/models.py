from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Create your models here.
class Contact(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email_address = models.EmailField(max_length=50)
  phone_number = models.CharField(
        max_length=12, 
        validators=[
            RegexValidator(r'^\d+$', "Phone numbers should contain only digits.")
        ]
    )
  address = models.TextField()
  
  def __str__(self):
        return self.first_name
      
      
      
      
      
