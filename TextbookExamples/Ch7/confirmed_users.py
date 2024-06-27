# start with users that need to be verified
# and an empty list to hold confirmed users.

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# confirming all users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

    # if list is empty, display all users in confirmed_users
    if not unconfirmed_users:
        for user in confirmed_users:
            print(f"{user.title()} now added...")