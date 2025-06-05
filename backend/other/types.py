from typing import Any

class TrackingDict(dict):
    """ Словарь с дополнительной обработкой метода pop """

    def pop(self, key, *args, **kwargs) -> Any:
        """ Переопределённый метод pop для вызова дополнительной фунции """ 
        value = super().pop(key, *args, **kwargs)
        if hasattr(value, 'on_pop'):
            value.on_pop()
        return value
