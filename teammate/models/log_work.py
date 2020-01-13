#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models import Teammate
from teammate.models.abstract_basic_model import AbstractBasicModel


class LogWork(AbstractBasicModel):
    """A Log Work that a teammate register in a software project"""
    date = models.DateField(null=False, blank=False, verbose_name='Log Date')
    time_logged = models.FloatField(null=False, blank=False, verbose_name='Time Logged (in hours)')
    teammate = models.OneToOneField(Teammate, on_delete=models.CASCADE, verbose_name='Teammate')

    class Meta:
        """Meta data for Log Work model"""
        verbose_name = 'log work'
        verbose_name_plural = 'log works'
