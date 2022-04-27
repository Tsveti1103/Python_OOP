class Registration:
    @staticmethod
    def add_user(user, library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        else:
            library.user_records.append(user)

    @staticmethod
    def remove_user(user, library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id, new_username, library):
        for user in library.user_records:
            if user_id == user.user_id:
                if new_username == user.username:
                    return "Please check again the provided username - it should be different than the username used so far!"
                else:
                    if user.username in library.rented_books.keys():
                        library.rented_books[new_username] = library.rented_books[user.username]
                        del library.rented_books[user.username]
                    user.username = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"

        return f"There is no user with id = {user_id}!"
