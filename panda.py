import pandas as pd

file = filedialog.askopenfilename(filetypes = (("Excel files","*.xlsx"),("all files","*.*")))
sheet = file.sheet_by_name('Sheet1')
data = pd.read_excel(file, sheet)