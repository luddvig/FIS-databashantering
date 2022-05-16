import pandas
import os

""" 
*** INSTRUKTIONER ***
Skapa en mapp "WCSL" med samtliga WCSL-Excelfiler som ska bearbetas. 
Skapa en tom mapp "WCSL_ranked".
Lägg in de båda mapparna samt denna programfil i samma mapp.

Exempelmapp:
    -wcsl_remakeFile.py             [pythonfil]
    -WCSL                           [mapp]
        -Excelfiler att bearbeta    [Excelfiler]
    -WCSL                           [mapp]
"""

cwd = os.getcwd()
wcsl_dir = "WCSL"
wcsl_ranked_dir = "WCSL_ranked"
wcsl_path = os.path.join(cwd, wcsl_dir)
wcsl_ranked_path = os.path.join(cwd, wcsl_ranked_dir)


def wcsl_remake(dirPath, fileName, outPath, *args):
    """Skapar excelfil med åkare som har ranking i wcsl excelfil. Ordnad efter ranking.
    Data för varje åkare: Fiscode, Competitorname, Gender, Birthyear, Nationcode, pos"""
    inFilePath = dirPath+"/"+fileName
    disciplins = ["DHpos", "SLpos", "GSpos", "SGpos"]
    dataFrame1 = pandas.ExcelFile(inFilePath).parse()       # Läser in Excelfil
    if "M" in dataFrame1["Gender"].values:
        gen = "M"                                           # Kollar om herrar
    else:
        gen = "W"                                           # Kollar om damer
    excel_file = outPath + "/" + fileName[32:36] + "." + gen + ".WorldCup.Ranked.xlsx"
    writer = pandas.ExcelWriter(excel_file, engine="xlsxwriter")
    for dis in disciplins:                                                              # Körs för samtliga discipliner
        dataFrame2 = dataFrame1[list(args)+[dis]].dropna(subset=dis).sort_values(dis)   # Bearbetning
        dataFrame2.to_excel(excel_writer=writer, sheet_name=dis, index=False)           # Skriver till ny Excelfil
    writer.save()


def run_wcsl_remake():
    """Hjälpfunktion för att köra wcsl_remake() för samtliga listor i wcsl-mappen, dvs för varje år."""
    for file in os.listdir(wcsl_path):
        wcsl_remake(wcsl_path, file, wcsl_ranked_path,
                    "Fiscode", "Competitorname", "Gender", "Nationcode", "Birthyear")
    print("run_wcsl_remake() klar")