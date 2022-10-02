# Planung und Konzeption
---
### welche Bewegungsprofile erkannt werden sollen und mit welcher erhofften Genauigkeit (Ziel)
- Gehen / Laufen
- Joggen
- Sitzen
- Velo fahren

---
In Hosentasche

Erwartung: 90% mit deep learning und 80% ohne deep learning

### was genau im Projekt erreicht werden soll / was nicht (Scope)

In Scope:
- mit csv files
- vergleichen von Modellen die verschiedene Sensoren nutzen
- vergleichen von verschiedenen Modellen (deep learning vs logistic regression, ...)
- explorative Datenanalyse (verschiedene Profile  für verschiedene Sensoren explorativ vergleichen)

Out of Scope:
- application with real time data
- only data by two people
- Verschieden Positionen von Smartphone (pro Bewegungsprofil nur eine Position)

### was es für Milestones gibt und wann diese etwa erreicht sein sollen (Planung)
- Daten sammeln
- Daten verarbeiten (reinigen)
- Modelle erstellen (und Experimente dokumentieren)
- Bericht fertigstellen

### wie das Vorgehen für die Datensicherung und Beschriftung (Label), die Datenverarbeitung, sowie die Modellierung ist (Konzept)
- Immer Blöcke von 20 Minuten und eine Aktivität aufzeichnen. Diese Daten dann als csv mit Name der Aktivität und Aufnahmegerät / Position im Titel speichern. (Velo-Fahren aufwärts / abwärts)
- Anfang und Ende von den Files entfernen
- Schauen, dass wir es zusammenführen können (gleiche Spalten in den Files)
- Daten aggregieren?
- Weights & Biases zum tracken der Experimente nutzen?

### in welcher Form die Erkenntnisse präsentiert werden sollen (Output)
- Bericht
    - Vergleich Approaches
    - Vergleich der Modelle (welche Hyperparameter wurden genutzt, warum?)
    - Lernings
    - Verbesserungsideen
    - Explorative Datenanalyse
- Presentation der Ergebnisse