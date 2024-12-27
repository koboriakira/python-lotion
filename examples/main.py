from lotion import Lotion, BasePage, notion_database, notion_prop
from lotion.properties import Title, Date


@notion_prop(name="Title")
class TaskTitle(Title):
    pass


@notion_prop(name="Started At")
class TaskDate(Date):
    # PROP_NAME = "Started At"
    pass


@notion_database(database_id="1696567a3bbf803e9817c7ae1e398b71")
class Task(BasePage):
    task_title: TaskTitle
    started_at: TaskDate


lotion = Lotion.get_instance()
tasks = lotion.retrieve_pages(Task)
for task in tasks:
    print(task.task_title.text)
    print(task.started_at.start_date)

new_task = Task.create(
    properties=[
        TaskTitle.from_plain_text("New Task"),
    ]
)
created_page = lotion.create_page(new_task)
print(created_page.task_title.text)


created_page.task_title = TaskTitle.from_plain_text(text="Updated Task")
print(created_page.task_title.text)
lotion.update(created_page)
