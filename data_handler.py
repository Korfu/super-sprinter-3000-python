import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_stories():
    all_stories = get_csv_data()

    return all_stories

def get_csv_data():
    data = []
    with open(DATA_FILE_PATH, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            file_row = dict(row)
            data.append(file_row)
    return data