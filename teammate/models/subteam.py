#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_team_model import AbstractTeamModel
from teammate.models.teammate import Teammate


class SubTeam(AbstractTeamModel):
    teammates = models.ManyToManyField(Teammate)

    class Meta:
        verbose_name = 'sub-team'
        verbose_name_plural = 'sub-teams'
