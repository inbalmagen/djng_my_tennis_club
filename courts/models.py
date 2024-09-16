from django.utils import timezone
from django.db import models
from members.models import Member

class Court(models.Model):
  number = models.PositiveIntegerField(unique=True)
  is_occupied = models.BooleanField(default=False)
  time_of_occupation = models.DateTimeField(null=True)
  updated = models.DateTimeField(auto_now=True, null=True)
  created = models.DateTimeField(auto_now_add=True, null=True)

#   def save(self, *args, **kwargs):
#     if self.is_occupied:  # Update the time only if the court is occupied
#         self.time_of_occupation = timezone.now()  # Use timezone-aware datetime
#     else:
#         self.time_of_occupation = None  # Optionally reset the time when the court is not occupied
#     super().save(*args, **kwargs)
def __str__(self):
    return f'Court {self.number}'

class CourtOrder(models.Model):
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    member1 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member1')
    member2 = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='member2')
    start_time = models.DateTimeField()

    def __str__(self):
        return f'Court {self.court.number} ordered by {self.member1.firstname} and {self.member2.firstname}'