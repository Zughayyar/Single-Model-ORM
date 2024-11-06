from django.db import models

# Create your models here.
class User(models.Model):
    def __str__(self) -> str:
        return f"< User object: {self.first_name} {self.id} >"
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    password = models.CharField(max_length=20)
    is_available = models.BooleanField(default=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def insert_to_users(data):
    first_name = data['first_name']
    last_name = data['last_name']
    email_address = data['email_address']
    age = data['age']
    User.objects.create(first_name = first_name, last_name = last_name , email_address = email_address , age = age)

def get_all_users():
    return User.objects.all()

def delete_from_users(user_id):
    c = User.objects.get(id = user_id)
    c.delete()