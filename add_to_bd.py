import sqlite3


def add(name, surname):
    con = sqlite3.connect("bd.sqlite3")
    cur = con.cursor()
    if name == "photo":
        last = cur.execute(f"SELECT id, template_size FROM users").fetchall()[-1]
        print(last[0], last[1])
        if last[1] == "":
            cur.execute(f"INSERT INTO users ({name}) VALUES ('{surname}')")
        else:
            cur.execute(f"UPDATE users set {name} = '{surname}' WHERE id = '{last[0]}'")
    else:
        last = cur.execute(f"SELECT id, photo FROM users").fetchall()[-1]
        if last[1] == "":
            cur.execute(f"INSERT INTO users ({name}) VALUES ('{surname}')")
        else:
            cur.execute(f"UPDATE users set {name} = '{surname}' WHERE id = '{last[0]}'")
    con.commit()
    cur.close()
    con.close()


def take_values():
    con = sqlite3.connect("bd.sqlite3")
    cur = con.cursor()
    last_id = cur.execute(f"SELECT id FROM users").fetchall()
    ans = cur.execute(f"SELECT photo, template_size FROM users WHERE id = '{last_id[-1][0]}'").fetchall()
    return ans


def add_photo_to_bd(photo):
    add("photo", photo)


def add_template(width, height):
    add("template_size", f"({width}, {height})")


if __name__ == "__main__":
    add("photo", "123")
    add("template_size", "(10, 10)")
