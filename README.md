# online_sales_analysis
Proiect din studiul Python, modul Git-GitHub,  pentru controlul versiunilor și colaborarea în echipă.

# Pt un sistem care să accepte:
- lucrul cu produse (adăugarea, afișarea, actualizarea și eliminarea);
- gestionarea coșului clientului (adăugarea produselor, afișarea conținutului și calcularea valorii totale);
- documentarea proiectului prin fișierul README.md și securitatea datelor prin .gitignore.

# Phase1 - set-up - mediul de lucru

# Phase 2 
- definirea clasei Product:
 - Conține atributele: name, price și quantity.
 - Metoda pentru afișarea informațiilor despre produs.
 - Metoda pentru actualizarea cantității de produse.

- definirea clasei Product Manager:
 - Conține ca atribut o listă cu toate produsele disponibile.
 - Adăugarea de produse.
 - Afișarea tuturor produselor.
 - Afișarea valorii totale a tuturor produselor.

- main.py:
 - adaugare produse arbitrare si afișați produsele și valoarea totală a inventarului

# Phase 3 - first commit of Phase2.

# Phase 4:
 - Creați o ramură nouă add-product-removal, in care:
     - Adăugați metoda în ProductManager pentru a elimina produsele după nume.
     -Faceți commit cu un mesaj semnificativ.


# Phase 6:
- ramură nouă cu add-cart-functionality,  in care:
 - definirea clasei Cart:
     - Atribut: cart_items – lista de produse din coș.
     - Metode:
         - Adăugarea produselor în coș.
         - Calcularea valorii totale a coșului, adică a sumei de plată.
         - Afișarea conţinutul coşului.
 - modificări în fișierul main.py:
     - o instanță a clasei Cart.
     - Adăugați în coș 3 produse selectate aleatoriu din lista de produse disponibile a instanței ProductManager.
     - Afișați valoarea totală de plată a conținutului coșului, precum și produsele care se află în acesta.

- Faceți un commit cu un mesaj semnificativ.