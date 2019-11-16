#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from teammate.models.abstract_person import Person


class Teammate(Person):
    """A person that works in a software project"""

    class Meta(Person.Meta):
        """Meta data for Teammate model"""
        verbose_name = 'teammate'
        verbose_name_plural = 'teammates'
