from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class queryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = querySerializer
    def get_queryset(self):
        return ChatbotapiQuery.objects.filter(user=self.request.user)

class EntityViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EntitySerializer
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # queryset = Entity.objects.all()
    def get_queryset(self):
        query_set = Entity.objects.filter(user=self.request.user)
        return query_set

class BotSocialConfigViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BotSocialConfigSerializer
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # queryset = Entity.objects.all()
    def get_queryset(self):
        return BotSocialConfig.objects.filter(user=self.request.user)
        

class IntentsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = IntentsSerializer
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # queryset = Entity.objects.all()
    def get_queryset(self):
        query_set = Intents.objects.filter(user=self.request.user)
        return query_set


class SkillsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = SkillsSerializer
    # user = serializers.PrimaryKeyRelatedField(
    #     # set it to read_only as we're handling the writing part ourselves
    #     read_only=True,
    # )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # queryset = Entity.objects.all()
    def get_queryset(self):
        query_set = Skills.objects.filter(user=self.request.user)
        return query_set

class BotsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = BotsSerializer
    user = serializers.PrimaryKeyRelatedField(
        # set it to read_only as we're handling the writing part ourselves
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    # queryset = Entity.objects.all()
    def get_queryset(self):
       query_set = Bots.objects.filter(user=self.request.user)
       return query_set


