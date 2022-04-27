from wcsl_remakeFile import *
from fis_remakeFile import *
from mergeLists import *
import time


# Uppdaterar alla filer och skapar databasen
# Tar cirka 3-3,5 minuter att köra
start = time.time()
run_wcsl_remake()
run_remake_fis()
run_fis_exclude_wcsl()
run_merge_to_db()
slut = time.time()
print("Tid: " + str(slut-start) + " sekunder")