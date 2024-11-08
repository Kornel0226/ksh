import asyncio
from fetch import download_file
import statistics
import record
from record import load_records
from statistics import testx

asyncio.run(download_file("https://www.ksh.hu/stadat_files/nep/hu/nep0002.xlsx", "./data/table.xlsx"))
_, xd=load_records("./data/table.xlsx", 1)
testx(xd)


#asyncio.run(download_file("https://file-examples.com/storage/fe00d37cde6728af4966ebc/2017/04/file_example_MP4_1920_18MG.mp4", "./data/test.mp4"))