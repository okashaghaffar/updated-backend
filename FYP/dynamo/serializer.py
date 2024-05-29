from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class TeamSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model=Team
        fields="__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['lead'] = UserSerializer(instance.lead).data
        return data

class RoleSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    teams=serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    class Meta:
        model=UserRole
        fields="__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance.user).data
        data['teams'] = TeamSerializer(instance.teams).data
        return data

class ProjectSerializer(serializers.ModelSerializer):
    bid_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model=Project
        fields="__all__"   
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['bid_by'] = UserSerializer(instance.bid_by).data
        return data

class UserStorySerializer(serializers.ModelSerializer):
    pid= serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    class Meta:
        model=UserStory
        fields="__all__"   
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['pid'] = ProjectSerializer(instance.pid).data
        return data 

class TaskSerializer(serializers.ModelSerializer):
    assigned_to= serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    pid= serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    usid=serializers.PrimaryKeyRelatedField(queryset=UserStory.objects.all())
    class Meta:
        model=Task
        fields="__all__"   
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['assigned_by'] = UserSerializer(instance.assigned_by).data
        data['assigned_to'] = UserSerializer(instance.assigned_to).data
        data['usid'] = UserStorySerializer(instance.usid).data
        data['pid'] = ProjectSerializer(instance.pid).data
        return data 
    

class PTeamSerializer(serializers.ModelSerializer):
    pid= serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    lead= serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model=PTeam
        fields="__all__"
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['lead'] = UserSerializer(instance.lead).data
        data['pid'] = ProjectSerializer(instance.pid).data
        return data 
    
    


