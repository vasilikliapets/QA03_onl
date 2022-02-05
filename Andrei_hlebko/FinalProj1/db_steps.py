def create_group(db):
    query = "INSERT INTO auth_group(name) VALUES (%s)"
    values = [('Group_1')]
    db.execute(query, values)
    return db.connection.commit()


def get_group_name(db):
    query = "SELECT name FROM auth_group"
    return db.execute(query)
