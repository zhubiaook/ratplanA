from fabric2 import Connection


def main():
    c = Connection("root@118.25.173.231", connect_kwargs={"password": "224517@ok"})
    c.run('ls')


if __name__ == '__main__':
    main()
