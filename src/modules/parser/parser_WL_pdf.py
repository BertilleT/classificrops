'''# Import the required Module
import tabula
# Read a PDF File
df = tabula.read_pdf("../../../data/WL/2020_WL.pdf", pages='all')[0]
# convert PDF into CSV
tabula.convert_into("../../../data/WL/2020_WL.pdf", "../../../data/WL/2020_WL.csv", output_format="csv", pages='all')
print(df)'''


import pdftables_api

c = pdftables_api.Client('motl4iq1ay5b')
c.csv('../../../data/WL/2020_WL.pdf', '../../../data/WL/2020_WL.csv')