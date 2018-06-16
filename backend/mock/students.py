default_pic_src = 'https://images.vexels.com/media/users/3/147101/isolated/preview/b4a49d4b864c74bb73de63f080ad7930-instagram-profile-button-by-vexels.png'


class Student:
    def __init__(self, id, name, info, pic=default_pic_src):
        self.id = id
        self.name = name
        self.info = info
        self.pic = pic

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "info": self.info,
            "pic": self.pic
        }

    def __repr__(self):
        return str(self.to_json())


students = ['student 1', 'student 2', 'student 3']


def init_students():
    return students
