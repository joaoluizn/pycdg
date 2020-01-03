#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.db import models

from teammate.models.abstract_team_model import AbstractTeamModel
from teammate.models.subteam import SubTeam
from teammate.models.teammate import Teammate


class Team(AbstractTeamModel):
    manager = models.OneToOneField(Teammate, on_delete=None)
    leaders = models.ManyToManyField(Teammate)
    sub_teams = models.ManyToManyField(SubTeam)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

        # TODO: Add constraints:
        #  #1 Allow the leader to be registered if it exists in the teammates
        #  #2 Allow the manager to be registered if it exists in the teammates
        # constraints = [
        #     models.CheckConstraint(check=models.Q(leader__gte=''))
        # ]
