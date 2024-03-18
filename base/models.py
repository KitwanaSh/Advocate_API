from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)
    bio = models.TextField(null=False)

    def __str__(self):
        return self.name

class Advocates(models.Model):
    """
        The Advacate mode class goes here
        Args:
            - company: The company of an advocate (one to many relationship with Company model)
            - username: The username of an advocate
            - bio: The biography of an advocate
            - str(self): The string representation of the model
    """
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
    bio = models.TextField(null=False)

    def __str__(self):
        return self.username
