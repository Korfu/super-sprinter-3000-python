from flask import Flask, render_template, request, redirect, url_for

import data_handler

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def route_list():
    user_stories = data_handler.get_all_user_stories()

    return render_template('list.html', user_stories=user_stories)

@app.route('/add_story', methods=['GET','POST'])
def add_story():
    if request.method == 'POST':
        story = {
            'title': request.form.get('title'),
            'user_story': request.form.get('user_story'),
            'acceptance_criteria': request.form.get('acceptance_criteria'),
            'business_value': request.form.get('business_value'),
            'estimation': request.form.get('estimation')
        }

        data_handler.add_user_story(story)
        return redirect('/')

    empty_user_story = {
        'business_value': 500,
        'estimation': 2
    }

    return render_template('user_story.html',
                           story = empty_user_story,
                           form_url = url_for('add_story'),
                           page_title = "Add User Story",
                           button_title = "Add new User Story")

@app.route('/edit_story/<id>', methods=['GET','POST'])
def edit_story(id: int):
    if request.method == 'POST':
        story = {
            'id': id,
            'title': request.form.get('title'),
            'user_story': request.form.get('user_story'),
            'acceptance_criteria': request.form.get('acceptance_criteria'),
            'business_value': request.form.get('business_value'),
            'estimation': request.form.get('estimation'),
            'status': request.form.get('status')
        }

        data_handler.update_user_story(story)
        return redirect('/')

    story = next((elem for elem in data_handler.get_all_user_stories() if elem['id'] == id), None)
    return render_template('user_story.html',
                           story = story,
                           form_url = url_for('edit_story', id=story['id']),
                           page_title = "Update User Story",
                           button_title = "Update User Story",
                           statuses = data_handler.STATUSES
                           )
if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True,
    )
