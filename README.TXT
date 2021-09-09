# Twitch-Farmer

Programm zum automatischen Sammeln von Twitch-Kanalpunkten und möglichen Drops.
Ein Projekt im Rahmen des Schulblocks der Klasse WDIT9a.

Projektleiter: Kevin Schulze
Projektmitglieder: Luke Gutbier, Finn Heeck, Tilman Lenz und Daniel Manjajkin


#INSTALLATION
Diese Anleitung gilt für Debian und Ubuntu derivate auf Basis eines amd64 Prozessors.


Bevor die eigentliche Installation durchgeführt werden kann,
wird empfohlen das System auf mögliche Updates zu überprüfen und entsprechend zu aktualisieren.


sudo apt update
sudo apt upgrade -y


1. sudo apt install git

Auf dem System sollten die Pakete "docker" und "docker-compose" installiert sein

2.apt install docker docker-compose -y

3. git pull https://github.com/kevoooo98/Twitch-Farmer.git

4. cd Twitch-Farmer

Nun sollte das docker-compose.yml angepasst werden
Geben Sie als Variable USER, PASS und 2FA_KEY Ihre Twitch Nutzerdaten ein.
  Um den 2FA_KEY zu erhalten, müssen Sie auf twitch.tv die "FA aktivieren, den
  QR-Code Downloaden und zB mit zbarimg auslesen

5. nano docker-compose.yml

6. sudo docker-compose up

7. Installation abgeschlossen.

Nun können über die Weboberfläche http://IP-Adresse die entsprechenden Streamer
sowie die Watchtime (Wie lange der Stream in Minuten angeschaut werden soll) eingetragen werden.

Unter http://IP-Adresse:7900 kann dem Webdriver zugeschaut werden. Das Passwort ist "secret"
