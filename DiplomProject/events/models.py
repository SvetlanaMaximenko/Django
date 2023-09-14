from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    name = models.CharField(max_length=200)
    meeting_time = models.DateTimeField()
    location = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    users = models.ManyToManyField("user.User", related_name="events")
    # tags = models.ManyToManyField(Tag, related_name="events")

    def __str__(self):
        return self.name

    @property
    def comments_count(self) -> int:
        return self.comments.all().count()


class Image(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)



