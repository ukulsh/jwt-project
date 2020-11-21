from rest_framework import serializers

from .models import *

class querySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatbotapiQuery
        fields = '__all__'

class EntitySerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Entity
        fields = '__all__'


class BotSocialConfigSerializer(serializers.HyperlinkedModelSerializer):
   
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = BotSocialConfig
        fields = '__all__'

    

class IntentsSerializer(serializers.HyperlinkedModelSerializer):
    
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Intents
        fields = '__all__'

class SkillsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Skills
        fields = '__all__'
        

class BotsSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
  
    class Meta:
        model = Bots
        fields = '__all__'
