from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # image = models.ImageField(upload_to='artistic/images/', null=True, blank=True)
    # video = models.FileField(upload_to='artistic/videos/', null=True, blank=True)
    post_info = models.CharField(max_length=255, blank=True)
    display_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.title}"

class MediaFile(models.Model):
    POST_MEDIA_TYPES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='aesthetic/media/')
    type = models.CharField(max_length=10, choices=POST_MEDIA_TYPES)

    def __str__(self):
        return f"{self.type}: {self.file.name}"
