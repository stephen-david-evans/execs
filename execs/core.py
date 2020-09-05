"""Basic implementation of an Entity Component System
"""
import uuid
import inspect
import itertools

from . import utils


def component(cls):
    """Class decorator which registers input cls with world and adds a basic __repr__ if not defined"""
    if cls.__repr__ is object.__repr__:
        cls.__repr__ = utils.component_repr
    return World.register(cls)


def system(func):
    """function decorator to register func as a system"""
    World.add_system(func)
    return func


class World:
    """Storage, tracker, and manipulator for all entities, components, and systems"""

    components = {}
    entities = {}
    systems = []

    def __repr__(self):
        return (
            f"{type(self).__name__}(components={self.components},"
            f" entities={tuple(self.entities.keys())})"
        )

    @classmethod
    def register(cls, component):
        """register a new component - called when decorating class with component"""
        cls.components[component] = set()
        return component

    @classmethod
    def add_system(cls, func):
        """add system to storage"""
        cls.systems.append(func)

    @classmethod
    def run_systems(cls):
        """run all systems"""
        for system in cls.systems:
            system()

    @classmethod
    def add(cls, entity, component):
        """Add entity + component to world"""
        try:
            cls.components[type(component)].add(entity.uuid)
        except KeyError:
            raise KeyError(f"No registered component: {type(component).__name__}")
        cls.entities[entity.uuid] = entity

    @classmethod
    def create(cls):
        """Create and return new entity"""
        entity = Entity()
        cls.entities[entity.uuid] = entity
        return entity

    @classmethod
    def gather(cls, component, where=lambda x: True):
        """Gather all entities with given component attached"""
        uuids = cls.components[component]
        return (cls.entities[uuid] for uuid in uuids if where(cls.entities[uuid]))

    @classmethod
    def join(cls, *args, where=lambda x: True):
        """Join components that have all provided components attached"""
        uuids = set.intersection(*(cls.components[c] for c in args))
        return (cls.entities[uuid] for uuid in uuids if where(cls.entities[uuid]))

    @classmethod
    def product(cls, *args):
        return itertools.product(*[tuple(cls.gather(c)) for c in args])


class Entity:
    def __init__(self):
        self.uuid = uuid.uuid4().int

    def __repr__(self):
        components = (c for c in self.__dict__.values() if type(c) in World.components)
        return f"{type(self).__name__}(uuid={self.uuid}, components={tuple(components)})"

    def attach(self, component):
        World.add(self, component)
        self.__dict__[utils.camel_to_snake(type(component).__name__)] = component
        return self
