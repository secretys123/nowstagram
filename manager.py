# -*- encoding=UTF8 -*-

import unittest
from nowstagram import db
from nowstagram.models import User, Image, Comment
from flask_script import Manager
from nowstagram import app
import random

manager = Manager(app)

@manager.command
def run_test():
    db.drop_all()
    db.create_all()
    tests=unittest.TestLoader().discover('./')
    unittest.TextTestRunner().run(tests)

def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000)) + 'm.png'


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 100):
        db.session.add(User('User' + str(i), 'a' + str(i)))
        for j in range(0, 10):
            db.session.add(Image(get_image_url(), i + 1))
            for k in range(0, 3):
                db.session.add(Comment('This is a comment'+str(k+1), 1+10*i+j, i+1))
    db.session.commit()

    print 1, User.query.all()
    print 2, User.query.get(3)
    user=User.query.get(1)
    print user.images
    image=Image.query.get(1)
    print image.user


if __name__ == '__main__':
    manager.run()
