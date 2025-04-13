import csv
from datetime import datetime

def read_tasks():
    tasks = []
    with open('task.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            tasks.append({
                'task': row['Task'],
                'priority': row['Priority'],
                'due': datetime.strptime(row['Due Date'], '%Y-%m-%d'),
                'duration': int(row['Duration'])
            })
    return sorted(tasks, key=lambda x: (x['due'], -1 if x['priority'] == 'High' else 0))

def generate_planner(tasks):
    today = datetime.today().strftime('%Y-%m-%d')
    filename = f'planner_{today}.txt'
    with open(filename, 'w') as f:
        f.write(f"🗓️ Planner for {today}\n\n")
        for task in tasks:
            f.write(f"- {task['task']} | Due: {task['due'].strftime('%b %d')} | Priority: {task['priority']} | Duration: {task['duration']}h\n")
        f.write("\n💡 Quote of the Day: 'Success is the sum of small efforts repeated daily.'\n")
    print(f"[✅] Planner generated: {filename}")

if __name__ == "__main__":
    tasks = read_tasks()
    generate_planner(tasks)
