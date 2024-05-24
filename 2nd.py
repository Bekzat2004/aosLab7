class AccessControlList:
    def __init__(self):
        self.users = {}
        self.groups = {}

    def add_user(self, username):
        if username not in self.users:
            self.users[username] = set()
            print(f"User '{username}' added.")
        else:
            print(f"User '{username}' already exists.")

    def add_group(self, groupname):
        if groupname not in self.groups:
            self.groups[groupname] = set()
            print(f"Group '{groupname}' added.")
        else:
            print(f"Group '{groupname}' already exists.")

    def assign_user_to_group(self, username, groupname):
        if username in self.users and groupname in self.groups:
            self.users[username].add(groupname)
            print(f"User '{username}' assigned to group '{groupname}'.")
        else:
            print(f"User '{username}' or group '{groupname}' does not exist.")

    def set_permission(self, groupname, permission):
        if groupname in self.groups:
            self.groups[groupname].add(permission)
            print(f"Permission '{permission}' added to group '{groupname}'.")
        else:
            print(f"Group '{groupname}' does not exist.")

    def check_permission(self, username, permission):
        if username in self.users:
            for group in self.users[username]:
                if permission in self.groups[group]:
                    return True
        return False

acl = AccessControlList()

acl.add_user("alice")
acl.add_user("bob")
acl.add_group("admin")
acl.add_group("user")

acl.assign_user_to_group("alice", "admin")
acl.assign_user_to_group("bob", "user")

acl.set_permission("admin", "read")
acl.set_permission("admin", "write")
acl.set_permission("user", "read")

print(acl.check_permission("alice", "read"))   # True
print(acl.check_permission("alice", "write"))  # True
print(acl.check_permission("bob", "read"))     # True
print(acl.check_permission("bob", "write"))    # False
