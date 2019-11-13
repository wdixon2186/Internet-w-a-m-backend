from django.db import models

class Script(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    logline = models.CharField(max_length=140)
    # thumb = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    script = models.ForeignKey(
        Script, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment