#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework import routers
from teammate.viewset import TeammateViewSet

router = routers.DefaultRouter()
router.register(r'teammate', TeammateViewSet)
