#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module utilizes for loop in dictionary"""


import data

SUPER_SIDEKICKS = {}
for HERO, HERO_DATA in data.SUPERHEROES.iteritems():
    SUPER_SIDEKICKS[HERO] = HERO_DATA.get('pet')
