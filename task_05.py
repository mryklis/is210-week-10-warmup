#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module changes a dictionary key value"""


from data import SUPERHEROES

SUPERHEROES = SUPERHEROES.copy()

SUPERHEROES['Logan']['alias'] = 'Wolverine' 
