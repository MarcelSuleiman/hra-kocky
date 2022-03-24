# hra-kocky
---
Hra 3 kocky.

Hra pre 2 - oo hráčov.

Ako prvé sa hráči dohodnú, o akú sumu budú hrať.
V prvom "nultom" kole každý hráč hodí jednou kockou a podľa výsledku sa určí, v akom poradí hráči hrajú. Najvyššie číslo začína.
Následne v poradí hádžu troma kockami naraz. Po každom hode 3 kockami sa hráč rozhodne, či chce pokračovať alebo prenechá kolo ďalšiemu hráčovi.
Ak sa rozhodne hrať, z hodených kociek si vyberie tú, pri ktorej má najvyššiu šancu druhým hodom sa trafiť medzi rozpätie zvyšných dvoch už hodených kociek.

Príklad, hod troma kockami 2, 4, 6 -> hráč si vyberie kocku č.: 2 (s hodnotou 4) a ak sa mu ňou podarí hodiť číslo 3, 4 alebo 5, vyhráva. Ak by hodil 1, 2 alebo 6 - prehráva.
			
V prípade že sa mu to podarí, vyhráva obsah banku a hra začína odznova.
V prípade neúspechu vypadáva z hry a na rade je ďalší hráč.
V prípade prehry sa hráč môže vykúpiť a to tým, že doloží výšku celého vkladu a tým pádom ostáva v hre.
príklad: 3 hráči, každý vložil po 10 tj. bank = 30.
Hráč 1 prehral ale ak má záujem, doložením 30 sa vykúpi a môže pokračovať v hre.
