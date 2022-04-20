from flask import Flask
from flask import render_template, request, url_for, redirect, flash, session
from run import app
from main import main, download_chapters


@app.route('/', methods=['POST', 'GET'])
def index(chapter_data = None):
    if request.method == 'POST':
        data = request.form.to_dict()
        # print(data)
        cb = {
            'PDF': 'off',
            'DEL': 'off'
            }
        if data.get('checkboxPDF') != None:
            cb['PDF'] = 'on'
        if data.get('checkboxDEL') != None:
            cb['DEL'] = 'on'
        # print(data)
        if data['form'] == 'Скачать все главы':
            flag = 'get_all'
            main(data['url'], data['path'], flag, cb)
        if data['form'] == 'Получить список глав':
            flag = 'get_list'
            chapter_data, title_name = main(data['url'], data['path'], flag, cb)
            
            session['chapter_data'] = chapter_data
            session['path'] = data['path']
            session['title_name'] = title_name
            session['cb'] = cb

            return redirect(url_for('selectedChapters'))
    return render_template('index.html')

@app.route('/selectedChapters', methods=['POST', 'GET'])
def selectedChapters():
    print('xxxxxxxxx')
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        if data.get('checkboxPDF') != None:
            cb['PDF'] = 'on'
            session['cb'] = cb
        if data.get('checkboxDEL') != None:
            cb['DEL'] = 'on'
            session['cb'] = cb
        if data.get('form') != None:
            if data['form'] == 'Получить список глав':
                flag = 'get_list'
                chapter_data, title_name = main(data['url'], data['path'], flag, session['cb'])
                session['chapter_data'] = chapter_data
                session['path'] = data['path']
                session['title_name'] = title_name
                return render_template('selectedChapters.html', chapter_data = chapter_data)
            if data['form'] == 'Скачать все главы':
                flag = 'get_all'
                main(data['url'], data['path'], flag, session['cb'])
        
        download_chapters(session['chapter_data'], session['path'], request.form.getlist('checkbox[]'), session['title_name'], session['cb']) 
    return render_template('selectedChapters.html', chapter_data = session['chapter_data'])