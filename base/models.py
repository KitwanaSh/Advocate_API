from django.db import models

class Advocates(models.Model):
    """
        The Advacate mode class goes here
        Args:
            - username: The username of an advocate
            - bio: The biography of an advocate
            - str(self): The string representation of the model
    """
    username = models.CharField(max_length=50, unique=True)
    bio = models.TextField(null=False)

    def __str__(self):
        return self.username
