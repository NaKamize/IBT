# Formálne modely aplikované v hudbe
## Inštalácia
Aby sme mohli výsledný program spustiť je potrebné si nainštalovať potrebné balíčky. Inštalujeme tie, ktoré sa nachádzajú mimo štandardnej knižnice python3.8. Python 3.8 je interpret pomocou ktorého bol tento program vyvíjaný.

Zoznam potrebných balíčkov je v súbore requirements.txt a nainštalujeme ich nasledovne:
Príkazy spustíme v koreňovom súbore následovne:

- apt install portaudio19-dev
- python3.8 -m pip install -r requirements.txt
## Spustenie
V zložke rsc/ sa nachádza ukážkový vstupný súbor example.xml.
V zložke src/ sa nachádzajú zdrojové súbory programu.
Uvedene príkazy je potrebne spúšťať v koreňovom súbore.

Pre spustenie nápovedy, ktorá obsahuje kompletný zoznam argumentov s popisom je nasledovný:

 - python3.8 src/variator.py --help

Príkaz pre ukážkové spustenie s variáciou opakovaním je:

 - python3.8 src/variator.py -i rsc/example.xml -r
