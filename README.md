# Task Trascker CLI

Task Tracker CLI is a command-line application that makes it easy to manage tasks using a JSON file. With this tool, you can add, update, mark and delete tasks, as well as view a list of tasks filtered by their status.

## Features

- **Add Task**: Allows you to add a new task with a description and a default status of "todo".
- **List Tasks**: Displays a list of all tasks, or filters by status (to do, in progress, completed, or all).
- **Update Task Description**: Updates the description of an existing task based on its ID.
- **Change Task Status**: Updates the status of a task to "in progress" or "completed" based on its ID.
- **Delete Task**: Removes an existing task based on its ID.

## Usage
### Add Task

To add a new task, use the `add` subcommand:

```bash
py main.py add "New Task Description"
```

### Update Task

To update a task description, use the `update` subcommand with the `id` and `description` positional arguments:

```bash
py main.py update id_code "New Description"
```

### Delete Task

To delete a task, use the `delete` subcommand:

```bash
py main.py delete id_code
```

### Changing the status of a task

To change the status of a task, use the `mark-in-progress` or `mark-done` subcommands:

```bash
py main.py mark-in-progress id_code

py main.py mark-done id_code
```

### List tasks

To list all tasks, use the `list` subcommand:

```bash
py main.py list
```
You can also list tasks according to their status, you can add a status as an argument either `todo`, `in-progress`, `done`:
```bash
py main.py list todo
py main.py list in-progress
py main.py list done
```

## Notes

- This project uses Python. You can download and install Python from the official site: [Python.org](https://www.python.org/).
- The JSON file must be located in the same directory as the script.
- The JSON file will be created automatically if it doesn't already exist.

## Project Link

You can find more information about this project at the following link: [Roadmaps Task Tracker CLI Project](https://roadmap.sh/projects/task-tracker).