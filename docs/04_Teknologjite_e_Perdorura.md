# 4. Teknologjitë e Përdorura

Në realizimin e projektit “Drone System Management – Kosovo” janë përdorur teknologji moderne të zhvillimit të aplikacioneve web, të ndara në frontend dhe backend. Zgjedhja e këtyre teknologjive është bërë duke marrë parasysh thjeshtësinë e implementimit, performancën, si dhe përdorimin e tyre të gjerë në industri dhe në mjedise akademike.

Arkitektura e sistemit bazohet në modelin **client-server**, ku frontend-i dhe backend-i komunikojnë përmes API-ve REST.

---

## 4.1 Backend – FastAPI (Python)

Backend-i i sistemit është zhvilluar duke përdorur **FastAPI**, një framework modern për ndërtimin e API-ve në gjuhën programuese Python.

### Arsyet e zgjedhjes së FastAPI:
- Performancë e lartë dhe shpejtësi në ekzekutim.
- Dokumentim automatik i API-ve përmes Swagger (OpenAPI).
- Lehtësi në krijimin e endpoint-eve REST.
- Mbështetje për tipizim statik dhe validim të të dhënave.

### Funksionalitetet kryesore të backend-it:
- Krijimi i fluturimeve të reja të dronëve.
- Ruajtja dhe menaxhimi i të dhënave të fluturimit.
- Gjenerimi i trajektores së fluturimit përmes një algoritmi të thjeshtuar (simulim i AI-së).
- Ofrimi i të dhënave për frontend-in përmes kërkesave HTTP.

Backend-i shërben si bërthama logjike e sistemit dhe është përgjegjës për përpunimin e të gjitha të dhënave.

---

## 4.2 Frontend – Vue.js & Vite

Frontend-i është zhvilluar duke përdorur **Vue.js**, një framework progresiv për ndërtimin e ndërfaqeve përdoruesi, së bashku me **Vite** si mjet ndërtimi dhe zhvillimi.

### Arsyet e zgjedhjes së Vue.js:
- Strukturë e qartë dhe e thjeshtë e komponentëve.
- Reaktivitet i lartë dhe përditësim dinamik i ndërfaqes.
- Lehtësi në integrim me API-të backend.
- I përshtatshëm për projekte akademike dhe profesionale.

### Roli i frontend-it:
- Ofrimi i një ndërfaqeje intuitive për përdoruesin.
- Mundësimi i zgjedhjes së pikës së nisjes (origin) dhe destinacionit.
- Dërgimi i të dhënave të fluturimit drejt backend-it.
- Vizualizimi i trajektores së dronit në hartë.

Frontend-i përfaqëson pjesën vizuale të sistemit dhe ndërvepron drejtpërdrejt me përdoruesin.

---

## 4.3 Vizualizimi i Hartës – Leaflet

Për vizualizimin e trajektores së fluturimit është përdorur biblioteka **Leaflet**, e cila është një nga bibliotekat më të njohura për harta interaktive në aplikacione web.

### Funksionalitetet e Leaflet në projekt:
- Shfaqja e hartës gjeografike.
- Vendosja e marker-ave për pikën e nisjes dhe destinacionin.
- Vizatimi i vijës lidhëse (trajektores) ndërmjet dy pikave.
- Mundësia e zmadhimit dhe lëvizjes në hartë.

Leaflet lejon një paraqitje të qartë vizuale të lëvizjes së dronit dhe e bën sistemin më intuitiv për përdoruesin.

---

## 4.4 Komunikimi Frontend–Backend – Axios & HTTP

Komunikimi ndërmjet frontend-it dhe backend-it realizohet përmes kërkesave HTTP duke përdorur bibliotekën **Axios**.

### Roli i Axios:
- Dërgimi i kërkesave POST për krijimin e fluturimeve.
- Marrja e të dhënave për trajektoren e fluturimit (GET requests).
- Menaxhimi i përgjigjeve nga serveri.

Ky mekanizëm siguron një komunikim të qëndrueshëm dhe të strukturuar ndërmjet dy pjesëve kryesore të sistemit.

---

## 4.5 Mjedisi i Zhvillimit dhe Versionimi

Për zhvillimin dhe menaxhimin e projektit janë përdorur këto mjete shtesë:

- **Visual Studio Code** – editor për zhvillim.
- **Git & GitHub** – për versionim dhe bashkëpunim në ekip.
- **Virtual Environment (venv)** – për izolimin e varësive të Python-it.
- **npm** – për menaxhimin e varësive të frontend-it.

Përdorimi i këtyre mjeteve siguron një zhvillim të organizuar, të kontrolluar dhe të përshtatshëm për punë ekipore.

---

## 4.6 Përmbledhje

Teknologjitë e përdorura në këtë projekt janë zgjedhur me qëllim që të ofrojnë:
- funksionalitet të plotë,
- arkitekturë të qartë,
- dhe mundësi zgjerimi në të ardhmen.

Kombinimi i FastAPI, Vue.js dhe Leaflet krijon një bazë solide për zhvillimin e sistemeve moderne të menaxhimit të dronëve dhe simulimit të trajektores së fluturimit.
