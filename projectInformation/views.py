from .models import projectData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import ProjectSerializer


def remove_spacing(project_property):
    project_property = [str(x).strip() for x in project_property]
    return project_property


"""
API to send the unique project properties.
Example:
    data = {
            "unique_technologies": ['a', 'b'],
            "frontend_technologies": ['a', 'b'],
            "backend_technologies": ['a', 'b'],
            "database_technologies": ['a', 'b'],
            "infrastructure_technologies": ['a', 'b'],
        }
    So that, filter can be applied on the basis of these data from the frontend
"""


def get_project_list(request):
    project_data_objects = projectData.objects.all()

    unique_technologies = list()
    unique_frontend = list()
    unique_backend = list()
    unique_databases = list()
    unique_infrastructures = list()

    for project_info in project_data_objects:
        project_technologies = remove_spacing(
            project_info.project_technologies.split(",")
        )
        frontend_technologies = remove_spacing(
            project_info.technical_skillset_frontend.split(",")
        )
        backend_technologies = remove_spacing(
            project_info.technical_skillset_backend.split(",")
        )
        database_technologies = remove_spacing(
            project_info.technical_skillset_databases.split(",")
        )
        infrastructure_technologies = remove_spacing(
            project_info.technical_skillset_infrastructre.split(",")
        )

        unique_technologies.extend(project_technologies)
        unique_frontend.extend(frontend_technologies)
        unique_backend.extend(backend_technologies)
        unique_databases.extend(database_technologies)
        unique_infrastructures.extend(infrastructure_technologies)

    unique_technologies_list = sorted(list(set(unique_technologies)))
    frontend_technologies_list = sorted(list(set(unique_frontend)))
    backend_technologies_list = sorted(list(set(unique_backend)))
    database_technologies_list = sorted(list(set(unique_databases)))
    infrastructure_technologies_list = sorted(list(set(unique_infrastructures)))

    data = {
        "unique_technologies": unique_technologies_list,
        "frontend_technologies": frontend_technologies_list,
        "backend_technologies": backend_technologies_list,
        "database_technologies": database_technologies_list,
        "infrastructure_technologies": infrastructure_technologies_list,
    }
    return JsonResponse(data=data)


"""
API to filter the projects based on the certain paramters like: backend and fronend Technologies
"""


@csrf_exempt
def filter_projects(request):
    data = projectData.objects.all()
    if request.method == "POST":
        project_technology = request.POST.get("project_technologies")
        frontend_technology = request.POST.get("frontend_technologies")
        backend_technology = request.POST.get("backend_technologies")
        database_technology = request.POST.get("database_technologies")
        infrastructure_technology = request.POST.get("infrastructure_technologies")

        for technologyData in [
            ["project_technologies", project_technology],
            ["technical_skillset_frontend", frontend_technology],
            ["technical_skillset_backend", backend_technology],
            ["technical_skillset_databases", database_technology],
            ["technical_skillset_infrastructre", infrastructure_technology],
        ]:
            data = filter_technologies(data, technologyData)

    serialized_data = ProjectSerializer(data, many=True)
    return JsonResponse({"data": serialized_data.data})


def filter_technologies(project_data, technologyData):
    fieldName, technology = technologyData[0], technologyData[1]
    data = []
    for project_info in project_data:
        technology_list = remove_spacing(getattr(project_info, fieldName).split(","))
        if not technology or technology in technology_list:
            data.append(project_info)
    return data
