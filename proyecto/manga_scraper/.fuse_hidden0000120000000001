#!/bin/bash

if [ "$#" -eq 1 ]; then  
    scrapy crawl mangahere_spider -a start_url=$1
#'http://www.mangahere.com/manga/naruto/'
#    scrapy crawl mangahere_spider -a start_url=$1
else
    echo "Num args. incorrecto. Uso $0 <mangahere_serie_url>"
    echo "Ejemplo: $0 'http://www.mangahere.com/manga/naruto/'"
fi
