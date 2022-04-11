# coding: utf-8

"""
    Trip Planner

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class AdditionalInfoResponseAffectedLine(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'destination': 'AdditionalInfoResponseAffectedLineDestination',
        'name': 'str',
        'number': 'str',
        'product': 'RouteProduct'
    }

    attribute_map = {
        'id': 'id',
        'destination': 'destination',
        'name': 'name',
        'number': 'number',
        'product': 'product'
    }

    def __init__(self, id=None, destination=None, name=None, number=None, product=None, _configuration=None):  # noqa: E501
        """AdditionalInfoResponseAffectedLine - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._destination = None
        self._name = None
        self._number = None
        self._product = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if destination is not None:
            self.destination = destination
        if name is not None:
            self.name = name
        if number is not None:
            self.number = number
        if product is not None:
            self.product = product

    @property
    def id(self):
        """Gets the id of this AdditionalInfoResponseAffectedLine.  # noqa: E501

        This is the unique ID that identifies the given line.  # noqa: E501

        :return: The id of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdditionalInfoResponseAffectedLine.

        This is the unique ID that identifies the given line.  # noqa: E501

        :param id: The id of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def destination(self):
        """Gets the destination of this AdditionalInfoResponseAffectedLine.  # noqa: E501


        :return: The destination of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :rtype: AdditionalInfoResponseAffectedLineDestination
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this AdditionalInfoResponseAffectedLine.


        :param destination: The destination of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :type: AdditionalInfoResponseAffectedLineDestination
        """

        self._destination = destination

    @property
    def name(self):
        """Gets the name of this AdditionalInfoResponseAffectedLine.  # noqa: E501

        This is the full name of the route.  # noqa: E501

        :return: The name of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AdditionalInfoResponseAffectedLine.

        This is the full name of the route.  # noqa: E501

        :param name: The name of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number(self):
        """Gets the number of this AdditionalInfoResponseAffectedLine.  # noqa: E501

        This is the short name or code of the route.  # noqa: E501

        :return: The number of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AdditionalInfoResponseAffectedLine.

        This is the short name or code of the route.  # noqa: E501

        :param number: The number of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :type: str
        """

        self._number = number

    @property
    def product(self):
        """Gets the product of this AdditionalInfoResponseAffectedLine.  # noqa: E501

        This element contains additional properties about the route.  # noqa: E501

        :return: The product of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :rtype: RouteProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this AdditionalInfoResponseAffectedLine.

        This element contains additional properties about the route.  # noqa: E501

        :param product: The product of this AdditionalInfoResponseAffectedLine.  # noqa: E501
        :type: RouteProduct
        """

        self._product = product

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AdditionalInfoResponseAffectedLine, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdditionalInfoResponseAffectedLine):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalInfoResponseAffectedLine):
            return True

        return self.to_dict() != other.to_dict()
