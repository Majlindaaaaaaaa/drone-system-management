# 5. Arkitektura e Sistemit

Sistemi “Drone System Management – Kosovo” është ndërtuar mbi një arkitekturë të ndarë në shtresa (layered architecture), e cila siguron modularitet, mirëmbajtje të lehtë dhe zgjerueshmëri në të ardhmen.

Arkitektura bazohet në modelin **Client–Server**, ku frontend-i dhe backend-i janë të ndarë qartë dhe komunikojnë përmes API-ve REST.

---

## 5.1 Pamje e Përgjithshme e Arkitekturës

Arkitektura e sistemit përbëhet nga tre komponentë kryesorë:

1. **Frontend (Client)**
2. **Backend (API Server)**
3. **Logjika e Trajektores (AI – Simulim)**

Komunikimi ndërmjet këtyre komponentëve realizohet përmes protokollit HTTP duke përdorur formate JSON për shkëmbimin e të dhënave.

---

## 5.2 Frontend – Shtresa e Prezantimit

Frontend-i përfaqëson ndërfaqen me të cilën përdoruesi ndërvepron drejtpërdrejt.

### Funksionet kryesore të frontend-it:
- Mundëson zgjedhjen e pikës së nisjes (origin).
- Mundëson zgjedhjen e destinacionit (destination).
- Dërgon kërkesë për krijimin e fluturimit në backend.
- Merr dhe shfaq trajektoren e fluturimit në hartë.
- Paraqet vizualisht pikat dhe vijën e fluturimit.

Frontend-i është ndërtuar duke përdorur komponentë të ndarë, ku secili komponent ka një rol të qartë (formular, hartë, kontroll logjik).

---

## 5.3 Backend – Shtresa e Logjikës dhe Shërbimeve

Backend-i është përgjegjës për përpunimin e të dhënave dhe menaxhimin e logjikës së sistemit.

### Roli i backend-it:
- Pranon kërkesa nga frontend-i (POST dhe GET).
- Validon të dhënat e dërguara nga përdoruesi.
- Krijon dhe ruan fluturimet në memorie (simulim).
- Gjeneron trajektoren e fluturimit.
- Kthen përgjigje të strukturuara në format JSON.

Backend-i është ndërtuar në mënyrë modulare, ku çdo funksionalitet është i ndarë në file dhe folderë të veçantë (routes, models, ai).

---

## 5.4 Rrugët (Routes) dhe API Endpoint-et

Backend-i ofron disa endpoint-e REST, të cilat përdoren nga frontend-i:

### Endpoint-et kryesore:
- **GET /**  
  Kontrollon nëse API është aktive.

- **POST /flights/**  
  Krijon një fluturim të ri bazuar në origin dhe destination.

- **GET /flights/**  
  Liston të gjitha fluturimet e krijuara.

- **GET /flights/{flight_id}/trajectory**  
  Gjeneron dhe kthen trajektoren e fluturimit për një fluturim të caktuar.

Këto endpoint-e janë të dokumentuara automatikisht përmes Swagger (FastAPI Docs).

---

## 5.5 Logjika e Trajektores (AI – Simulim Akademik)

Gjenerimi i trajektores së fluturimit realizohet përmes një algoritmi të thjeshtuar që simulon inteligjencën artificiale.

### Karakteristikat e këtij moduli:
- Merr si input pikën e nisjes dhe destinacionin.
- Gjeneron pika të ndërmjetme midis dy koordinatave.
- Krijon një vijë fluturimi të vazhdueshme.
- Simulon një rrugë reale fluturimi të dronit.

Ky modul nuk përdor AI të avancuar reale, por përfaqëson një **simulim akademik**, i cili është i përshtatshëm për qëllime mësimore dhe demonstrative.

---

## 5.6 Rrjedha e të Dhënave (Data Flow)

Rrjedha e të dhënave në sistem funksionon sipas këtij hapi:

1. Përdoruesi zgjedh origin dhe destination në frontend.
2. Frontend-i dërgon kërkesë POST në backend.
3. Backend-i krijon fluturimin dhe ruan të dhënat.
4. Frontend-i kërkon trajektoren për fluturimin e krijuar.
5. Backend-i gjeneron trajektoren dhe e kthen përgjigjen.
6. Frontend-i shfaq pikat dhe vijën në hartë.

Ky proces siguron një komunikim të qartë dhe të kontrolluar ndërmjet komponentëve.

---

## 5.7 Avantazhet e Arkitekturës së Zgjedhur

Arkitektura e përdorur ofron disa avantazhe kryesore:

- Ndarje e qartë e përgjegjësive.
- Lehtësi në mirëmbajtje dhe zgjerim.
- Mundësi integrimi me sisteme reale në të ardhmen.
- E përshtatshme për punë ekipore dhe zhvillim akademik.

---

## 5.8 Përmbledhje

Arkitektura e sistemit është ndërtuar në mënyrë të strukturuar dhe profesionale, duke siguruar funksionalitet të plotë dhe një bazë të fortë për zhvillime të mëtejshme. Ndarja frontend–backend dhe përdorimi i moduleve të veçanta e bën sistemin të qartë, të kuptueshëm dhe të qëndrueshëm.
