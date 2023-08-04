# Django Todo Application
### This is a simple Django Todo Application that allows users to manage their tasks. Users can add, view, edit, mark as complete, and delete tasks using the web interface.  

## Features

- Add a new task with a title and description.
- View a list of tasks with their titles and descriptions.
- Edit existing tasks' titles and descriptions.
- Mark tasks as complete or reopen them.
- Delete tasks from the list.

## Installation

- Clone repository

https://github.com/Bermet777/Neobis_ToDo_Project_new

- Create a virtual environment and activate it:

```python -m venv venv```

```source venv/bin/activate   # On Windows: venv\Scripts\activate```

- Set up the database:

```python manage.py migrate```

- Run the development server

```python manage.py runserver```

The application will be accessible at http://127.0.0.1:8000/.

## Usage

- To add a new task, enter the title and description in the "New task" form and click the "Add" button.
- To edit a task, click the "Edit" button for the task you want to modify. You will be taken to the "Edit Task" page where you can update the title and description. Click "Save" to save the changes.
- To mark a task as complete or reopen it, click the "Close" or "Open" button.
- To delete a task, click the "Delete" button.





