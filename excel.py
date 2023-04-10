import xlsxwriter

def makeExcel(tab:dict, columns:int) -> None:
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook('./result/proba.xlsx')
    worksheet = workbook.add_worksheet()

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 15)

    # Text with formatting.
    worksheet.write('A1', 'Somme \ Etape', bold)

    # Write some numbers, with row/column notation.
    for c in range(columns + 1):
        worksheet.write(f"{chr(ord('A') + c + 1)}1", c, bold)

    for row in tab:
        worksheet.write(f"A{row + 2}", str(row) + 'E', bold)

        for column, value in tab[row].items():
            worksheet.write(row + 1, column + 1, value)

    # Close and Save Excel file
    workbook.close()