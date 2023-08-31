from livereload import Server, shell
from jinja2 import Environment, FileSystemLoader, select_autoescape


def rebuild():
    print(1)
    

def main():
    server = Server()
    server.watch('index.html', rebuild)
    server.serve()


if __name__ == "__main__":
    main()