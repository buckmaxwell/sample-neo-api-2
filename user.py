__author__ = 'Max Buck'
__email__ = 'maxbuckdeveloper@gmail.com'
__version__ = '1.0.0'

from neomodel import (StringProperty, AliasProperty, RelationshipTo, Relationship, ZeroOrOne)
from serializable_structured_node import SerializableStructuredNode, SerializableStructuredRel


class User(SerializableStructuredNode):
    """
    This is an example class for showing how a SerializableStructuredNode is put together. ALL rules for StructuredNode\
    apply to SerializableStructuredNode.  Please refer to the NeoModel documentation at \
    http://neomodel.readthedocs.org/en/latest/.
    """

    __type__ = 'users'  # => __type__ must be specified and the same as the default for type

    # INFO
    version = '1.0.0'  # => A version is not required but is a good idea
    secret = ['password']  # => Variable names listed in this list don't show up in resource objects returned by the API
    hashed = ['password']  # => Variable names listed in this list are encrypted using sha256
    enums = {'gender': ['m', 'f', 'o']}  # => Enums in this dictionary can only be
    dates = ['birthday']  # => Format datetime object as date because datetime.date objects cannot be json encoded

    # ATTRIBUTES -- NOTE: 'type' and 'id' are required for json api specification compliance
    type = StringProperty(default='users')  # => required
    id = StringProperty(unique_index=True, required=True)  # => required
    email = AliasProperty(to='id')
    password = StringProperty(required=True)
    gender = StringProperty()

    # RELATIONSHIPS
    friends = Relationship('User', 'HAS_FRIEND', model=SerializableStructuredRel)
    mom = RelationshipTo('User', 'HAS_MOM', cardinality=ZeroOrOne, model=SerializableStructuredRel)
