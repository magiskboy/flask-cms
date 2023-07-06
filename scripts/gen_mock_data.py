from faker import Faker
from cms.user.models import User, UserRole
from cms.extensions import db

faker = Faker()

photos = ["https://w7.pngwing.com/pngs/0/775/png-transparent-goku-frieza-vegeta-dragon-ball-heroes-krillin-goku-face-head-fictional-character-thumbnail.png", "https://yt3.googleusercontent.com/smXw06mtTdznHe7aWuaOjCCrGEbuXu56tDClt9BbQABUgcE-miQUdAxVoDWk9mjaX8NzyrmKHQ=s900-c-k-c0x00ffffff-no-rj", "https://w7.pngwing.com/pngs/563/712/png-transparent-sticker-ear-lucky-luke-lucky-luke-face-hand-fashion-thumbnail.png"]

def gen_user():
    u = User(
        fullname=faker.name(),
        profile_url=faker.random_element(photos),
        username=faker.user_name(),
        role=faker.random_element([UserRole.normal, UserRole.writer]),
        email=faker.email(),
    )
    u.password = faker.password()
    return u
