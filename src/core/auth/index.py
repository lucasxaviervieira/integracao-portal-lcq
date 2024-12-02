from ldap3 import Server, Connection, ALL
from dotenv import load_dotenv
import os

load_dotenv(override=True)


class LdapAuth:
    def __init__(self):
        self.ldap_server = os.getenv("LDAP_SERVER")
        self.ldap_port = int(os.getenv("LDAP_PORT"))
        self.ldap_dn = os.getenv("LDAP_DN")

    def login(self, username, password):
        try:
            server = Server(self.ldap_server, port=self.ldap_port, get_info=ALL)
            connection = Connection(
                server, f"{self.ldap_dn}\\{username}", password, auto_bind=True
            )
            return True
        except Exception as e:
            print(f"Erro: {e}")
            return False
