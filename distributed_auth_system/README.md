# Authentication Service

Dieses Projekt implementiert ein Proof-of-Concept (PoC) für ein **Authentifizierungssystem** in einer verteilten Anwendung. Es unterstützt zwei Authentifizierungsmethoden: **Token-basierte Authentifizierung** und **Username/Passwort-basierte Authentifizierung**. 

## Features

- **Token-basierte Authentifizierung**
  - Generiert JWT-Tokens mit Ablaufzeit und überprüft deren Gültigkeit.
- **Username/Passwort-basierte Authentifizierung**
  - Authentifiziert Benutzer mit einem Benutzernamen und Passwort.
  - Speichert Passwörter sicher mit Passwort-Hashing (Werkzeug).

## Voraussetzungen

Stelle sicher, dass du die folgenden Programme installiert hast:

- [Python 3.10 oder höher](https://www.python.org/downloads/)
- [pip (Python Package Installer)](https://pip.pypa.io/en/stable/)

Zusätzlich benötigst du die Python-Bibliotheken **Flask** und **Werkzeug**. Diese kannst du installieren, wie in der Anleitung unten beschrieben.

## Installation

1. Klone das Repository (falls es online gespeichert ist) oder lade die Projektdateien herunter.

   ```bash
   git clone <repository-url>
   cd Authentication