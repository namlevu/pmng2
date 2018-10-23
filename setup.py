from productmng.models import User


def run():
    #print("[DEBUG] Setup running")
    try:
        if(len(User.objects(username="admin")) == 0):
            #print("[DEBUG] user admin is not exist")
            default_user = User(
                username="admin", fullname="administrator", email="admin@website.com")
            default_user.set_password("admin")
            default_user.save()
    except Exception as e:
        print(repr(e))
