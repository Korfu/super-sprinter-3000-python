import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_stories():
    all_stories = get_csv_data()

    return all_stories

def add_user_story(story):
    story['id'] = get_next_id()
    story['status'] = STATUSES[1]

    with open(DATA_FILE_PATH, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=DATA_HEADER)
        writer.writerow(story)

def update_user_story(story):
    data = get_all_user_stories()
    with open(DATA_FILE_PATH, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=DATA_HEADER)
        writer.writeheader()
        for row in data:
            if row['id'] == story['id']:
                writer.writerow(story)
            writer.writerow(row)

def get_csv_data():
    data =[]
    with open(DATA_FILE_PATH, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            file_row = dict(row)
            data.append(file_row)
    return data

def get_next_id():
    existing_data = get_all_user_stories()

    if len(existing_data) == 0:
        return '1'

    return str(int(existing_data[-1]['id']) + 1)