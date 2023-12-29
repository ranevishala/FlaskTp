# app.py

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

# Sample data (replace with your own data)
data = [
    {"Name": "John", "Age": 25},
    {"Name": "Alice", "Age": 30},
    {"Name": "Bob", "Age": 22},
    # Add more rows as needed
]

# Specify the projects you want to include in the dropdown
included_projects = ['Project A', 'Project B']

search_options = ['Find Error', 'Find by RunID']  # Dropdown options for search types

@app.route('/')
def index():
    return render_template('index.html', projects=included_projects, search_options=search_options)

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    selected_project = request.form.get('project')
    selected_search_option = request.form.get('search_option')

    # Call the appropriate function based on the selected search option
    if selected_search_option == 'Find Error':
        result = find_error_solution()
    elif selected_search_option == 'Find by RunID':
        result = find_by_run_id()
    else:
        result = []

    return render_template('index.html', projects=included_projects, search_options=search_options, data=result, query=query, selected_search_option=selected_search_option)

def find_error_solution():
    # Implement logic to find the error solution
    return [{"Name": "Error Solution", "Age": "-"}]

def find_by_run_id():
    # Implement logic to find errors by RunID and return a table
    return [
        {"Name": "Error 1", "Age": "-"},
        {"Name": "Error 2", "Age": "-"},
        {"Name": "Error 3", "Age": "-"},
        # Add more rows as needed
    ]

if __name__ == '__main__':
    app.run(debug=True)
