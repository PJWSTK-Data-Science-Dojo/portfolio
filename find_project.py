import json
from Project import Project

projects_json_file = open('pages/projects.json', encoding='utf-8')
projects_json = json.load(projects_json_file)

projects = []
for project_json in projects_json:
    project = Project(json_data=project_json)
    projects.append(project)

def find_project(project_name: str):
    predicate = lambda proj: isinstance(proj, Project) and proj.project_name == project_name
    return next((proj for proj in projects if predicate(proj)), None)
