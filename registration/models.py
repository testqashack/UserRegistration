from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    message = models.CharField(max_length=100)

    class Meta:
        # Mention the name of the table from MySQL
        db_table = "user"
