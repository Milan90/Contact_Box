from django.db import models



class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=250)
    description = models.TextField()
    address = models.ForeignKey("Address", null=True, on_delete=models.CASCADE)


class Address(models.Model):
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    building_number = models.SmallIntegerField()
    flat_number = models.SmallIntegerField()


class Phone(models.Model):
    phone_type = (
        (1, "domowy"),
        (2, "prywatny"),
        (3, "służbowy"),
    )
    phone_number = models.IntegerField()
    type = models.SmallIntegerField(choices=phone_type)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Email(models.Model):
    email_typ = (
        (1, "domowy"),
        (2, "prywatny"),
        (3, "służbowy"),
    )
    email_address = models.CharField(max_length=100)
    type = models.IntegerField(choices=email_typ)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
