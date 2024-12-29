from lotion import Lotion, BasePage, notion_database, notion_prop
from lotion.properties import Title, Date, Text, Select
from lotion.properties.multi_select import MultiSelect


@notion_prop(name="Title")
class TaskTitle(Title):
    def add_hello(self) -> str:
        return f"Hello, {self.text}"


@notion_prop(name="Started At")
class TaskDate(Date):
    # PROP_NAME = "Started At"
    pass


@notion_prop(name="Memo")
class TaskMemo(Text):
    pass


@notion_prop(name="Goal")
class TaskGoal(Text):
    pass


@notion_prop(name="Category")
class TaskCategory(Select):
    pass


@notion_prop(name="Tags")
class TaskTags(MultiSelect):
    pass


@notion_database(database_id="1696567a3bbf803e9817c7ae1e398b71")
class Task(BasePage):
    task_title: TaskTitle
    started_at: TaskDate
    memo: TaskMemo
    goal: TaskGoal
    category: TaskCategory
    tags: TaskTags


lotion = Lotion.get_instance()
tasks = lotion.retrieve_pages(Task)
for task in tasks:
    print(task.task_title.text)
    print(task.task_title.add_hello())
    print(task.started_at.start_date)
    print(task.memo.text)
    print(task.goal.text)
    print(task.category.selected_name)
    print(task.tags.values)

category = lotion.fetch_select(Task, TaskCategory, "Rent")
tag = lotion.fetch_multi_select(Task, TaskTags, ["Test", "Sample"])
new_task = Task.create(
    properties=[
        TaskTitle.from_plain_text("New Task"),
        category,
        tag,
    ]
)
created_page = lotion.create_page(new_task)
print(created_page.task_title.text)


new_task_title = TaskTitle.from_plain_text("Updated Task")
created_page.set_prop(new_task_title)
new_select = TaskCategory.from_name("Food")
created_page.set_prop(new_select)
new_tag = TaskTags.from_name(["Specified"])
created_page.set_prop(new_tag)
print(created_page.task_title.text)
lotion.update(created_page)
