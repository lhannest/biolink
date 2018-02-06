# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class ConceptDetail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, tag: str=None, value: str=None):  # noqa: E501
        """ConceptDetail - a model defined in Swagger

        :param tag: The tag of this ConceptDetail.  # noqa: E501
        :type tag: str
        :param value: The value of this ConceptDetail.  # noqa: E501
        :type value: str
        """
        self.swagger_types = {
            'tag': str,
            'value': str
        }

        self.attribute_map = {
            'tag': 'tag',
            'value': 'value'
        }

        self._tag = tag
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'ConceptDetail':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ConceptDetail of this ConceptDetail.  # noqa: E501
        :rtype: ConceptDetail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tag(self) -> str:
        """Gets the tag of this ConceptDetail.

        property name   # noqa: E501

        :return: The tag of this ConceptDetail.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag: str):
        """Sets the tag of this ConceptDetail.

        property name   # noqa: E501

        :param tag: The tag of this ConceptDetail.
        :type tag: str
        """

        self._tag = tag

    @property
    def value(self) -> str:
        """Gets the value of this ConceptDetail.

        property value   # noqa: E501

        :return: The value of this ConceptDetail.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this ConceptDetail.

        property value   # noqa: E501

        :param value: The value of this ConceptDetail.
        :type value: str
        """

        self._value = value
