#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from teammate.models import Teammate
from teammate.serializers import TeammateSerializer
from rest_framework import viewsets


class TeammateViewSet(viewsets.ModelViewSet):
    queryset = Teammate.objects.all()
    serializer_class = TeammateSerializer
