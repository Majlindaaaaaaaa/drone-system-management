# 6. Implementimi i Sistemit

Ky kapitull përshkruan implementimin e sistemit **“Drone System Management – Kosovo”**, i zhvilluar si një platformë akademike për menaxhimin dhe vizualizimin e fluturimeve të dronave në mënyrë të simuluar. Implementimi është realizuar duke ndjekur parimet e **Systems Engineering** dhe **Challenge-Based Learning (CBL)**.

Sistemi është ndërtuar sipas arkitekturës **client–server**, duke ndarë qartë komponentët e backend-it dhe frontend-it.

---

## Backend

Backend-i është zhvilluar me **Python** dhe **FastAPI**. Ai ofron API për:
- krijimin e fluturimeve,
- ruajtjen e pikës së nisjes dhe destinacionit,
- gjenerimin e trajektores së fluturimit përmes një moduli të thjeshtë **AI**.

Logjika e trajektores gjeneron automatikisht pika ndërmjet dy qyteteve, duke simuluar planifikimin e rrugës së dronit.

---

## Frontend

Frontend-i është zhvilluar me **Vue.js (Vite)** dhe përfshin:
- një formë për zgjedhjen e **origin** dhe **destination**,
- butonin **Create Flight**,
- një hartë interaktive të ndërtuar me **Leaflet**, ku shfaqen pikat A dhe B si dhe trajektorja e fluturimit.

Ndërfaqja është e thjeshtë, e përqendruar dhe e orientuar drejt përdoruesit.

---

## Integrimi i Sistemit

Frontend-i dhe backend-i komunikojnë përmes thirrjeve REST API. Ky integrim demonstron funksionimin e një sistemi të plotë, ku të dhënat krijohen në frontend, përpunohen në backend dhe vizualizohen në kohë reale në hartë.

---

## Përfundim

Implementimi i sistemit demonstron aplikimin praktik të koncepteve të **Systems Engineering**, integrimin e teknologjive të ndryshme dhe zgjidhjen e një problemi real përmes një qasjeje ndërdisiplinore dhe akademike.
