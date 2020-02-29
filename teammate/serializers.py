#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import serializers
from teammate.models.teammate import Teammate


class TeammateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teammate
        fields = '__all__'
