from flask_login import UserMixin
from common.utils import JsonSerializable

class User(UserMixin, JsonSerializable):
    def __init__(self, id, email, username, first_name, last_name, roles = []):
        self.id = id
        self.email = email
        self.username = username
        # self.first_name = first_name
        # self.last_name = last_name
        # pseudo-serializer for loading from json (map dict role to Role)
        if roles and type(roles[0]) == dict:
            from roles.models import Role
            roles = [Role(**r) for r in roles]
        self.roles = roles
        self.authenticated = False
        self.first_name = first_name
        self.last_name = last_name
    def is_active(self):
        return self.is_active()
    def is_anonymous(self):
        return False
    def is_authenticated(self):
        return self.authenticated
    def is_active(self):
        return True
    def get_id(self):
        return str(self.id)
    # usable in templates and views to check if user has a role
    def has_role(self, role):
        for r in self.roles:
            if r.name in [role, "Admin"]: # if has Admin role, always allow
                return True
        return False
    def has_one_of_roles(self, roles):
        _roles = [list(roles), "Admin"]
        for r in self.roles:
            if r.name in _roles:
                return True
        return False
    # def get_first_name(self):
    #     return self.first_name
    # def get_last_name(self):
    #     return self.last_name