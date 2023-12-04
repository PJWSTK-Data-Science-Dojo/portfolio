class Project:
    def __init__(self, json_data):
        self.project_name = json_data.get("project_name", "")
        self.project_link = json_data.get("project_link", "")
        self.project_description = json_data.get("project_description", "")
        self.project_goal = json_data.get("project_goal", "")
        self.start_time = json_data.get("start_time", "")
        self.spent_time = json_data.get("spent_time", "")
        self.project_members = json_data.get("project_members", [])
        self.utilized_technical_resources = json_data.get("utilized_technical_resources", [])
        self.tests_and_their_results = json_data.get("tests_and_their_results", [])

    def __str__(self):
        return f"Project Name: {self.project_name}\n" \
               f"Project Link: {self.project_link}\n" \
               f"Project Description: {self.project_description}\n" \
               f"Project Goal: {self.project_goal}\n" \
               f"Start Time: {self.start_time}\n" \
               f"Spent Time: {self.spent_time}\n" \
               f"Project Members: {', '.join(map(str, self.project_members))}\n" \
               f"Utilized Technical Resources: {', '.join(map(str, self.utilized_technical_resources))}\n" \
               f"Tests and Their Results: {self.tests_and_their_results}"

""" Sample JSON data
json_data = '''
[
    {
        "project_name": "Streamlit",
        "project_link": "",
        "project_description": "**Streamlit** jest projektem o opowiadaniu o reszcie projektów **Koła**!",
        "project_goal": "",
        "start_time": "",
        "spent_time": "",
        "project_members": ["mention if there are specialists of that field in the team", ""],
        "utilized_technical_resources": [""],
        "tests_and_their_results": [
            {
                "name": "",
                "description_md": "if tests are automated, mention that here",
                "result": ""
            }
        ]
    }
]
'''
"""