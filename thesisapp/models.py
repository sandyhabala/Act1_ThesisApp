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

class Comment(models.Model):
    post = models.ForeignKey(Thesis, 
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email=models.EmailField()
    body= models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'