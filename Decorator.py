
# decorator is just a higher order function(@)

def login_required(func):
    def wrapper_func():
        print("this is before homapage")
        print(func())
        print("this is after homepage")

    return wrapper_func()    


@login_required
def home():
    html = "this is a homepage"
    return html
home()


@login_required
def admin():
    html = " this is admin page"
    return html

admin()