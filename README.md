# picoW socket
![dht](https://github.com/acican/picoW_socket/assets/10486613/1b427783-e8af-4dc0-9b78-04c51cfaf875)

Un exemplu de cod in micropython pentru citirea temperaturii si umiditatii de la un senzor dht22 si afisarea datelor citite intr-o fereastra grafica creata in python. Aplicatia se bazeaza pe o conexiune socket, client-server, in reteaua lan wifi locala, in care serverul este instalat pe un microcontroler picoW iar clientul intr-o aplicatie desktop scrisa in python. 

Elementele de baza:
- Raspberry pico W
- interpretor: rp2-pico-w-20230426-v1.20.0.uf2
- modul AM2302
- pc windows
- retea wifi locala
  
Exemplele de cod folosite sunt grupate in folderul "chat" si au fost obtinute prin cerere pe chatGPG, respectiv:
- cod micropyton pentru socket server
- cod python pentru socket client
- exemplu de fereastra grafica in python, folosind interfata implicita tkinter
- exemplu de afisare periodica in fereastra a datei si orei
- conectare la reteaua wifi din micropython, furnizand ssid si password-ul ruter-ului.
  
Senzorul de temperatura si umiditate comunica cu controlerul printr-o conexiune pe 1 fir (in exemplu, de cod, pinul 20) prin intermediul librariei micropython "dht".
Codul socket-serverului este cel din fisierul "main.py", restrictia de nume este ceruta de micropython din motiv de pornire automata a interpretorului, pe acest fisier, la reconectarea alimentarii microcontrolerului.
Adresa "ip" a serverului depinde de domeniul alocat de ruter si ar trebui sa fie statica.
