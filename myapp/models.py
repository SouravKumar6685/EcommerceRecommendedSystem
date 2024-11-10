from django.db import models
from django.utils import timezone
from django.contrib.postgres.search import SearchVectorField, SearchVector
from django.contrib.postgres.indexes import GinIndex

# Step 1: Define the abstract base model with core fields
class BaseModel(models.Model):
    """
    Abstract base model that provides common fields for all models,
    ensuring code reusability and maintainability.
    """
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Additional shared behavior can be defined here
        super().save(*args, **kwargs)

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    """
    The Product model represents items in the e-commerce store.
    Inherits from BaseModel for core fields and provides additional
    product-specific fields, adhering to the Single Responsibility Principle.
    """
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.FloatField()
    rating = models.FloatField()
    stock = models.PositiveIntegerField()
    brand = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    warranty_information = models.CharField(max_length=255, blank=True, null=True)
    shipping_information = models.CharField(max_length=255, blank=True, null=True)
    availability_status = models.CharField(max_length=50)
    return_policy = models.TextField()
    minimum_order_quantity = models.PositiveIntegerField()
    dimensions = models.CharField(max_length=200, blank=True, null=True)
    weight = models.CharField(max_length=100, blank=True, null=True) 
    thumbnail = models.URLField(default='https://via.placeholder.com/150')
    tags = models.ManyToManyField('Tag', related_name='products')
    search_vector = SearchVectorField(null=True)

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('title', 'description', 'category', 'tags__name')
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        indexes = [GinIndex(fields=['search_vector'])]

    def __str__(self):
        return self.title
    
    

    def get_discounted_price(self):
        """
        Calculate and return the price after applying the discount.
        This adheres to the Single Responsibility Principle by providing
        a specific method for discount calculations.
        """
        return self.price * (1 - (self.discount_percentage / 100))

class Review(BaseModel):
    """
    The Review model represents customer feedback for a product.
    It has a ForeignKey relationship with Product.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField()
    reviewer_name = models.CharField(max_length=255)
    reviewer_email = models.EmailField()

    def __str__(self):
        return f'Review for {self.product.title} by {self.reviewer_name}'


class Category(BaseModel):
    """
    The Category model represents a product category (e.g., beauty, electronics).
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



