class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        conn = cls()
        conn.user = user
        conn.password = password
        return conn



conn1 = Connection.create_with_auth("Kael", 1234)
vars(conn1)

conn2 = Connection()
conn2.set_user("Naju")
conn2.set_password("4321")
vars(conn2)