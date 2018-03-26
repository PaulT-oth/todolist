from bottle import run, route, get, post, debug, template, static_file, request, redirect
from pymongo import MongoClient
import sqlite3

import sqlite_chores as chore_list


@route('/', method='GET')
def home():

    if request.GET.submit:
        chore = request.GET.chore.strip()
        person = request.GET.person.strip()
        status = request.GET.status

        chore, person, status = set_default_values(chore, person, status)

        add_chore(chore, person, status)
        return redirect('/')


    chores = chore_list.get_chores()
    output = template('test', rows = chores)
    return output


@route('/delete<_id>', method="GET")
def delete(_id):
    chore_list.delete_chore(_id)
    return redirect('/')


def set_default_values(chore, person, status):
    if chore == "":
        chore = "Freed Fank"
    if person == "":
        person = "Elizabath"
    if status == "":
        status = "57"
    return chore, person, status


def add_chore(chore, person, status):
    chore_list.save_chore({"desk":chore, "person":person, "status":status})


@get('/static/<filepath:path>')
def server_static(filepath):
    print(filepath)
    return static_file(filepath, root='./static')

def setup():
    chore_list.save_chore({"desk":"feed fishes", "person":"Mommy", "status":"0"})


######setup()
debug(True)
run(host="0.0.0.0", port=8080, reloader=True)