#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module manipulates the BANDS dictionary."""


from data import BANDS

CORRECTED = BANDS.copy()

CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen']['Sammy Hagar'] = ['vocals']

print CORRECTED['Van Halen'].keys()
