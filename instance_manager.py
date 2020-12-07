# instance_manager.py
# All instances created in the PGN Viewer is managed here.


class InstanceManager:
    def __init__(self):
        self.instances = []

    def create_instance(self, **kwargs):
        """
        :param kwargs: "class": instance that you want to create. "name: name of instance.
        :return: pointer to the instance.
        """
        class_of_instance = kwargs["class"]
        name_of_instance = kwargs["name"]
        class_of_instance(kwargs)