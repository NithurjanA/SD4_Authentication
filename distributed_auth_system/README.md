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


### **Erklärungen zu den Abschnitten und Designentscheidungen**

### **password_auth_service/**
Dieser Ordner enthält den Code für die Username/Passwort-basierte Authentifizierung.

#### **Komponenten**:
- **main.py**:  
  - Enthält die Endpunkte für die Benutzerregistrierung (`/register`) und die Benutzeranmeldung (`/login`).  
  - Diese Endpunkte validieren die eingegebenen Benutzerdaten und speichern sie sicher in einer Datenbank (oder in-memory als Proof-of-Concept).  
  - **Designentscheidung**: Passwörter werden mit einer Hashing-Funktion (`werkzeug.security`) gespeichert, um sicherzustellen, dass sie nicht im Klartext vorliegen. Dies schützt vor Datenlecks und macht kompromittierte Passwörter schwer zugänglich.

- **requirements.txt**:  
  - Listet die Python-Bibliotheken, die für diesen Service erforderlich sind, wie `Flask` und `Werkzeug`.

- **Dockerfile**:  
  - Definiert die Konfiguration, um den Service in einem Docker-Container auszuführen.  
  - **Designentscheidung**: Durch die Containerisierung wird sichergestellt, dass der Service in einer isolierten Umgebung unabhängig von der Host-Konfiguration läuft.

---

### **sample_service/**
Dieser Ordner enthält den Beispielservice, der beide Authentifizierungsmethoden integriert.

#### **Komponenten**:
- **main.py**:  
  - Greift auf beide Authentifizierungsservices zu (Token- und Username/Passwort-basierte Authentifizierung).  
  - Endpunkte wie `/secure-data` prüfen die Gültigkeit eines JWTs, während `/profile` auf Benutzerdaten mit Username und Passwort zugreift.  
  - **Designentscheidung**: Dieser Service zeigt, wie beide Authentifizierungsmethoden kombiniert und in einer Anwendung verwendet werden können.

- **requirements.txt**:  
  - Listet die Abhängigkeiten, die für den Beispielservice benötigt werden, einschließlich Bibliotheken zur Kommunikation mit den Authentifizierungsservices.

- **Dockerfile**:  
  - Containerisiert den Beispielservice, um eine konsistente Umgebung für die Ausführung zu gewährleisten.  
  - **Designentscheidung**: Dieser Ansatz ermöglicht, den Beispielservice unabhängig von den Authentifizierungsservices auszuführen und zu testen.

---

### **token_auth_service/**
Dieser Ordner enthält den Code für die JWT-basierte Authentifizierung.

#### **Komponenten**:
- **main.py**:  
  - Implementiert die Endpunkte `/generate-token` und `/validate-token`.  
  - **Designentscheidung**: 
    - Tokens werden mit einer Signatur (HMAC-SHA256) generiert, um ihre Integrität zu gewährleisten.  
    - Claims wie `iat` (Issued At) und `exp` (Expiration) werden genutzt, um sicherzustellen, dass Tokens zeitlich eingeschränkt gültig sind.

- **requirements.txt**:  
  - Enthält die Bibliotheken, die für die Implementierung der Token-Authentifizierung erforderlich sind, wie `PyJWT`.

- **Dockerfile**:  
  - Containerisiert den Service, um sicherzustellen, dass die Token-Verarbeitung unabhängig von anderen Services funktioniert.

---

### **docker-compose.yml**
Ermöglicht die gleichzeitige Ausführung aller Services in separaten Containern.

#### **Designentscheidung**:
- Koordiniert die Services (`password_auth_service`, `token_auth_service`, `sample_service`) und stellt sicher, dass sie in einer definierten Netzwerkumgebung kommunizieren können.
- **Vorteil**: Entwickler können die gesamte Anwendung mit einem einzigen Befehl starten und testen.

---

### **README.md**
Dokumentiert das Projekt, einschließlich:
- **Beschreibung der Authentifizierungsmethoden**: Erklärt die Verwendung von Tokens und Username/Passwort.
- **Schritte zur Einrichtung**: Führt durch die Installation der Abhängigkeiten, den Start der Services und das Testen mit Postman.
- **Designentscheidungen**: Bietet Hintergrundinformationen zu den gewählten Technologien und ihrer Implementierung.


---

## **Voraussetzungen**

1. **[Docker](https://www.docker.com/products/docker-desktop/)**: Version 20.10 oder neuer.  
   Lade Docker Desktop für Windows, macOS oder Linux herunter, um Container zu erstellen und auszuführen.

2. **[Postman](https://www.postman.com/downloads/)**: Für API-Tests.  
   Lade Postman herunter, um HTTP-Anfragen an deine API zu senden und die Antworten zu testen.

3. **[Git](https://git-scm.com/downloads/)**: Zum Klonen des Repositories.  
   Installiere Git, um Repositories von Plattformen wie GitHub zu clonen und Änderungen zu verwalten.

---

## **Schritt 1: Git Repository Clonen**

**Wichtig:** Bitte wie unter Kapitel Voraussetzung beschrieben zuerst Git installieren, bevor diese Schritte durchgeführt werden.

### Schritte
1. Öffne die  Eingabeaufforderung.  

2. Navigiere zu dem Ordner, in dem du das Repository speichern möchtest:  

   ```bash
   cd pfad/zum/ordner

3. Clone das Repository mit folgendem Befehl:
    ```bash
    git clone https://github.com/NithurjanA/SD4_Authentication.git

4. Git erstellt automatisch einen neuen Ordner mit dem Namen des Repositories (SD4_Authentication) und lädt alle Dateien in diesen Ordner.

Jetzt sollten die Daten aus dem Git-Repository auf deinem Computer im angegebenen Pfad heruntergeladen worden sein, und du kannst mit dem nächsten Schritt fortfahren.

---

## **Schritt 2: Docker starten und docker-compose ausführen**

### Docker starten und ausführen
1. Die Anwendung "Docker Desktop" starten, da es ausgeführt sein muss.

![alt text](image-1.png)

2. Öffne die Eingabeaufforderung.

3. Navigiere zum Pfad wo Github heruntergeladen wurde und gehe eine Ebene im Ordner SD4_Authentication rein zu "distributed_auth_system". Ungefähr so sollte sollte es aussehen (je nach Speicherort sieht es bei dir anders aus):
![alt text](image-2.png)

4. Führe den folgenden Befehl aus, um alle Services zu bauen und zu starten:
    ```bash
    docker-compose up --build

### **Verfügbare Services**

Nach dem erfolgreichen Start von `docker-compose up --build` sind die folgenden Services aktiv:

#### **1. Password Auth Service**
- **URL:** [http://localhost:5000](http://localhost:5000)
- **Beschreibung:** 
  Dieser Service bietet die Username/Passwort-basierte Authentifizierung. Er ist unter der IP-Adresse `http://127.0.0.1:5000` verfügbar.
- **Verfügbare Endpunkte:**
  - `POST /register`: Registriert neue Benutzer.
  - `POST /login`: Authentifiziert bestehende Benutzer.
---

#### **2. Token Auth Service**
- **URL:** [http://localhost:5001](http://localhost:5001)
- **Beschreibung:** 
  Dieser Service implementiert die Token-basierte Authentifizierung mit JSON Web Tokens (JWT). Er ist unter der IP-Adresse `http://127.0.0.1:5001` verfügbar.
- **Verfügbare Endpunkte:**
  - `POST /generate-token`: Generiert ein neues Token für autorisierte Benutzer.
  - `POST /validate-token`: Validiert ein bestehendes Token.
---

#### **3. Sample Service**
- **URL:** [http://localhost:5002](http://localhost:5002)
- **Beschreibung:** 
  Der Beispielservice zeigt, wie die beiden Authentifizierungsmethoden integriert werden. Er ist unter der IP-Adresse `http://127.0.0.1:5002` verfügbar.
- **Verfügbare Endpunkte:**
  - `POST /secure-data`: Zugriff auf geschützte Daten mit einem gültigen JWT.
  - `POST /profile`: Ruft Benutzerprofile basierend auf Username/Passwort-Authentifizierung ab.
---

## **Schritt 3: Services testen**

Bitte wie unter Kapitel Voraussetzungen beschrieben zuerst Postman installieren, bevor diese Schritte durchgeführt werden.

Jetzt testen wir die einzelnen Services nacheinander.

### **1. Password Auth Service**

#### 1. Benutzerregistierung
1. Postman öffnen
2. Klicke auf "New" und wähle "HTTP".
3. Wähle die Methode POST.
4. Gib die URL ein: http://localhost:5000/register.
5. Gehe zum Tab Body, wähle raw und stelle sicher, dass JSON ausgewählt ist.
6. Füge diesen Inhalt in den Body ein mit der gewünschen Benutzername und Passwort:

![alt text](image-3.png)

7. Klicke auf Send.

Erwartete Antwort:

![alt text](image-4.png)

Wenn eine Angabe fehlt oder nicht korrekt eingegeben wurde, erscheint unten im Body eine Fehlermeldung. Wenn alles korrekt ist, sollte die Registrierung problemlos funktionieren.

#### 2. Benutzerlogin
Nachdem ein Benutzer registriert wurde, können wir verifizieren, ob der Login mit den angegebenen Daten erfolgreich ist.
1. Postman öffnen
2. Klicke auf "New" und wähle "HTTP".
3. Wähle die Methode POST.
4. Gib die URL ein: http://localhost:5000/login.
5. Gehe zum Tab Body, wähle raw und stelle sicher, dass JSON ausgewählt ist.
6. Füge diesen Inhalt in den Body ein mit der korrekten Benutzername und Passwort:

![alt text](image-5.png)

7. Klicke auf Send.

Erwartete Antwort:

![alt text](image-6.png)

Wenn der Benutzername oder das Passwort nicht korrekt ist, erscheint eine Fehlermeldung wie im folgenden Screenshot:

![alt text](image-7.png)

---

### **2. Token Auth Service**

Hier testen wir den Service, der JSON Web Tokens (JWT) generiert.

#### 1. Token Generierung
1. Postman öffnen
2. Klicke auf "New" und wähle "HTTP".
3. Wähle die Methode POST.
4. Gib die URL ein: http://localhost:5001/generate-token.
5. Lass den Tab Body leer (dieser Endpunkt benötigt keinen Body).
6. Klicke auf Send.

Erwartete Antwort:
Es sollte ein Token,wie im nachfolgenden Bild ersichtlich ist, generiert und angezeigt werden.

![alt text](image-8.png)

Kopiere den Token und speichere ihn in der Zwischenablage, da du ihn für den nächsten Schritt benötigst.

#### 2. Token Validierung
1. Postman öffnen
2. Klicke auf "New" und wähle "HTTP".
3. Wähle die Methode POST.
4. Gib die URL ein: http://localhost:5001/validate-token.
5. Gehe zum Tab Body, wähle raw, und stelle sicher, dass JSON ausgewählt ist.
6. Füge diesen Inhalt in den Body ein, wobei der angezeigte Token durch den generierten Token, die du im vorherigen Schritt kopiert hast, ersetzt wird:

![alt text](image-9.png)
7. Klicke auf Send.

Erwartete Resultat:

![alt text](image-10.png)

#### Beschreibung der Ausgabe:
- **"decoded"**: iat (Issued at) zeigt wenn der Token erstellt wurde und exp (Expiration) zeigt den Zeitpunkt, zu dem der Token abläuft.
- **"message"**: Token is valid Bedeutet, dass der übermittelte Token korrekt signiert ist und innerhalb seiner Gültigkeitsdauer liegt.

Wenn der Token nicht gültig ist, erscheint eine Fehlermeldung wie:

![alt text](image-11.png)

---

### **3. Sample Services**
Mit einem gültigen Token können wir nun geschützte Daten abrufen.
1. Postman öffnen
2. Klicke auf "New" und wähle "HTTP".
3. Wähle die Methode POST.
4. Gib die URL ein: http://localhost:5002/secure-data.
5. Gehe zum Tab Body, wähle raw, und stelle sicher, dass JSON ausgewählt ist.
6. Füge diesen Inhalt in den Body ein, wobei der angezeigte Token durch den generierten Token, die du im vorherigen Schritt kopiert hast, ersetzt wird:

![alt text](image-12.png)
7. Klicke auf Send.

Erwartete Antwort:

![alt text](image-13.png)

Der Zugriff wird nur gewährt, wenn der Token gültig ist.

#### Wozu dieser Schritt:
- **Zugriffskontrolle:** Der Endpunkt prüft, ob ein gültiges Token im Body der Anfrage übermittelt wurde. Nur wenn das Token gültig ist (z. B. nicht abgelaufen und korrekt signiert), erhält der Benutzer Zugriff auf die geschützten Daten.
- **Sicherheit:** Die geschützten Daten werden nicht an Benutzer ausgegeben, die kein gültiges Token übermitteln. Dadurch wird sichergestellt, dass nur authentifizierte und autorisierte Benutzer auf die Daten zugreifen können.
- **Praktisches Beispiel:** In einer realen Anwendung könnte dieser Endpunkt sensible Informationen wie Benutzerdaten, Rechnungen oder andere geschützte Ressourcen bereitstellen. Das Beispiel hier zeigt, dass ein gültiges Token den Zugriff auf eine einfache Antwort wie "Secure data with Token Auth" gewährt.

Wenn der Token nicht gültig ist, wird die nachfolgende Fehlermeldung angezeigt:

![alt text](image-14.png)

---

### **4. Benutzerprofil abrufen**
Hier rufen wir Benutzerprofile mit Benutzername und Passwort ab.
1. Postman öffnen
2. Klicke auf "New" und wähle "HTTP".
3. Wähle die Methode POST.
4. Gib die URL ein: http://localhost:5002/profile.
5. Gehe zum Tab Body, wähle raw, und stelle sicher, dass JSON ausgewählt ist.
6. Füge diesen Inhalt in den Body ein:

![alt text](image-15.png)
7. Klicke auf Send.

Erwartete Resultat:

![alt text](image-16.png)

Wenn Benutzername oder Passwort nicht korrekt sind, wird eine Fehlermeldung angezeigt:

![alt text](image-17.png)

---

## Trade-offs und Herausforderungen der Authentifizierungsmethoden

In diesem Projekt werden zwei Authentifizierungsmethoden verwendet: **Token-basierte Authentifizierung** und **Username/Passwort-basierte Authentifizierung**. Beide Ansätze haben spezifische Vor- und Nachteile, die bei der Auswahl der geeigneten Methode in verteilten Systemen berücksichtigt werden müssen.

### Token-basierte Authentifizierung

**Vorteile:**
- **Skalierbarkeit:**
  - Tokens können wiederverwendet werden, ohne dass der Authentifizierungsserver bei jeder Anfrage belastet wird.
  - Ideal für hochfrequentierte Systeme und Microservices-Architekturen.
- **Effizienz:**
  - Nach der ersten Authentifizierung können Clients einfach das Token mit jeder Anfrage senden, wodurch die Latenzzeiten reduziert werden.
- **Flexibilität:**
  - Tokens enthalten Claims (z. B. `iat` und `exp`), die zusätzliche Informationen über den Benutzer und den Token bereitstellen. Dadurch wird eine granulare Zugriffskontrolle ermöglicht.

**Nachteile:**
- **Sicherheitsrisiken:**
  - Wenn ein Token kompromittiert wird (z. B. durch Abfangen), kann ein Angreifer auf geschützte Ressourcen zugreifen, bis der Token abläuft.
  - Zusätzliche Sicherheitsmaßnahmen wie Token-Revocation oder kurze Ablaufzeiten (`exp`) sind erforderlich.
- **Komplexität:**
  - Die Implementierung von Mechanismen wie Token-Erstellung, -Validierung und -Widerruf erfordert zusätzliche Entwicklungsressourcen.

---

### Username/Passwort-basierte Authentifizierung

**Vorteile:**
- **Einfachheit:**
  - Die Implementierung ist unkompliziert und für viele Entwickler vertraut.
  - Es sind keine zusätzlichen Mechanismen wie Token-Management erforderlich.
- **Direkte Kontrolle:**
  - Benutzeranmeldedaten werden bei jeder Anfrage direkt überprüft, was besonders in kleineren Anwendungen ausreichend ist.

**Nachteile:**
- **Geringere Skalierbarkeit:**
  - Jede Anfrage erfordert eine erneute Validierung der Benutzeranmeldeinformationen, was den Server bei hoher Last stark belasten kann.
- **Erhöhtes Risiko bei der Übertragung:**
  - Benutzeranmeldedaten müssen bei jeder Anfrage über das Netzwerk gesendet werden. Ohne sichere Verbindungen (z. B. HTTPS) besteht ein hohes Risiko des Abfangens (Man-in-the-Middle-Angriffe).

---

### Zusammenfassung der Herausforderungen

- **Leistung vs. Sicherheit:**  
  Während Token-basierte Authentifizierung leistungsfähiger ist, erfordert sie zusätzliche Sicherheitsmechanismen, um Missbrauch zu verhindern.

- **Einsatzszenarien:**  
  Die Wahl der Methode hängt von den Anforderungen ab:
  - **Token-basierte Authentifizierung:** Geeignet für verteilte Systeme mit hoher Last und mehreren Microservices.
  - **Username/Passwort-basierte Authentifizierung:** Ideal für einfache oder zentralisierte Anwendungen.

---

## Token Management-Strategie

Das Projekt verwendet **JSON Web Tokens (JWT)** zur Token-basierten Authentifizierung. Die Tokens sind **signiert**, aber nicht verschlüsselt, um eine Balance zwischen Sicherheit und Effizienz zu gewährleisten.

### Eigenschaften der Tokens

1. **Signatur (HMAC-SHA256):**
   - Tokens werden mit dem Algorithmus **HS256** signiert, um die **Integrität** des Inhalts zu gewährleisten.
   - Die Signatur garantiert, dass der Token-Inhalt (Header und Payload) nicht manipuliert wurde.
   - **Warum keine Verschlüsselung?**
     - Da der Token keine sensiblen Informationen enthält (wie Passwörter), ist eine Verschlüsselung nicht erforderlich.
     - Die Signatur reicht aus, um sicherzustellen, dass der Token unverändert bleibt.

2. **Claims im Token:**
   - **`iat` (Issued At):**
     - Gibt an, wann der Token erstellt wurde (Unix-Zeitstempel).
     - Dieser Claim stellt sicher, dass der Token nicht vor einer bestimmten Zeit gültig ist.
     - Beispiel: `"iat": 1702213200` (entspricht 10. Dezember 2024, 18:00 Uhr UTC).
   - **`exp` (Expiration):**
     - Gibt das Ablaufdatum des Tokens an.
     - Nach dem angegebenen Zeitpunkt wird der Token als ungültig betrachtet und muss erneuert werden.
     - Dieser Claim minimiert das Risiko, dass ein kompromittierter Token langfristig missbraucht wird.
     - Beispiel: `"exp": 1702216800` (entspricht 10. Dezember 2024, 19:00 Uhr UTC).

---

### Warum diese Strategie?

1. **Effizienz:**
   - Signierte Tokens benötigen weniger Rechenressourcen als verschlüsselte Tokens und sind daher ideal für skalierbare Systeme.
   - Clients können den Token wiederholt verwenden, ohne sich bei jedem API-Aufruf neu zu authentifizieren.

2. **Sicherheit:**
   - Die Claims `iat` und `exp` helfen, den Missbrauch von Tokens zu minimieren:
     - **`iat`** verhindert, dass ein Token vor seiner Erstellung verwendet wird.
     - **`exp`** stellt sicher, dass Tokens nach einer festgelegten Zeit ablaufen und reduziert die Auswirkungen von gestohlenen Tokens.

3. **Flexibilität:**
   - Mit Claims wie `iat` und `exp` kann die Gültigkeit eines Tokens dynamisch gesteuert werden.
   - Weitere Claims können hinzugefügt werden, z. B. Benutzerrollen (`role`) oder Zugriffsrechte (`scope`).

---

### Mögliche Erweiterungen

1. **Token-Revocation:**
   - Ergänzung einer Blacklist, um Tokens vor Ablaufzeit ungültig zu machen.
   - Nützlich in Szenarien, in denen ein Benutzer manuell abgemeldet wird oder ein Token kompromittiert wurde.

2. **Kurzfristige Tokens und Refresh Tokens:**
   - Einsatz von kurzen Ablaufzeiten für Access Tokens.
   - Einführung von Refresh Tokens, um neue Access Tokens zu generieren, ohne den Benutzer erneut zu authentifizieren.

Diese Strategie stellt eine sichere und flexible Implementierung der Token-basierten Authentifizierung dar und kann je nach Bedarf erweitert werden.

