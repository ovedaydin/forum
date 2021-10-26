from django.db import models
from django.contrib.auth.models import User

# class Thread(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
#    created_at = models.DateTimeField(auto_now_add=True)
#    subject = models.CharField(max_length=200, null=True, blank=True)


class Post(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #edited_at = models.DateTimeField(null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)
    # thread = models.OneToOneField(Thread, on_delete=models.CASCADE, null=True, blank=True)

    @property
    def get_likes(self):
        return self.liked_set.all()

    @property
    def get_likes_count(self):
        return len(self.get_likes)


class Liked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = ["user", "post"]
