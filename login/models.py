from django.db import models

class PasswordResetRequest(models.Model):
    email = models.EmailField()
    token = models.CharField(max_length=255)
    request_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset request for {self.email} at {self.request_time}"
