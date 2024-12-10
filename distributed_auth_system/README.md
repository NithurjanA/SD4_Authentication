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

1. **Docker**: Version 20.10 oder neuer.
2. **Postman**: Für API-Tests.
3. **Git**: Zum Klonen des Repositories.

---