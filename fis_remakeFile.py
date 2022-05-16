import pandas
import os

""" 
*** INSTRUKTIONER ***
Kör först programmet wcsl_remakeFile.py, sedan:
Skapa en mapp "FISLIST" med samtliga FIS-Excelfiler som ska bearbetas. 
Skapa en tom mapp "FISLIST_ranked".
Lägg in de båda mapparna samt denna programfil i samma mapp.

Exempelmapp:
    -fis_remakeFile.py              [pythonfil]
    -FISLIST                        [mapp]
        -Excelfiler att bearbeta    [Excelfiler]
    -FISLIST_ranked                 [mapp]
"""

cwd = os.getcwd()
fis_dir = "FISLIST"
fis_ranked_dir = "FISLIST_ranked"
fis_path = os.path.join(cwd, fis_dir)
fis_ranked_path = os.path.join(cwd, fis_ranked_dir)

wcsl_dir = "WCSL"
wcsl_ranked_dir = "WCSL_ranked"
wcsl_path = os.path.join(cwd, wcsl_dir)
wcsl_ranked_path = os.path.join(cwd, wcsl_ranked_dir)


def fis_remake(dirPath, fileName, outPath, gender, *args):
    """Skapar excelfil med ett blad för varje disciplin från ursprunglig fispoints excelfil."""
    inFilePath = dirPath+"/"+fileName
    disciplins = ["DHpos", "SLpos", "GSpos", "SGpos"]
    dataFrame1 = pandas.ExcelFile(inFilePath).parse()
    gen = gender
    excel_file = outPath + "/" + fileName[19:23] + "." + gen + ".FIS.Ranked.xlsx"
    writer = pandas.ExcelWriter(excel_file, engine="xlsxwriter")
    for dis in disciplins:
        dataFrame2 = dataFrame1[dataFrame1["Gender"].isin([gen])]
        dataFrame2 = dataFrame2[list(args)+[dis]].dropna(subset=dis)
        dataFrame2.to_excel(excel_writer=writer, sheet_name=dis, index=False)
    writer.save()


def run_remake_fis():
    """Hjälpfunktion som kör fis_remake() för varje lista i FISLIST-mappen. Tar cirka 2 min att köra"""
    for file in os.listdir(fis_path):
        if not file.startswith("."):
            for gen in ["M", "W"]:
                fis_remake(fis_path, file, fis_ranked_path, gen,
                           "Fiscode", "Competitorname", "Gender", "Nationcode", "Birthyear")
    print("run_remake_fis() klar")


def fis_exclude_wcsl(fis_path, wcsl_path, filename):
    """Exkluderar åkare med ranking i wcsl från fis_remake. Ordnad efter ranking."""
    inFisPath = fis_path+"/"+filename
    inWCSLPath = wcsl_path+"/"+filename[:7]+"WorldCup.Ranked.xlsx"
    disciplins = ["DHpos", "SLpos", "GSpos", "SGpos"]
    excel_file = inFisPath[:-4]+"exclude.xlsx"
    writer = pandas.ExcelWriter(path=excel_file, engine="xlsxwriter")
    for dis in disciplins:
        dataframe1 = pandas.ExcelFile(inFisPath).parse(sheet_name=dis)
        dataframe2 = pandas.ExcelFile(inWCSLPath).parse(sheet_name=dis)
        used = dataframe2["Fiscode"].tolist()
        dataframe3 = dataframe1[~dataframe1["Fiscode"].isin(used)].sort_values(dis)
        dataframe3.to_excel(excel_writer=writer, sheet_name=dis, index=False)
    writer.save()


def run_fis_exclude_wcsl():
    """Hjälpfunktion för att köra fis_exclude_wcsl(). Ger Tar cirka 30 sec att köra"""
    for file in os.listdir(fis_ranked_path):
        if not file.startswith(".") and "exclude" not in file:
            fis_exclude_wcsl(fis_ranked_path, wcsl_ranked_path, file)
    print("run_fis_exclude_wcsl() klar")