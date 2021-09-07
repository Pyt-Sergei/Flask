from faker import Faker

SEED = 1234


def generate_users(users_count):
    fake = Faker()
    fake.seed_instance(SEED)

    users = []

    for i in range(users_count):
        users.append({
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        })

    return users
