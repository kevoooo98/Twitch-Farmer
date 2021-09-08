# Twitch-Farmer

Programm zum automatischen Sammeln von Twitch-Kanalpunkten und möglichen Drops.
Ein Projekt im Rahmen des Schulblocks der Klasse WDIT9a.

Projektleiter: Kevin Schulze
Projektmitglieder: Luke Gutbier, Finn Heeck, Tilman Lenz und Daniel Manjajkin


#INSTALLATION

Bevor die eigentliche Installation durchgeführt werden kann,
wird empfohlen das System auf mögliche Updates zu überprüfen und entsprechend zu aktualisieren.

sudo apt update
sudo apt upgrade -y


1. sudo apt install git

2. git pull https://github.com/kevoooo98/Twitch-Farmer.git

3. cd Twitch-Farmer

Ggf. müssen vor dem Ausführen des folgenden Befehls die Pakete "docker-compose" und "docker" installiert werden.

4.  curl -fsSL https://test.docker.com -o test-docker.sh

    sudo sh test-docker.sh

    sudo curl -L https://github.com/docker/compose/releases/download/1.25.3/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

    sudo chmod +x /usr/local/bin/docker-compose

5. sudo docker-compose up

6. Installation abgeschlossen.

Nun können über die Weboberfläche http://IP-Adresse die entsprechenden Streamer sowie die Watchtime (Wie lange der Stream angeschaut werden soll) eingetragen werden.
