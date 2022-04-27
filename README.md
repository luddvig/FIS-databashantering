# Kvaf-databashantering
Script för bearbetning av data och skapa ny databas

För att köra:
  1. Lägg filerna i en mapp där python kan köras. Refereras hädanefter till som "huvudmapp".
  2. Skapa 5 undermappar i huvudmappen: FISLIST, FISLIST_ranked, NewDatabase, WCSL, WCSL_ranked
  3. Lägg till "fispointlist" excelfiler i FISLIST.
  4. Lägg till "worldcup startlist" excelfiler i WCSL.
  5. Kör huvudprogram.py

Efter körning:
  - WCSL_ranked innehåller excelfiler för varje år och kön. Varje excelfil har 4 blad, ett för varje disciplin, med åkare som är rankade på worldcup.
  - FISLIST_ranked innehåller excelfiler av två typer: "exklude" eller vanlig. "exclude" är ranking exklusive de med ranking på worldcup. Vanlig har med alla åkare. En excelfil för varje år och kön, 4 blad för varje disciplin. 
  - NewDatabase innehåller excelfiler för varje år och kön med ny ranking utifrån WCSL_ranked och FISLIST_ranked. WCSL_ranked rankas högst, följt av FISLIST_ranked.

Format excelfiler för fispointlist och worldcup startlist excelfiler:
  - fispointlist: "FIS-points-list-AL-2012-{xxx}.xlsx"
    -  Exempel: FIS-points-list-AL-2012-184.xlsx
  - worldcup startlist: "FIS-Standings-{DD.MM.YYYY}-{xx}h{zz}AL-{year}-WCSL" 
    - Exempel: "FIS-Standing-04.05.2021-13h09AL-2021-WCSL"
