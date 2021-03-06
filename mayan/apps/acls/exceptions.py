class ACLsBaseException(Exception):
    """
    Base exception for the acls app
    """


class PermissionNotValidForClass(ACLsBaseException):
    """
    The permission is not one that has been registered for a class using the
    ModelPermission class.
    """
