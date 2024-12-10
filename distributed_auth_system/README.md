# Authentication Service

Dieses Projekt implementiert ein Proof-of-Concept (PoC) für ein **Authentifizierungssystem** in einer verteilten Anwendung. Es bietet zwei Authentifizierungsmethoden: **Token-basierte Authentifizierung** und **Username/Passwort-basierte Authentifizierung**.

---

## **Projektübersicht**

- **Ziel:** Demonstration von Authentifizierungstechniken in einer verteilten Architektur.
- **Ansatz:** Vergleich und Integration von Token- und Username/Passwort-basierten Authentifizierungsmethoden.
- **Ergebnis:** Ein vollständig funktionales, containerisiertes System, das die Grundlagen moderner Authentifizierungsmethoden zeigt.

---

## **Projektstruktur**
![alt text](image.png)
*Abbildung: Ordnerstruktur des Projekts*

---

## **Erklärungen zu den Abschnitten**

### **password_auth_service/**
Dieser Ordner enthält den Code für die Username/Passwort-basierte Authentifizierung.

- **main.py**: Der Hauptcode, der die Endpunkte für Benutzerregistrierung und -Authentifizierung implementiert.
- **requirements.txt**: Die benötigten Python-Abhängigkeiten für diesen Service.
- **Dockerfile**: Zum Containerisieren des Services.

---

### **sample_service/**
Dieser Ordner enthält den Beispielservice, der beide Authentifizierungsmethoden integriert.

- **main.py**: Der Hauptcode, der auf die beiden Authentifizierungsservices zugreift.
- **requirements.txt**: Die benötigten Python-Abhängigkeiten.
- **Dockerfile**: Zum Containerisieren des Services.

---

### **token_auth_service/**
Dieser Ordner enthält den Code für die JWT-basierte Authentifizierung.

- **main.py**: Der Hauptcode, der die Endpunkte für Token-Generierung und -Validierung implementiert.
- **requirements.txt**: Die benötigten Python-Abhängigkeiten für diesen Service.
- **Dockerfile**: Zum Containerisieren des Services.

---

### **docker-compose.yml**
Ermöglicht die gleichzeitige Ausführung aller Services in Containern.

---

### **README.md**
Dokumentation des Projekts.

---

## **Voraussetzungen**

1. **[Docker](https://www.docker.com/products/docker-desktop/)**: Version 20.10 oder neuer.  
   Lade Docker Desktop für Windows, macOS oder Linux herunter, um Container zu erstellen und auszuführen.

2. **[Postman](https://www.postman.com/downloads/)**: Für API-Tests.  
   Lade Postman herunter, um HTTP-Anfragen an deine API zu senden und die Antworten zu testen.

3. **[Git](https://git-scm.com/downloads/)**: Zum Klonen des Repositories.  
   Installiere Git, um Repositories von Plattformen wie GitHub zu clonen und Änderungen zu verwalten.

---

## **Git Repository Clonen**

**Wichtig:** Bitte zuerst Git installieren, bevor diese Schritte durchgeführt werden.

### Schritt: Repository clonen

1. Öffne das Terminal oder die Eingabeaufforderung.  

2. Navigiere zu dem Ordner, in dem du das Repository speichern möchtest:  

   ```bash
   cd pfad/zum/ordner

3. Clone das Repository mit folgendem Befehl:
git clone https://github.com/NithurjanA/SD4_Authentication.git

4. Git erstellt automatisch einen neuen Ordner mit dem Namen des Repositories (SD4_Authentication) und lädt alle Dateien und die Versionshistorie in diesen Ordner.

Jetzt sollten die Daten aus dem Git-Repository auf deinem Computer im angegebenen Pfad heruntergeladen worden sein, und du kannst mit dem nächsten Schritt fortfahren.

---

