#!/usr/bin/python
import os
import sys

full_path = sys.argv[0]
dir_path = os.path.dirname(full_path)


if(len(sys.argv) == 2):

    os.chdir(dir_path)
    command = 'scrapy crawl mangahere_spider -a start_url=%s' % sys.argv[1]
    print command
    success = os.system(command)
    

elif(len(sys.argv) == 1):
    print "Num args. incorrecto. Uso %s <mangahere_serie_url>" % full_path
    print "Ejemplo: %s http://www.mangahere.com/manga/naruto/" % full_path

