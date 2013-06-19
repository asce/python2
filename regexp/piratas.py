#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
Cadena= "En un lugar de la Mancha fea y negra de los piratas"
Resultados= re.sub("a |a$", "as ", Cadena)
print Cadena
print Resultados
