from livereload import Server, shell


def rebuild():
    print(1)
    

def main():
    server = Server()
    server.watch('index.html', rebuild)
    server.serve()


if __name__ == "__main__":
    main()