class Singleton:
    """Simple Singleton pattern"""
    _version = "v1.0"
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance
            return cls._instance
        else:
            return cls._instance




