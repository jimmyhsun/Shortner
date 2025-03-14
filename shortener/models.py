from django.db import models
import shortuuid
from django.utils.timezone import now, timedelta

class ShortURL(models.Model):
    original_url = models.URLField(max_length=2048)
    short_url = models.CharField(max_length=10, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = shortuuid.ShortUUID().random(length=6) # 生成 6 位短網址
        if not self.expiration_date:
            self.expiration_date = now() + timedelta(days=30)  # 預設 30 天有效期
        super().save(*args, **kwargs)
