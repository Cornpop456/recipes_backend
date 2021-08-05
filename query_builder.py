def insert_recipe(cur, con, recipe):
    cur.execute("insert into recipes values (NULL, ?, ?, ?, ?)", (recipe.name, ":".join(
        recipe.ingredients), ":".join(recipe.steps), recipe.type))
    con.commit()
    return cur.lastrowid


def delete_recipe(cur, con, id):
    cur.execute("delete from recipes where id=?", (id,))
    con.commit()


def get_recipes(cur):
    cur.execute("select * from recipes")
    return [{
        "id": el[0],
        "name": el[1],
        "ingredients": el[2].split(":"),
        "steps": el[3].split(":"), "type": el[4]} for el in cur.fetchall()]
