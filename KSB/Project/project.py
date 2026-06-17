import os

task_list = []
next_task_id = 1

def add_task():
    global next_task_id
    task_title = input("Enter task title: ").strip()
    if task_title:
        task_list.append({"id": next_task_id, "title": task_title, "done": False})
        next_task_id += 1
        print("Task added successfully.")

def view_tasks():
    for task in task_list:
        status = "Done" if task["done"] else "Not Done"
        print(f"[{task['id']}] {task['title']} | {status}")

def mark_done():
    target_id = int(input("Enter task ID: "))
    for task in task_list:
        if task["id"] == target_id:
            task["done"] = True
            print("Task marked as Done.")

def delete_task():
    target_id = int(input("Enter task ID: "))
    for index, task in enumerate(task_list):
        if task["id"] == target_id:
            task_list.pop(index)
            print("Task deleted.")
            return

def show_stats():
    total_tasks = len(task_list)
    done_tasks = sum(1 for task in task_list if task["done"])
    not_done_tasks = total_tasks - done_tasks
    
    completion_percentage = int((done_tasks / total_tasks) * 100) if total_tasks else 0
    print(f"Total tasks: {total_tasks}\nDone: {done_tasks}\nNot done: {not_done_tasks}\nCompletion: {completion_percentage}%")

def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in task_list:
            status_bit = "1" if task["done"] else "0"
            file.write(f"{task['id']}|{task['title']}|{status_bit}\n")

def load_tasks():
    global next_task_id
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                if line.strip():
                    task_id, task_title, is_done = line.strip().split("|")
                    task_list.append({"id": int(task_id), "title": task_title, "done": is_done == "1"})
                    next_task_id = max(next_task_id, int(task_id) + 1)

def main():
    load_tasks()
    menu_text = "\n=== STUDENT TASK MANAGER ===\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Show Statistics\n6. Save & Exit"
    menu_actions = {"1": add_task, "2": view_tasks, "3": mark_done, "4": delete_task, "5": show_stats}
    
    while True:
        print(menu_text)
        user_choice = input("Choose an option: ").strip()
        if user_choice == "6":
            save_tasks()
            break
        if user_choice in menu_actions:
            menu_actions[user_choice]()

if __name__ == "__main__":
    main()