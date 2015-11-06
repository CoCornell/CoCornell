from datetime import datetime


class SerializableModel(object):
    """	A SQLAlchemy model mixin class that can serialize itself as JSON. """

    def to_dict(self):
        """Return dict representation of class by iterating over database columns."""
        value = {}
        for column in self.__table__.columns:
            attribute = getattr(self, column.name)
            if isinstance(attribute, datetime):
                attribute = str(attribute)
            value[column.name] = attribute
        return value
