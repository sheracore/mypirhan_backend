import uuid
import os

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# recommnded to retrieve setting from the django settings(custom_shit.setting)
from django.conf import settings
from django.utils import timezone


def product_image_file_path(instance, filename):
    """Generate file path for new product image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/product/', filename)


def design_append_image_file_path(instance, filename):
    """Generate file path for new product image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/design_append/', filename)


def design_upload_append_image_file_path(instance, filename):
    """Generate file path for new product image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/design_upload_append/', filename)


def design_image_file_path(instance, filename):
    """Generate file path for new product image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/final_product/', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a new user"""
        if not email:
            raise ValueError("users most have an email address")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create a superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    """Custom user model that suppors using email instead of username"""
    email = models.EmailField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Supplier(models.Model):
    """Supplier to be used for products"""
    """Instead of reffrence user object directly that we could do
       we ganna use best practice method to retrieving auth user model
       setting from django settings"""
    company_name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    type_good = models.CharField(max_length=64)
    discount_type = models.CharField(max_length=64, null=True)
    url = models.URLField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.company_name


class Category(models.Model):
    category_type = models.CharField(
        max_length=128, default='Tshirt', unique=True)

    def __str__(self):
        return self.category_type


class Product(models.Model):
    """Supplier to be used for products"""
    """Instead of reffrence user object directly that we could do
       we ganna use best practice method to retrieving auth user model
       setting from django settings"""
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_brand = models.CharField(max_length=64)
    product_name = models.CharField(max_length=64)
    product_description = models.CharField(
        max_length=512, null=True)
    price_irr = models.IntegerField()
    product_available = models.BooleanField(default=True)
    discount_available = models.BooleanField(default=True)
    discount = models.FloatField(default=0.0)
    available_size = models.BooleanField(default=True)
    available_colors = models.BooleanField(default=True)
    size = models.CharField(max_length=64)
    color = models.CharField(max_length=64, default="No color")
    weight_gram = models.FloatField(null=True)
    units_in_stock = models.IntegerField(null=True)
    units_on_order_per_day = models.IntegerField(null=True)
    image_front = models.ImageField(upload_to=product_image_file_path)
    image_back = models.ImageField(upload_to=product_image_file_path)
    image_side_left = models.ImageField(upload_to=product_image_file_path)
    image_side_right = models.ImageField(upload_to=product_image_file_path)
    ranking = models.FloatField(null=True)
    note = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.product_name


class ProductColors(models.Model):
    """ProductColors to be used for products"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=64)
    image_front = models.ImageField(upload_to=product_image_file_path)
    image_back = models.ImageField(upload_to=product_image_file_path)
    image_side_left = models.ImageField(upload_to=product_image_file_path)
    image_side_right = models.ImageField(upload_to=product_image_file_path)

    def __str__(self):
        return self.color


class Shipper(models.Model):
    """Shipper to transfer product to the customer"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    company_name = models.CharField(max_length=64)

    def __str__(self):
        return self.company_name


class Customer(models.Model):
    """Customer created when purchase occured"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE
                                )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=64, default='Tehran')
    province = models.CharField(max_length=64, default='Tehran')
    phone = models.CharField(max_length=11, unique=True)
    postal_code = models.CharField(max_length=32)
    country = models.CharField(max_length=64, default='IRAN')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.first_name


class DesignAppendCategory(models.Model):
    """OrderItemAppendCategory use for OrderItemAppend """
    type_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.type_name


class Order(models.Model):
    """Order to save customers purchase"""
    customer_id = models.IntegerField()
    create_order_datetime = models.DateTimeField(default=timezone.now)
    shipper_date = models.DateTimeField()
    paid_datetime = models.DateTimeField(null=True)
    paid = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, unique=True)
    age = models.IntegerField(null=True)
    city = models.CharField(max_length=64, default='Tehran')
    province = models.CharField(max_length=64, default='Tehran')
    postal_code = models.CharField(max_length=32, null=True)
    country = models.CharField(max_length=64, default='IRAN')

    def __str__(self):
        return self.first_name


class OrderItem(models.Model):
    """OrderItem to store edited products and its price"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    product_brand = models.CharField(max_length=64)
    product_name = models.CharField(max_length=64)
    product_description = models.CharField(
        max_length=512, null=True)
    # Its contain product price and orderitemappend price
    price_irr = models.IntegerField()  # Product price
    # Total = quantity * price_irr + (total design append price)
    total_price_irr = models.IntegerField()
    discount = models.FloatField(default=0.0)
    size = models.CharField(max_length=64)
    color = models.CharField(max_length=64, default="No color")
    weight_gram = models.FloatField(null=True)
    final_product_image_front = models.ImageField(
        upload_to=design_image_file_path)
    final_product_image_back = models.ImageField(
        upload_to=design_image_file_path)
    final_product_image_side_left = models.ImageField(
        upload_to=design_image_file_path)
    final_product_image_side_right = models.ImageField(
        upload_to=design_image_file_path)

    def __str__(self):
        return self.product_name


class DesignAppend(models.Model):
    """OrderItemAppend useed to customizing products in order item"""
    design_append_category = models.ForeignKey(
        DesignAppendCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    design_append_price_irr = models.IntegerField()
    image = models.ImageField(upload_to=design_append_image_file_path)

    def __str__(self):
        return self.name


class DesignUpload(models.Model):
    """DesignUpload used to uloading new design from user"""
    image = models.ImageField(upload_to=design_upload_append_image_file_path)
