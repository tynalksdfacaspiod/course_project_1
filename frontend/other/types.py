class TrackingDict(dict):
    def pop(self, key, *args, **kwargs):
        value = super().pop(key, *args, **kwargs)
        if hasattr(value, 'on_pop'):
            value.on_pop()
        return value
