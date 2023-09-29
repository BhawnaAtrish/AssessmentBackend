from django.shortcuts import render
from .models import projectData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializer import ProjectSerializer

def remove_spacing(project_property):
    project_property=[str(x).strip() for x in project_property]
    return project_property



def get_project_list(request):
    # Sample input data
    project_data_objects = projectData.objects.all()

    # Create a list to store unique project technologies
    unique_technologies = list()
    unique_frontend = list()
    unique_backend = list()
    unique_databases = list()
    unique_infrastructures = list()

    # Parse the input data and extract project technologies
    for project_info in project_data_objects:
        project_technologies = remove_spacing(project_info.project_technologies.split(','))
        frontend_technologies = remove_spacing(project_info.technical_skillset_frontend.split(','))
        backend_technologies = remove_spacing(project_info.technical_skillset_backend.split(','))
        database_technologies = remove_spacing(project_info.technical_skillset_databases.split(','))
        infrastructure_technologies = remove_spacing(project_info.technical_skillset_infrastructre.split(','))

        unique_technologies.extend(project_technologies)
        unique_frontend.extend(frontend_technologies)
        unique_backend.extend(backend_technologies)
        unique_databases.extend(database_technologies)
        unique_infrastructures.extend(infrastructure_technologies)

    # Convert the set to a list and sort it if needed
    unique_technologies_list = sorted(list(set(unique_technologies)))
    frontend_technologies_list = sorted(list(set(unique_frontend)))
    backend_technologies_list = sorted(list(set(unique_backend)))
    database_technologies_list = sorted(list(set(unique_databases)))
    infrastructure_technologies_list = sorted(list(set(unique_infrastructures)))

    # Send the unique project technologies to the frontend as JSON response
    data = {
        "unique_technologies": unique_technologies_list,
        "frontend_technologies": frontend_technologies_list,
        "backend_technologies": backend_technologies_list,
        "database_technologies": database_technologies_list,
        "infrastructure_technologies": infrastructure_technologies_list
        }
    print(data)
    return JsonResponse(data = data)

@csrf_exempt
def filter_projects(request):
    project_data_objects = projectData.objects.all()
    data = project_data_objects
    if request.method=="POST":
        project_technologies = request.POST.get("project_technologies")
        frontend_technologies = request.POST.get("frontend_technologies")
        backend_technologies = request.POST.get("backend_technologies")
        database_technologies = request.POST.get("database_technologies")
        infrastructure_technologies = request.POST.get("infrastructure_technologies")

        data = filter_project_technologies(project_data_objects,project_technologies)
        data = filter_frontend_technologies(data,frontend_technologies)
        data = filter_backend_technologies(data,backend_technologies)
        data = filter_database_technologies(data,database_technologies)
        data = filter_infrastructure_technologies(data, infrastructure_technologies)
            
    serialized_data = ProjectSerializer(data, many=True)
    return JsonResponse({'data': serialized_data.data})
    
    return JsonResponse({'data' : data})

def filter_project_technologies(project_data, project_technologies):
    data = []
    for project_info in project_data:
            project_technologies_list = remove_spacing(project_info.project_technologies.split(','))
            print(project_technologies_list)
            if(not project_technologies or project_technologies in project_technologies_list):
                data.append(project_info)
    return data

def filter_frontend_technologies(project_data, frontend_technologies):
    data = []
    for project_info in project_data:
            frontend_technologies_list = remove_spacing(project_info.technical_skillset_frontend.split(','))
            if(not frontend_technologies or frontend_technologies in frontend_technologies_list):
                data.append(project_info) 
    return data

def filter_backend_technologies(project_data, backend_technologies):
    data = []
    for project_info in project_data:
            backend_technologies_list = remove_spacing(project_info.technical_skillset_backend.split(','))
            if(not backend_technologies or backend_technologies in backend_technologies_list):
                data.append(project_info)  
    return data

def filter_database_technologies(project_data, database_technologies):
    data = []
    for project_info in project_data:
            database_technologies_list = remove_spacing(project_info.technical_skillset_databases.split(','))
            if(not database_technologies or database_technologies in database_technologies_list):
                data.append(project_info) 
    return data

def filter_infrastructure_technologies(project_data, infrastructure_technologies):
    data = []
    for project_info in project_data:
            infrastructure_technologies_list = remove_spacing(project_info.technical_skillset_infrastructre.split(','))
            if(not infrastructure_technologies or infrastructure_technologies in infrastructure_technologies_list):
                data.append(project_info)  
    return data