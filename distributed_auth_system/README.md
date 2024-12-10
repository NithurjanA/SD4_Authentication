# Authentication Service

Dieses Projekt implementiert ein Proof-of-Concept (PoC) für ein **Authentifizierungssystem** in einer verteilten Anwendung. Es bietet zwei Authentifizierungsmethoden: **Token-basierte Authentifizierung** und **Username/Passwort-basierte Authentifizierung**.

---

## **Projektübersicht**

- **Ziel:** Demonstration von Authentifizierungstechniken in einer verteilten Architektur.
- **Ansatz:** Vergleich und Integration von Token- und Username/Passwort-basierten Authentifizierungsmethoden.
- **Ergebnis:** Ein vollständig funktionales, containerisiertes System, das die Grundlagen moderner Authentifizierungsmethoden zeigt.

---

## **Projektstruktur**
distributed_auth_system/ │ ├── token_auth_service/ # Service für JWT-basierte Authentifizierung │ ├── main.py # Hauptcode │ ├── requirements.txt # Abhängigkeiten │ └── Dockerfile # Docker-Konfiguration │ ├── password_auth_service/ # Service für Username/Passwort-Authentifizierung │ ├── main.py # Hauptcode │ ├── requirements.txt # Abhängigkeiten │ └── Dockerfile # Docker-Konfiguration │ ├── sample_service/ # Beispielservice, der beide Methoden verwendet │ ├── main.py # Hauptcode │ ├── requirements.txt # Abhängigkeiten │ └── Dockerfile # Docker-Konfiguration │ ├── docker-compose.yml # Orchestrierung aller Services └── README.md # Projektdokumentation


---

## **Voraussetzungen**

1. **Docker**: Version 20.10 oder neuer.
2. **Postman**: Für API-Tests (optional).
3. **Git**: Zum Klonen des Repositories.

---