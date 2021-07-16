from django.db import models
from django.contrib.auth.models import User
class todomodel(models.Model):
    statusF=[
        ('C','Complete'),
        ('P','Pending'),
    ]
    P_status=[
        ('1','1️⃣'),
        ('2','2️⃣'),
        ('3','3️⃣'),
        ('4','4️⃣'),
        ('5','5️⃣'),
        ('6','6️⃣'),
        ('7','7️⃣'),
        ('8','8️⃣'),
        ('9','9️⃣'),
        ('10','🔟'),
    ]
    title=models.CharField(max_length=30)
    status=models.CharField(max_length=2,choices=statusF)
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Priority=models.CharField(max_length=2,choices=P_status)

