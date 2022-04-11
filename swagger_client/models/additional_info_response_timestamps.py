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


class AdditionalInfoResponseTimestamps(object):
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
        'creation': 'str',
        'last_modification': 'str',
        'availability': 'AdditionalInfoResponseTimestampsAvailability',
        'validity': 'list[AdditionalInfoResponseTimestampsValidity]'
    }

    attribute_map = {
        'creation': 'creation',
        'last_modification': 'lastModification',
        'availability': 'availability',
        'validity': 'validity'
    }

    def __init__(self, creation=None, last_modification=None, availability=None, validity=None, _configuration=None):  # noqa: E501
        """AdditionalInfoResponseTimestamps - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._creation = None
        self._last_modification = None
        self._availability = None
        self._validity = None
        self.discriminator = None

        if creation is not None:
            self.creation = creation
        if last_modification is not None:
            self.last_modification = last_modification
        if availability is not None:
            self.availability = availability
        if validity is not None:
            self.validity = validity

    @property
    def creation(self):
        """Gets the creation of this AdditionalInfoResponseTimestamps.  # noqa: E501

        A timestamp in `YYYY-MM-DDTHH:MM:SSZ` format that indicates when the alert was created.  # noqa: E501

        :return: The creation of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :rtype: str
        """
        return self._creation

    @creation.setter
    def creation(self, creation):
        """Sets the creation of this AdditionalInfoResponseTimestamps.

        A timestamp in `YYYY-MM-DDTHH:MM:SSZ` format that indicates when the alert was created.  # noqa: E501

        :param creation: The creation of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :type: str
        """

        self._creation = creation

    @property
    def last_modification(self):
        """Gets the last_modification of this AdditionalInfoResponseTimestamps.  # noqa: E501

        A timestamp in `YYYY-MM-DDTHH:MM:SSZ` format that indicates when the alert was last modified.  # noqa: E501

        :return: The last_modification of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :rtype: str
        """
        return self._last_modification

    @last_modification.setter
    def last_modification(self, last_modification):
        """Sets the last_modification of this AdditionalInfoResponseTimestamps.

        A timestamp in `YYYY-MM-DDTHH:MM:SSZ` format that indicates when the alert was last modified.  # noqa: E501

        :param last_modification: The last_modification of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :type: str
        """

        self._last_modification = last_modification

    @property
    def availability(self):
        """Gets the availability of this AdditionalInfoResponseTimestamps.  # noqa: E501


        :return: The availability of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :rtype: AdditionalInfoResponseTimestampsAvailability
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this AdditionalInfoResponseTimestamps.


        :param availability: The availability of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :type: AdditionalInfoResponseTimestampsAvailability
        """

        self._availability = availability

    @property
    def validity(self):
        """Gets the validity of this AdditionalInfoResponseTimestamps.  # noqa: E501

        This describes when the incident is actually occurring.   # noqa: E501

        :return: The validity of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :rtype: list[AdditionalInfoResponseTimestampsValidity]
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this AdditionalInfoResponseTimestamps.

        This describes when the incident is actually occurring.   # noqa: E501

        :param validity: The validity of this AdditionalInfoResponseTimestamps.  # noqa: E501
        :type: list[AdditionalInfoResponseTimestampsValidity]
        """

        self._validity = validity

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
        if issubclass(AdditionalInfoResponseTimestamps, dict):
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
        if not isinstance(other, AdditionalInfoResponseTimestamps):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AdditionalInfoResponseTimestamps):
            return True

        return self.to_dict() != other.to_dict()
