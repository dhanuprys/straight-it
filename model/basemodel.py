from abc import ABC, abstractmethod

class BaseModel(ABC):
    @abstractmethod
    def store(self, gateway, target):
        """
        This method used to store link data
        """
        pass
    @abstractmethod
    def update(self, gateway, new_target):
        """
        We can update previous target with new target with this method
        """
        pass
    @abstractmethod
    def delete(self, gateway):
        """
        Used to delete selected data (gateway)
        """
        pass
    @abstractmethod
    def get_gateway(self, target):
        """
        Get gateway by target
        """
        pass
    @abstractmethod
    def get_target(self, gateway):
        """
        Get target by gateway
        """
        pass
