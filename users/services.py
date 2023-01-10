from common.exceptions import ObjectNotFoundException
from users.models import CustomUser


class UserService:
    model = CustomUser

    @classmethod
    def get_user(cls, **filters) -> CustomUser:
        try:
            return cls.model.objects.get(**filters)
        except cls.model.DoesNotExist:
            raise ObjectNotFoundException('User not found')
