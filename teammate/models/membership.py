#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_basic_model import AbstractBasicModel
from teammate.models.teammate import Teammate
from teammate.exceptions.teammate_still_exists_exception import TeammateStillExistsException

JOINED_AT = 'joined_at'
DISJOINED_AT = 'disjoined_at'
MEMBERSHIP_TYPE = 'membership_type'
TEAMMATE = 'teammate'


class Membership(AbstractBasicModel):
    """Register when a teammate became a member of the development team"""
    teammate = models.OneToOneField(Teammate, on_delete=models.CASCADE, verbose_name='Teammate')
    joined_at = models.DateField(null=False, blank=False, verbose_name='Joined At')
    disjoined_at = models.DateField(null=True, blank=True, verbose_name='Disjoined At')
    membership_type = models.CharField(max_length=50, verbose_name='Membership Type')

    def __str__(self):
        """
        :return str: full person name
        """
        return '{} {}'.format(self.teammate, self.membership_type)

    def delete(self, using=None, keep_parents=False):
        """Deletes only if the teammate doesn't exist"""
        if self.teammate.id:
            raise TeammateStillExistsException(self)

        super().delete(using, keep_parents)

    class Meta:
        verbose_name = 'membership'
        verbose_name_plural = 'memberships'
