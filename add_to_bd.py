import sqlite3


def add(name, surname):
    con = sqlite3.connect("bd.sqlite3")
    cur = con.cursor()
    cur.execute(f"INSERT INTO users ({name}) VALUES ('{surname}')")
    con.commit()
    cur.close()
    con.close()


def add_photo_to_bd(photo):
    add("photo", photo)


def add_template(width, height):
    add("template_size", f"({width}, {height})")
