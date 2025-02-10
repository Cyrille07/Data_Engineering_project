FROM python:3.12.5

# Ici pour créer des dossiers
RUN mkdir /home/dev/ && mkdir /home/dev/project_dsia/
WORKDIR /home/dev/project_dsia

#on copie tous les fichiers du répertoire de travail
COPY . .
COPY requirements.txt /home/dev/project_dsia/requirements.txt
# on installe les bibliothèques via requirements.txt
RUN pip install --no-cache-dir -r /home/dev/project_dsia/requirements.txt

#Ne pas oublier de finir d'installer playwright
RUN playwright install
RUN playwright install-deps

#lancer le scraping en se placant dans le dossier concerné !
RUN chmod +x /home/dev/project_dsia/uniqlo_project/spiders/run_spiders.sh
ENTRYPOINT ["/home/dev/project_dsia/uniqlo_project/spiders/run_spiders.sh"]

# Laisser un shell actif après le script
CMD ["tail", "-f", "/dev/null"]
