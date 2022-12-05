from jinja2 import Template, FileSystemLoader, Environment

name = 'Ерема'
cars = [
    {'name': 'Pety', 'old': 19, 'weigth': 82.4},
    {'name': 'Nikol', 'old': 19, 'weigth': 78.9},
    {'name': 'Jon', 'old': 45, 'weigth': 77.2},
    {'name': 'Forest', 'old': 25, 'weigth': 75.1},
]
file_loader = FileSystemLoader('Template')
env = Environment(loader = file_loader)

tm = env.get_template('page.htm')
msg = tm.render(domain='http://proproprogs.ru', title="Pro Linja")
print(msg)