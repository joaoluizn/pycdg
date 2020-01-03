#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_basic_model import AbstractBasicModel


class AbstractTeamModel(AbstractBasicModel):
    name = models.CharField(null=False, blank=False, max_length=60)
    description = models.TextField(null=False, blank=False)

    class Meta:
        abstract = True
