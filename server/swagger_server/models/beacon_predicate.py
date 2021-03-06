# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class BeaconPredicate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, definition: str=None):  # noqa: E501
        """BeaconPredicate - a model defined in Swagger

        :param id: The id of this BeaconPredicate.  # noqa: E501
        :type id: str
        :param name: The name of this BeaconPredicate.  # noqa: E501
        :type name: str
        :param definition: The definition of this BeaconPredicate.  # noqa: E501
        :type definition: str
        """
        self.swagger_types = {
            'id': str,
            'name': str,
            'definition': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'definition': 'definition'
        }

        self._id = id
        self._name = name
        self._definition = definition

    @classmethod
    def from_dict(cls, dikt) -> 'BeaconPredicate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The BeaconPredicate of this BeaconPredicate.  # noqa: E501
        :rtype: BeaconPredicate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this BeaconPredicate.

        CURIE-encoded identifier of predicate resource   # noqa: E501

        :return: The id of this BeaconPredicate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this BeaconPredicate.

        CURIE-encoded identifier of predicate resource   # noqa: E501

        :param id: The id of this BeaconPredicate.
        :type id: str
        """

        self._id = id

    @property
    def name(self) -> str:
        """Gets the name of this BeaconPredicate.

        human readable name of predicate relation   # noqa: E501

        :return: The name of this BeaconPredicate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this BeaconPredicate.

        human readable name of predicate relation   # noqa: E501

        :param name: The name of this BeaconPredicate.
        :type name: str
        """

        self._name = name

    @property
    def definition(self) -> str:
        """Gets the definition of this BeaconPredicate.

        human readable definition of predicate relation provided by this beacon   # noqa: E501

        :return: The definition of this BeaconPredicate.
        :rtype: str
        """
        return self._definition

    @definition.setter
    def definition(self, definition: str):
        """Sets the definition of this BeaconPredicate.

        human readable definition of predicate relation provided by this beacon   # noqa: E501

        :param definition: The definition of this BeaconPredicate.
        :type definition: str
        """

        self._definition = definition
