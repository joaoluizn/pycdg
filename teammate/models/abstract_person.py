#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_basic_model import AbstractBasicModel

STR = '__str__'
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
BIRTH_DATE = 'birth_date'


class Person(AbstractBasicModel):
    """Abstract person"""
    first_name = models.CharField(max_length=50, null=True, blank=False, verbose_name='First Name')
    last_name = models.CharField(max_length=50, null=True, blank=False, verbose_name='Last Name')
    birth_date = models.DateField(null=False, verbose_name='Birthday')

    def __str__(self):
        """
        :return str: full person name
        """
        return ' '.join([self.first_name, self.last_name])

    class Meta:
        abstract = True

        constraints = [
            models.UniqueConstraint(fields=[FIRST_NAME, LAST_NAME], name='unique-person')
        ]
