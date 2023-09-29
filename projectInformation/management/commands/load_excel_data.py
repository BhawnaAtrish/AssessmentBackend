from projectInformation.models import projectData
import openpyxl

"""
Function to load the project data present in the excel into the DB.
"""


def load_excel_data_into_db():
    excel_file = "Project_data.xlsx"
    wb = openpyxl.load_workbook(excel_file)

    worksheet = wb["Sheet1"]
    print(worksheet)

    excel_data = list()
    for row in worksheet.iter_rows():
        row_data = list()
        for cell in row:
            row_data.append(str(cell.value))
        excel_data.append(row_data)

    for i in range(1, len(excel_data)):
        projectData.objects.create(
            project_title=excel_data[i][0],
            project_technologies=excel_data[i][1],
            technical_skillset_frontend=excel_data[i][2],
            technical_skillset_backend=excel_data[i][3],
            technical_skillset_databases=excel_data[i][4],
            technical_skillset_infrastructre=excel_data[i][5],
            other_information_availability=excel_data[i][6],
        )
