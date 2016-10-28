#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module demonstrates the dictionary update."""


from data import BANDS

BANDS['Buckingham Nicks'] = {'Lindsey Buckingham': ['guitar', 'vocals'],
                             'Stevie Nicks': ['vocals', 'tambourine']}

BANDS['Fleetwood Mac'].update(BANDS['Buckingham Nicks'])
