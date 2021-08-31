from utils.db_api.sqlite import Database

db = Database()


def test():
    db.create_table_users()

    users = db.select_all_users()
    print(f"Before add users: {users=}")

    db.add_user(1, "Fedya", "fedya@mail.ru")
    db.add_user(2, "Tolya", "Tolya@mail.ru")
    db.add_user(3, "Olga", "Olga@mail.ru")

    users = db.select_all_users()
    print(f"After add users: {users=}")

    user = db.select_user(Name="Olga")
    print(f"Get user {user}")

test()

