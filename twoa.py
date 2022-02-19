import xlrd
import os

def excel_file_filter(filename, extensions=['.xls', '.xlsx']):
    return any(filename.endswith(e) for e in extensions)

def get_filenames(root):
    filename_list = []
    for path, subdirs, files in os.walk(root):
        for filename in filter(excel_file_filter, files):
            filename_list.append(os.path.join(path, filename))
    return filename_list

spreadsheets = get_filenames('D:\\')
for s in spreadsheets:
# define empty_cell boolean
    empty_cell= False
    with xlrd.open_workbook(s) as wb:
        cs= wb.sheet_by_index(0)
        num_cols= cs.ncols
        num_rows= cs.nrows
        for row_index in range(1, num_rows):
            # set count empty cells
            count_empty = 0
            #print('Row: {}'.format(row_index))
        for col_index in range(0,num_cols):
            # get cell value
            cell_type= cs.cell_type(row_index, col_index)
            # check if cell is empty
            if cell_type == xlrd.XL_CELL_EMPTY:
                # set empty cell is True
                empty_cell = True
                # increment counter
                break
            else:
                # set empty cell is false
                empty_cell= False

            # check if cell is not empty
            if not empty_cell:
                # print value of cell
                print('Col #: {} | Value: {}'.format(col_index))

        # check the counter if is = num_cols means the whole row is empty       
        if count_empty == num_cols:
            print ('Row is empty')
            # stop looping to next rows
            break     