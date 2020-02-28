External Libraries: <br/>
 < Python 3.8 >  <br/>
<br/>
Uputstvo: <br/>
(1)Unesite korenski direktorijum(apsolutna putanja) <br/>
(2)Opcije: <br/>
 1 - Unesite,ponovo,korenski direktorijum. <br/>
 2 - Unesite upit. <br/>
 3 - Izlazak iz programa. <br/>
<br/>
#trie - pored odgovarajućih klasa kojima se predstavlja trie stablo, implementira funkcije za dodavanje reči u stablo i pretragu reči u stablu.<br/><br/>
#osnovne_skupovne_operacije - primenjuju osnovne skupovne operacije preseka, unije i komplementa(umesto ugradjenih pozivaju se one iz seta) i utvrđuju se rezultati skupa stranica.<br/><br/>
#pretraga_dokumenata - određivanje skupova HTML stranica koje sadrže pojedinačne reči upita.<br/><br/>
#unos_upita - parsiranje upita, određivanje reči i utvrđivanje postojanja nekog od logičkih operatora AND, OR i NOT.Upit sadrzi 3 reci, 2reci, 1 rec, ili 2 reci i 1 logicki operator(koji se nalazi izmedju reci).Za pogresne unose upita izlazi obavestenje o tome, i zatim se opet trazi novi unos,sve do tacnog unosa. <br/><br/>
#parsiranje_skupa_HTML_dokumenata - izgradnja trie stabla u koje su smestene sve reci iz svih HTML dokumenata.Za pogresne unose korenskog direktorijuma izlazi obavestenje o tome, i zatim se opet trazi novi unos,sve do tacnog unosa.<br/>
algoritam rangiranja:
    
    konacan_set.stranice-lista putanja onih stranica koje su rezultat pretrage
    #rangiranje po broju pojavljivanja reci
    -prolazak kroz putanje u konacan set
        -prolazak kroz putanje u konacnom recniku(to je mapa gde su kljucevi putanje, a vrednosti su brojevi pojavljivanja)
            -da li je putanja iz konacnog seta jednaka putanji iz konacnog recnika?
                ako jeste na vrednosti koje vec postoje dodajemo broj pojavljivanja iz konacnog recnika za tu putanju
                ako nije vec ubacena u rangovi_putanje od te putanje, ubacujemo iz konacnog recnika broj pojavljivanja za tu putanju
     -prodjemo kroz mapu rangova i putanja i mnozimo rangove sa 0.3
     
     #rangiranje na osnovu broja linkova na tu stranicu       
     rang1-od putanja broj onih koji ih linkuju
     -prolazimo kroz rangovi_putanje mapu 
        -prolazimo kroz sve vertekse
            -da li je putanja tog verteksa jednaka putanji do koje smo dosli
                -ako ta putanja vec postoji dodajemo na postojecu vrednost broj koji ga linkuju,
                -a ako ne upisujemo broj onih koji ga linkuju u rang1
      -prolazimo kroz rang1.keys() (broj onih koji ga linkuju)
        dodajemo u pocetnu mapu broj onih koji ga linkuju pomnozen sa 0.2
        
      # rangiranje na osnovu stranica koje imaju link na taj html i sadrze trazenu rec
      -prolazimo kroz putanje
        -prolazimo kroz vertekse
            -da li je putanja verteksa jednaka toj putanji
                   -ako nije vec dodata u rang2.keys stavljamo ga na nulu i
                   -koristimo kroz metodu u grafu koja vraca listu svih putanja od onih koji ga linkuju i prolazimo kroz te putanje i
                        -pitamo da li je ta putanja medju onim koje sadrze datu rec       
                            -ako jeste onda povecavamo brojac za jedan
      -prolazimo kroz rang2 i u pocetnu mapu dodajemo staru + novu*0.5
      
      vracamo rangovi_putanje(key-putanje,vrednost-rang), tu se nalazi broj pojavljivanja reci * 0.3, broj onih koje ga linkuju *0.2,
      broj onih koje ga linkiju i sadrze trazenu rec *0.5   

algoritam sortiranja:<br/>
Merge sort- ukupno vreme izvrsavanja je O(nlogn), brz je
    
    -pravimo listu od rangova i prolazimo po rangovima, prebacimo u set da bi bilo jedinstveno, ubacimo listu u merge_sort
     -prolazimo redom po rangovima, one putanje koje imaju taj rang se stampaju.
           
        
        
<br/>
Student 1: <br/>
 Ana Atanackovic RA 43/2017 <br/>
<br/><br/>
Student 2: <br/>
 Emina Turkovic RA 49/2017 <br/>
<br/><br/>
