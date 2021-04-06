from os import path
from model.basemodel import BaseModel
import orjson

class JsonStorage(BaseModel):
    def __init__(self):
        real_storage_path = path.join(
            path.dirname(
                path.realpath(__file__)
            ), 
            "db.json"
        )
        
        if not path.isfile(real_storage_path):
            with open(real_storage_path, "w+") as storage:
                storage.write("{}")

        self.real_storage_path = real_storage_path
    def store(self, gateway, target, throw_exception=True):
        collection = self.__read_storage()
        collection_key_check = collection.get(gateway)
        
        if collection_key_check:
            if throw_exception:
                raise KeyError("Storage key is already present")
            
            return False

        # FIXME: Add url validator
        collection[gateway] = target

        return self.__put_storage(collection)
    def update(self, gateway, new_target, throw_exception=True):
        collection = self.__read_storage()
        collection_key_check = collection.get(gateway)

        if not collection_key_check:
            if throw_exception:
                raise KeyError("Key is not avalaible")
            
            return False

        # FIXME: Add URL validator
        collection[gateway] = new_target

        return self.__put_storage(collection)
    def delete(self, gateway, throw_exception=True):
        collection = self.__read_storage()
        collection_key_check = collection.get(gateway)

        if not collection_key_check:
            if throw_exception:
                raise KeyError("Key is not avalaible")
            
            return False

        del collection[gateway]

        return self.__put_storage(collection)
    def get_gateway(self, target):
        collection = self.__read_storage()
        
        for gateway in collection.keys():
            if collection[gateway] == target:
                return gateway

        return None
    def get_target(self, gateway):
        collection = self.__read_storage()
        return collection.get(gateway)
    def __read_storage(self):
        try:
            with open(self.real_storage_path, 'r') as storage:
                return orjson.loads(storage.read())
        except:
            return {}
    def __put_storage(self, object_data):
        try:
            object_data = str(orjson.dumps(object_data), "utf-8")

            with open(self.real_storage_path, 'w') as storage:
                storage.write(object_data)
        except:
            return False
        
        return True

jsonstorage = JsonStorage()