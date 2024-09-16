import json
import uuid
from datetime import datetime
import os
import argparse
import sys

# Functions to read and write to the JSON file
def load_tasks():
    json_file='tasks_list.json'

    # Si el archivo no existe, crearlo y retornar una lista vacía
    if not os.path.exists(json_file):
        with open(json_file, 'w') as file:
            json.dump([], file)
        return []

    # Si existe, cargar y devolver las tareas
    with open(json_file, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    json_file='tasks_list.json'

    with open(json_file, 'w') as file:
        json.dump(tasks, file, indent=4)



# Functions to manage tasks
def add_task(description):
    try:
        print(f"Creating the task...")
        task = {
            'id': str(uuid.uuid4().hex[:8]),
            'description': description,
            'status': 'todo',
            'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        tasks_list = load_tasks()
        tasks_list.append(task)
        save_tasks(tasks_list)

        return task
    except Exception as e:
        print(f"Error creating task: {e}")
        return None

def list_tasks(status):
    try:
        tasks_list = load_tasks()
        columns = ['ID', 'Status', 'Description', 'CreatedAt', 'UpdatedAt']

        header = f" {'ID':<8}  {'Status':<11}  {'Description':<30}  {'CreatedAt':19}  {'UpdatedAt':19}"
        print(header)

        if status:
            tasks_list = [task for task in tasks_list if task['status'] == status]
        
        for task in tasks_list:
            row = f" {task['id']:<8}  {task['status']:<11}  {task['description']:<30}  {task['createdAt']:<19}  {task['updatedAt']:<19} "
            print(row)

    except Exception as e:
        print(f"Error reading task: {e}")

def validate_status(status):
    valid_statuses = {'todo', 'in-progress', 'done'}
    if status not in valid_statuses:
        raise argparse.ArgumentTypeError(f"Invalid status '{status}'. Must be one of {', '.join(valid_statuses)}.")
    return status

def update_task(task_id, description=None):
    try:
        print(f"Updating the task...")
        tasks_list = load_tasks()
        task = next((task for task in tasks_list if task['id'] == task_id), None)

        if task:
            if description:
                task['description'] = description
            task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            save_tasks(tasks_list)

        return task
    except Exception as e:
        print(f"Error updating task: {e}")
        return None

def delete_task(task_id):
    try:
        print(f"Deleting the task...")
        tasks_list = load_tasks()
        tasks_list = [task for task in tasks_list if task['id'] != task_id]
        save_tasks(tasks_list)
    except Exception as e:
        print(f"Error deleting task: {e}")
        return None

def mark_in_progress(task_id):
    try:
        print(f"Changing task status...")
        tasks_list = load_tasks()
        task = next((task for task in tasks_list if task['id'] == task_id), None)

        if task:
            task['status'] = 'in-progress'
            task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            save_tasks(tasks_list)

        return task
    except Exception as e:
        print(f"Error deleting task: {e}")
        return None

def mark_done(task_id):
    try:
        print(f"Changing task status...")
        tasks_list = load_tasks()
        task = next((task for task in tasks_list if task['id'] == task_id), None)

        if task:
            task['status'] = 'done'
            task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            save_tasks(tasks_list)

        return task
    except Exception as e:
        print(f"Error deleting task: {e}")
        return None


def main():

    parser = argparse.ArgumentParser(description='Task Tracker CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Subcommand 'add'
    add_parser = subparsers.add_parser('add', help='Create a new task')
    add_parser.add_argument('description', type=str, help='Task description')

    # Subcommand 'list'
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', nargs='?', default=None, type=validate_status, help='Optional status to filter tasks (todo, in-progress, done)')

    # Subcommand 'update'
    update_parser = subparsers.add_parser('update', help='Update the description of a task')
    update_parser.add_argument('id', type=str, help='Task ID')
    update_parser.add_argument('description', type=str, help='Task description')

    # Subcommand 'delete'
    delete_parser = subparsers.add_parser('delete', help='Delete task')
    delete_parser.add_argument('id', type=str, help='Task ID')

    # Subcommand 'mark-in-progress'
    in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark task status as in-progress')
    in_progress_parser.add_argument('id', type=str, help='Task ID')

    # Subcommand 'mark-done'
    done_parser = subparsers.add_parser('mark-done', help='Mark task status as done')
    done_parser.add_argument('id', type=str, help='Task ID')

    try:
        # Parsear los argumentos
        args = parser.parse_args()

        # Procesar los comandos
        # Ejecutar la acción correspondiente
        if args.command == 'add':
            add_task(args.description)
        elif args.command == 'list':
            list_tasks(args.status)
        elif args.command == 'update':
            update_task(args.id, args.description)
        elif args.command == 'delete':
            delete_task(args.id)
        elif args.command == 'mark-in-progress':
            mark_in_progress(args.id)
        elif args.command == 'mark-done':
            mark_done(args.id)
        else:
            print("Unrecognized command")
            parser.print_help()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
