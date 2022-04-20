from typing import Union
from functools import total_ordering

from sqlalchemy.sql import sqltypes, schema

from mammon_gpio.db import Base, session
from mammon_gpio.db.utils import filters, decorators


@total_ordering
class BaseModel(Base):
    """Base Model"""
    __abstract__ = True
    id = schema.Column(sqltypes.Integer, primary_key=True, autoincrement=True, unique=True)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __lt__(self, other):
        return self.id < other.id

    @classmethod
    def _filter_input(cls, **kwargs: dict) -> dict:
        """Clears the input of unnecessary arguments"""
        required_fields = cls.__table__.columns.keys()
        filtered_kwargs = filters.leave_required_keys(kwargs, required_fields)
        required_fields.remove('id')

        # Checking that all required fields have been passed
        if set(required_fields) - set(filtered_kwargs):
            raise KeyError(f"Required fields were not passed: {set(required_fields) - set(filtered_kwargs)}")

        return filtered_kwargs

    @classmethod
    @decorators.with_insertion_lock
    @decorators.inserting_errors_handling
    def set_or_get(cls, **kwargs) -> 'BaseModel':
        """Create or get an existing model"""
        filtered_kwargs = cls._filter_input(**kwargs)
        record = session.query(cls).filter_by(**filtered_kwargs).limit(1).scalar()
        if not record:
            if 'id' in filtered_kwargs:
                filtered_kwargs.pop('id')

            record = cls(**filtered_kwargs)
            session.add(record)
            session.commit()

        return record

    @classmethod
    @decorators.with_insertion_lock
    @decorators.inserting_errors_handling
    def set(cls, **kwargs) -> 'BaseModel':
        """Create a new table entry"""
        filtered_kwargs = cls._filter_input(**kwargs)

        record = cls(**filtered_kwargs)
        session.add(record)
        session.commit()

        return record

    @classmethod
    def get_all(cls, **kwargs) -> list['BaseModel']:
        """Get all records"""
        required_fields = cls.__table__.columns.keys()
        filtered_kwargs = filters.leave_required_keys(kwargs, required_fields)

        return session.query(cls).filter_by(**filtered_kwargs).all()

    @classmethod
    def get_last(cls, **kwargs) -> Union['BaseModel', None]:
        """Get the latest record from the passed data"""
        required_fields = cls.__table__.columns.keys()
        filtered_kwargs = filters.leave_required_keys(kwargs, required_fields)

        return session.query(cls).filter_by(**filtered_kwargs).limit(1).scalar()

    @decorators.with_insertion_lock
    @decorators.inserting_errors_handling
    def update(self, update: dict) -> 'BaseModel':
        """
        Update record field data
        Args:
            update (dict): Dictionary of fields with updating values

        Returns:
            BaseModel - Class instance with updated data
        """
        session.query(self.__class__).filter_by(id=self.id).update(update)
        session.commit()

        self.__dict__ |= update  # Merging dictionaries to update class entries
        return self

    @classmethod
    def get_pool_with_offset(cls, offset: int, pool: int) -> list['BaseModel']:
        """
        Get list of records with offset
        Args:
            offset (int): Offset in the list
            pool (int): Number of records

        Returns:
            list[BaseModel] - List of records of this model
        """
        return session.query(cls).order_by(cls.id.desc()).offset(offset).limit(pool).all()
