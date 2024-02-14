from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Panelist(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Adviser(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Thesis(models.Model):

    class Status(models.TextChoices):
        DENIED = "DN", "Denied"
        PUBLISHED = "PB", "Published"
        PENDING = "PD", "Pending"

    title = models.CharField(max_length=255)
    status = models.CharField(
        max_length=3, choices=Status.choices, default=Status.PENDING
    )
    published = models.DateTimeField()
    authors = models.ManyToManyField(Author)
    panelists = models.ManyToManyField(Panelist)
    abstract = models.TextField()
    adviser = models.ForeignKey(Adviser, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.title
