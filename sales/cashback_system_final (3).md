# Documentatie Beloningssysteem: Consumentenpanel App

**Conversiekoers:** 10.000 punten = €10,00 (100 punten = €0,10)
**Minimale uitbetalingsdrempel:** €10,00

---

## 1. De Basisregels & Wielen
Het systeem maakt gebruik van twee gamification-wielen met een vaste wiskundige *Expected Value* (EV).

* **Standaard Rad (Standaard Spin):** EV = 100 punten (€0,10)
* **Premium Rad (Premium Spin):** EV = 200 punten (€0,20)

**De "Grote Kar" Bonus (Definitie & Base Reward)**
Een "Grote Kar" is objectief gedefinieerd als een kassaticket met een totaalbedrag van **€75,00 of meer**. Alles onder de €75 is een normaal ticket.
* **Standaard Bonus:** +50 punten per volledige schijf van €75 (bijv. €160 = 2 schijven = +100 ptn).
* **Bedrag Cap:** Maximaal berekend tot **€300 per ticket** (maximaal +200 standaard bonuspunten voor 4 schijven).
* **Frequentie Cap (Anti-Fraude):** Gebruikers kunnen *alle* Grote Kar-gerelateerde bonussen op maximaal **6 tickets per kalendermaand** verdienen. 

---

## 2. Het Tier Systeem (Kalendermaand Model)
De status van de gebruiker is gekoppeld aan **kalendermaanden** (niet aan een rollende periode, voor maximale duidelijkheid). Het aantal geüploade tickets in de huidige maand bepaalt de Tier voor de *volgende* maand (bijv. je scans in oktober bepalen je status voor heel november).

| Tier | Voorwaarde | Beloning per Ticket | Grote Kar Bonus (Max 6x/maand) |
| :--- | :--- | :--- | :--- |
| **Brons** | < 4 tickets | 1 Standaard Spin (EV 100) | Standaard schijven (Max +200 ptn) |
| **Zilver** | 4 tot 9 tickets | 1 Standaard Spin + **75 vaste ptn** | Standaard schijven + **25 extra ptn** |
| **Goud** | 10+ tickets | **1 Premium Spin (EV 200)** | Standaard schijven + **50 extra ptn** |

> **Strategische Notitie:** Een regulier Zilver-ticket is hiermee structureel 175 punten waard. Goud (Premium EV van 200) is een overduidelijke upgrade. Zodra een gebruiker de serieuze drempel van €75 passeert, ontgrendelen ze direct de lucratieve Grote Kar bonussen.

---

## 3. Wekelijkse Streak & Continue Streak Rewards
Om wekelijkse activiteit en langdurige gewoontevorming te stimuleren, is er een oplopende bonus. 

**Niveau 1: De Standaard Maand-Streak (Maand 1)**
Totale *Expected Value* bij 4 aaneengesloten weken scannen: **500 punten (€0,50)**.
* **Week 1:** Geen bonus (Start van de cyclus)
* **Week 2:** + 1 Standaard Spin (EV 100 ptn)
* **Week 3:** + 150 vaste punten
* **Week 4 (Climax Maand 1):** + 1 Premium Spin & 50 vaste punten (EV 250 ptn)

**Niveau 2: De Continue Maand-Streak (Maand 2 en verder)**
Als een gebruiker *direct* doorgaat zonder een week te missen, verdubbelt de totale streak reward naar **1.000 punten (€1,00)** per 4 weken. Ze krijgen nu wekelijks een beloning om het momentum vast te houden.
* **Week 1:** **+ 150 vaste punten** *(Loyaliteits-startbonus)*
* **Week 2:** + 1 Standaard Spin & 100 vaste punten (EV 200 ptn)
* **Week 3:** + 1 Standaard Spin & 150 vaste punten (EV 250 ptn)
* **Week 4 (Climax Continue Maand):** + 1 Premium Spin & 200 vaste punten (EV 400 ptn)

*Let op: Mist een gebruiker één week? Dan breekt de continue streak en valt de gebruiker onverbiddelijk terug naar Week 1 van de Standaard Maand-Streak (Niveau 1).*

---

## 4. Fair Use Caps (Het "Waterproof" Systeem)
Om ticket-fraude en data-vervuiling te blokkeren, gelden deze harde limieten:

1.  **Daglimiet:** Maximaal **2 tickets per dag, per supermarktketen**.
2.  **Weeklimiet:** Maximaal **5 tickets per week**.
3.  **Maandlimiet:** Maximaal **15 tickets per maand** (voor het genereren van wielen/basisbeloningen). 
4.  **Grote Kar Limiet:** Maximaal **6 tickets per maand** voor de Grote Kar bonussen.
5.  **De "Streak Saver" (Dead Zone Oplossing):** Tikt een actieve gebruiker de limiet van 15 tickets al in week 3 aan? Dan tellen tickets vanaf nummertje 16 nóg steeds mee voor het behouden van de wekelijkse streak en het Tier-niveau. Ze genereren géén wielen of bedrag-bonussen meer, maar leveren een symbolische **10 vaste punten** op ter compensatie voor de moeite.

---

## 5. Maandelijkse Kostenanalyse (Unit Economics)
Berekend met de schijven van €75, bedrag cap van €300 en Continue Streak van €1,00.

### Scenario A: De Inconsistente Gebruiker (Gemiddeld gedrag, GEEN Streak)
*Profiel: Brons/Zilver. Uploadt regelmatig, maar mist af en toe een week.*
* **Brons (3 tickets, geen Grote Kar):** 3 × 100 ptn = **300 punten (€0,30 per maand)**
* **Zilver (6 tickets, waarvan 2x Grote Kar van ~€75):** 2 × Grote Kar Zilver (175 basis + 50 schijf + 25 bonus = 250 ptn) + 4 × Normale Zilver (175 ptn) = **1.200 punten (€1,20 per maand)**

### Scenario B: De Actieve Gebruiker (Gemiddeld gedrag + Continue Streak Maand 2+)
*Profiel: Haalt de continue streak (€1,00) en uploadt wekelijks betrouwbaar.*
* **Zilver Actief (8 tickets, waarvan 2x Grote Kar van ~€75):** * 2 × Grote Kar Zilver (175 basis + 50 schijven + 25 bonus) = 2 × 250 ptn = 500 ptn
  * 6 × Normale Zilver = 6 × 175 ptn = 1.050 ptn
  * Continue Streak = 1.000 ptn
  * **Totaal Zilver: 2.550 punten (€2,55 per maand)**
* **Goud Gemiddeld (12 tickets, waarvan 6x Grote Kar van ~€75-149):** * 6 × Grote Kar Goud (200 Premium + 50 schijven + 50 bonus) = 6 × 300 ptn = 1.800 ptn
  * 6 × Normale Goud = 6 × 200 ptn = 1.200 ptn
  * Continue Streak = 1.000 ptn
  * **Totaal Goud: 4.000 punten (€4,00 per maand)**

### Scenario C: Ultieme Worst Case (De "Power User" stuitert tegen alle caps + Continue Streak)
*Profiel: Haalt de continue streak (€1,00). Uploadt de maximale 15 tickets. Pakt 6x de absolute maximale Grote Kar bonus (ticketwaarde = €300+). Goud status.*
* 6 tickets met Maximale Grote Kar Goud (200 Premium + 200 schijven + 50 bonus): 6 × 450 ptn = 2.700 ptn
* 9 normale tickets (restant tot de cap van 15): 9 × 200 ptn = 1.800 ptn
* Voltooide Continue Maandstreak: 1.000 ptn
* **Absolute Worst Case Kosten:** 2.700 + 1.800 + 1.000 = **5.500 punten (€5,50 per maand)**

> **Conclusie Unit Economics:** De keuze voor €75 als 'Grote Kar' drempel is enorm motiverend voor de modale Belgische shopper en zorgt ervoor dat ze de app sneller als 'gulle gever' ervaren. Doordat de maximale ticketbonus is afgetopt op €300 (4 schijven), stijgen de kosten aan de achterkant echter niet mee! De voorspelbaarheid blijft fantastisch: Goud Gemiddeld draait rond de **€4,00** en het absolute doemscenario zit potdicht op **€5,50**.

---

## 6. Onboarding & Customer Acquisition Cost (CAC)
Omdat de uitbetalingsdrempel van €10 hoog is, wordt een "Kickstart" strategie gebruikt om *churn* in de eerste weken te voorkomen. 

**De "Kickstart" Welkomstbonus (Totale CAC: ~2.500 punten / €1,70)**
Nieuwe gebruikers doorlopen een fasering voor hun eerste drie geldige tickets:
* **Ticket 1 (De "Aha!"-ervaring):** 500 vaste ptn + 1 Premium Spin (EV 200) + ticketwaarde. 
* **Ticket 2 (De Bevestiging):** 500 vaste ptn + ticketwaarde. 
* **Ticket 3 (De Gewoonte):** 500 vaste ptn + ticketwaarde. Kickstart voltooid!

### 6.1 UI/UX Implementatie van de Opstartfase
1. **De "Kickstart Progress Bar":** Op het dashboard zien nieuwe gebruikers niet de wekelijkse streak, maar een balk met 3 visuele cadeautjes.
2. **Heldere Microcopy:** Boven de balk: *"Welkom! Voltooi je Kickstart en verdien direct €1,70 aan punten."*
3. **Animatie & Beloning:** Bij elke succesvolle upload opent een cadeautje op de balk met feestelijke animatie.
4. **De Transitie (Na ticket 3):** Pop-up: *"Je Kickstart is voltooid! Vanaf nu spaar je voor streaks en de Goud-status!"* De UI verandert naar de reguliere voortgangsbalken.