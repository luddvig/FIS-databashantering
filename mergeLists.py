import pandas
import os

""" 
*** INSTRUKTIONER ***
Kör först programmet wcsl_remakeFile.py samt fis_remakeFile.py, sedan:
Skapa en mapp "NewDatabase" med en undermapp "YearAndGender". 
Lägg mappen "NewDatabase" samt denna programfil i samma mapp.

Exempelmapp:
    -mergeLists.py          [pythonfil]
    -NewDatabase            [mapp]
        -YearAndGender      [mapp]
"""

cwd = os.getcwd()       # nuvarande directory

# Initierar vägar för fis-filer
fis_dir = "FISLIST"
fis_ranked_dir = "FISLIST_ranked"
fis_path = os.path.join(cwd, fis_dir)
fis_ranked_path = os.path.join(cwd, fis_ranked_dir)

# Initierar vägar för wcsl-filer
wcsl_dir = "WCSL"
wcsl_ranked_dir = "WCSL_ranked"
wcsl_path = os.path.join(cwd, wcsl_dir)
wcsl_ranked_path = os.path.join(cwd, wcsl_ranked_dir)

# Initierar vägar för ny databas
db_dir = "NewDatabase/YearAndGender"
db_path = os.path.join(cwd, db_dir)


def merge_to_db(wcsl_path, fis_path, db_path, wcsl_file, fis_file):
    """Sammanfogar wcsl och fispoint till en slutgiltig databas och lägger till ranking. wcsl högst, fis därefter."""
    disciplins = ["DHpos", "SLpos", "GSpos", "SGpos"]
    inWCLSPath = wcsl_path+"/"+wcsl_file
    inFisPath = fis_path+"/"+fis_file
    excel_file = db_path+"/"+wcsl_file[:7]+"db.xlsx"
    listYear = excel_file.split("/")[-1].split(".")[0]
    writer = pandas.ExcelWriter(path=excel_file, engine="xlsxwriter")
    for dis in disciplins:
        dataframe_wcsl = pandas.ExcelFile(inWCLSPath).parse(sheet_name=dis)
        dataframe_fis = pandas.ExcelFile(inFisPath).parse(sheet_name=dis)
        dataframe_db = pandas.concat([dataframe_wcsl, dataframe_fis])
        dataframe_db["list_year"] = listYear
        dataframe_db["pos"] = range(1, len(dataframe_db)+1)
        dataframe_db["pos_reversed"] = list(reversed(range(1, len(dataframe_db)+1)))
        dataframe_db["age"] = dataframe_db["list_year"].astype(int) - dataframe_db["Birthyear"].astype(int)
        del dataframe_db[dis]
        dataframe_db.to_excel(excel_writer=writer, sheet_name=dis, index=False)
    writer.save()


def run_merge_to_db():
    """Hjälpfunktion som kör merge_to_db() för varje år. Tar cirka 40 sec att köra"""
    for fis_file in os.listdir(fis_ranked_path):
        if not fis_file.startswith(".") and "exclude" in fis_file:
            wcsl_file = fis_file[:7]+"WorldCup.Ranked.xlsx"
            merge_to_db(wcsl_ranked_path, fis_ranked_path, db_path, wcsl_file, fis_file)
    print("run_merge_to_db() klar")
