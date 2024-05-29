from django.contrib.auth.models import User
from django.db import models
import datetime
class Team(models.Model):
    id = models.AutoField(primary_key=True)
    lead=models.ForeignKey(User,on_delete=models.CASCADE)
class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=100,null=False)
    teams = models.ForeignKey(Team,on_delete=models.CASCADE,default=1)
    @property
    def username(self):
        return self.user.username


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    bid_by=models.ForeignKey(User,on_delete=models.CASCADE)
    start=models.DateTimeField(default=datetime.datetime.now())
    deadline=models.DateField(default=datetime.datetime.now())
    price=models.IntegerField(default=0)
    column=models.CharField(max_length=100)
    assigned=models.BooleanField(default=False)
    status=models.BooleanField(default=True)

class PTeam(models.Model):
    id =models.AutoField(primary_key=True)
    lead=models.ForeignKey(User,on_delete=models.CASCADE)
    pid=models.ForeignKey(Project,on_delete=models.CASCADE)



class UserStory(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    pid=models.ForeignKey(Project,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    # assigned_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name="assigned_by")
    pid=models.ForeignKey(Project,on_delete=models.CASCADE)
    assigned_to=models.ForeignKey(User,on_delete=models.CASCADE,related_name="assigned_to",default=11)
    status=models.CharField(max_length=100,default="todo")
    usid=models.ForeignKey(UserStory,on_delete=models.CASCADE,null=True)