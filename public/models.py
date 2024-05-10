from django.db import models

class users(models.Model):

    userid=models.AutoField(primary_key=True)


class login(models.Model):
    pass