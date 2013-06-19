#!/usr/bin/python
# -*-coding: utf-8 -*-
import re
patron= "mancha"
cadena="En un lugar de la mancha de cuyo nombre no quiero acordarme"
if re.search(patron, cadena):
    print "Lo encontré, que cosas"
else:
    print "No aparece"

