#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class TeammateStillExistsException(Exception):

    def __init__(self, membership, *args, **kwargs):
        """
        :param teammate.models.membership.Membership membership:
        :param list args:
        :param dict kwargs:
        """
        super().__init__('The {} "{}" still exists'.format(
            membership.teammate.__class__.__name__.lower(), membership.teammate), args, kwargs)
