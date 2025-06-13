from django.db import models

class TestCase(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    user_name = models.TextField(blank=True, null=True)
    product = models.TextField(blank=True, null=True)
    component = models.TextField(blank=True, null=True)
    priority = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
            ('Critical', 'Critical'),
        ],
        default='Medium'
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('Draft', 'Draft'),
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        ],
        default='Draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
