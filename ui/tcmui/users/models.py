"""
User-related remote objects.

"""
import urllib

from ..core.api import RemoteObject, ListObject, fields
from ..core.models import Company
from ..static.fields import StaticData



class User(RemoteObject):
    company = fields.Locator(Company)
    email = fields.Field()
    firstName = fields.Field()
    lastName = fields.Field()
    password = fields.Field()
    screenName = fields.Field()
    userStatus = StaticData("USERSTATUS")


    def __unicode__(self):
        return self.screenName


    @classmethod
    def current(cls, **kwargs):
        kwargs["url"] = "users/current"
        return cls.get(**kwargs)


    def activate(self, **kwargs):
        self._put(relative_url="activate", **kwargs)


    def deactivate(self, **kwargs):
        self._put(relative_url="deactivate", **kwargs)


    def emailchange(self, newemail, **kwargs):
        self._put(
            relative_url="emailchange/%s" % urllib.quote(newemail),
            **kwargs
        )


    def emailconfirm(self, **kwargs):
        self._put(relative_url="emailconfirm", **kwargs)


    def passwordchange(self, newpassword, **kwargs):
        self._put(
            relative_url="passwordchange/%s" % urllib.quote(newpassword),
            **kwargs
        )


    def login(self, **kwargs):
        self._put(
            url="users/login",
            version_payload=False,
            update_from_response=False,
            **kwargs
            )


    def logout(self, **kwargs):
        self._put(
            url="users/logout",
            version_payload=False,
            update_from_response=False,
            **kwargs
            )



class UserList(ListObject):
    entryclass = User
    api_name = "users"
    default_url = "users"

    entries = fields.List(fields.Object(User))


    def __unicode__(self):
        return u"%s Users" % len(self)
