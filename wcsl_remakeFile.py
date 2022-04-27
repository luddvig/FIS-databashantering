import pandas
import os

cwd = os.getcwd()
wcsl_dir = "WCSL"
wcsl_ranked_dir = "WCSL_ranked"
wcsl_path = os.path.join(cwd, wcsl_dir)
wcsl_ranked_path = os.path.join(cwd, wcsl_ranked_dir)


def wcsl_remake(dirPath, fileName, outPath, *args):
    """Skapar excelfil med åkare som har ranking i wcsl excelfil. Ordnad efter ranking."""
    inFilePath = dirPath+"/"+fileName
    disciplins = ["DHpos", "SLpos", "GSpos", "SGpos"]
    dataFrame1 = pandas.ExcelFile(inFilePath).parse()
    if "M" in dataFrame1["Gender"].values:
        gen = "M"
    else:
        gen = "W"
    excel_file = outPath + "/" + fileName[32:36] + "." + gen + ".WorldCup.Ranked.xlsx"
    writer = pandas.ExcelWriter(excel_file, engine="xlsxwriter")
    for dis in disciplins:
        dataFrame2 = dataFrame1[list(args)+[dis]].dropna(subset=dis).sort_values(dis)
        dataFrame2.to_excel(excel_writer=writer, sheet_name=dis, index=False)
    writer.save()


def run_wcsl_remake():
    for file in os.listdir(wcsl_path):
        wcsl_remake(wcsl_path, file, wcsl_ranked_path, "Fiscode", "Competitorname", "Gender", "Birthyear")
    print("run_wcsl_remake() klar")