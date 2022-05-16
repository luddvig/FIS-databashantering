import pandas
import os

""" 
*** INSTRUKTIONER ***
Kör först programmet mergeLists.py, sedan:
Skapa en undermapp "DisciplineAndGender" i mappen "NewDatabase".
Lägg denna programfil i samma mapp som "DisciplineAndGender".

Exempelmapp:
    -mergeDisciplines.py        [pythonfil]
    -NewDatabase                [mapp]
        -YearAndGender          [mapp]
        -DisciplineAndGender    [mapp]
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

# Initierar vägar för YearAndGender filer
yeadAndGender_dir = "NewDatabase/YearAndGender"
yeadAndGender_path = os.path.join(cwd, yeadAndGender_dir)

# Initierar vägar för ny databas
discipline_dir = "NewDatabase/DisciplineAndGender"
discipline_path = os.path.join(cwd, discipline_dir)

def merge_to_discipline(yearAndGender_path, discipline_path, gender, discipline):
    """Sammanfogar årsvisa rankinglistor till disciplin-visa data för respektive kön."""
    excel_file = discipline_path + "/" + discipline + "." + gender + ".db.xlsx"
    writer = pandas.ExcelWriter(path=excel_file, engine="xlsxwriter")
    dataframe_merged = pandas.DataFrame()
    for file in os.listdir(yearAndGender_path):
        if file.split(".")[1] == gender and not file.startswith("~"):
            file_path = yearAndGender_path+"/"+file
            dataframe = pandas.ExcelFile(file_path).parse(sheet_name=discipline)
            dataframe_merged = pandas.concat([dataframe_merged, dataframe])
    dataframe_merged.to_excel(excel_writer=writer, sheet_name=discipline, index=False)
    writer.save()


def run_merge_to_discipline():
    """Hjälpfunktion som kör merge_to_discipline() för samtliga årsvisa listor"""
    disciplines = ["DHpos", "SLpos", "GSpos", "SGpos"]
    for gender in ["M", "W"]:
        for dis in disciplines:
            merge_to_discipline(yeadAndGender_path, discipline_path, gender, dis)
            print(gender+dis)

