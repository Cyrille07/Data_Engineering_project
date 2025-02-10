#!/bin/bash

# Exécution des spiders et sauvegarde des résultats

rm -rf data_scraped/*

echo "Lancement des spiders..."

scrapy crawl uniqlomb -o data_scraped/uniqlomb.json
scrapy crawl uniqlomo -o data_scraped/uniqlomo.json
scrapy crawl uniqloms -o data_scraped/uniqloms.json
scrapy crawl uniqlowb -o data_scraped/uniqlowb.json
scrapy crawl uniqlowo -o data_scraped/uniqlowo.json
scrapy crawl uniqlows -o data_scraped/uniqlows.json

echo "Tous les spiders ont été exécutés et les fichiers JSON générés."
