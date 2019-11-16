#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

CREATED_AT = 'created_at'
UPDATED_AT = 'updated_at'


class AbstractBasicModel(models.Model):
    """Holds basic fields for any models"""
    created_at = models.DateTimeField(null=False, auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(null=False, auto_now=True, verbose_name='Updated At')

    class Meta:
        abstract = True
