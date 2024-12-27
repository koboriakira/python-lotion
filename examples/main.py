from lotion import Lotion, BasePage, lotion
from lotion.properties import Title, Date


class TaskTitle(Title):
    PROP_NAME = "Title"


class TaskDate(Date):
    PROP_NAME = "Started At"


@lotion
class Task(BasePage):
    DATABASE_ID = "1696567a3bbf803e9817c7ae1e398b71"
    task_title: TaskTitle
    started_at: TaskDate


lotion = Lotion.get_instance()
tasks = lotion.retrieve_pages(Task)
for task in tasks:
    print(task.task_title.text)
    print(task.started_at.start_date)

new_task = Task.create(
    properties=[
        TaskTitle.from_plain_text(name=TaskTitle.PROP_NAME, text="New Task"),
    ]
)
created_page = lotion.create_page(page=new_task)
print(created_page.task_title.text)
