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


class TripRequestResponseJourney(object):
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
        'rating': 'int',
        'is_additional': 'bool',
        'legs': 'list[TripRequestResponseJourneyLeg]',
        'fare': 'TripRequestResponseJourneyFare'
    }

    attribute_map = {
        'rating': 'rating',
        'is_additional': 'isAdditional',
        'legs': 'legs',
        'fare': 'fare'
    }

    def __init__(self, rating=None, is_additional=None, legs=None, fare=None, _configuration=None):  # noqa: E501
        """TripRequestResponseJourney - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._rating = None
        self._is_additional = None
        self._legs = None
        self._fare = None
        self.discriminator = None

        if rating is not None:
            self.rating = rating
        if is_additional is not None:
            self.is_additional = is_additional
        if legs is not None:
            self.legs = legs
        if fare is not None:
            self.fare = fare

    @property
    def rating(self):
        """Gets the rating of this TripRequestResponseJourney.  # noqa: E501

        XXX  # noqa: E501

        :return: The rating of this TripRequestResponseJourney.  # noqa: E501
        :rtype: int
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this TripRequestResponseJourney.

        XXX  # noqa: E501

        :param rating: The rating of this TripRequestResponseJourney.  # noqa: E501
        :type: int
        """

        self._rating = rating

    @property
    def is_additional(self):
        """Gets the is_additional of this TripRequestResponseJourney.  # noqa: E501

        XXX  # noqa: E501

        :return: The is_additional of this TripRequestResponseJourney.  # noqa: E501
        :rtype: bool
        """
        return self._is_additional

    @is_additional.setter
    def is_additional(self, is_additional):
        """Sets the is_additional of this TripRequestResponseJourney.

        XXX  # noqa: E501

        :param is_additional: The is_additional of this TripRequestResponseJourney.  # noqa: E501
        :type: bool
        """

        self._is_additional = is_additional

    @property
    def legs(self):
        """Gets the legs of this TripRequestResponseJourney.  # noqa: E501

        This element contains one or more legs that constitute the trip.  # noqa: E501

        :return: The legs of this TripRequestResponseJourney.  # noqa: E501
        :rtype: list[TripRequestResponseJourneyLeg]
        """
        return self._legs

    @legs.setter
    def legs(self, legs):
        """Sets the legs of this TripRequestResponseJourney.

        This element contains one or more legs that constitute the trip.  # noqa: E501

        :param legs: The legs of this TripRequestResponseJourney.  # noqa: E501
        :type: list[TripRequestResponseJourneyLeg]
        """

        self._legs = legs

    @property
    def fare(self):
        """Gets the fare of this TripRequestResponseJourney.  # noqa: E501


        :return: The fare of this TripRequestResponseJourney.  # noqa: E501
        :rtype: TripRequestResponseJourneyFare
        """
        return self._fare

    @fare.setter
    def fare(self, fare):
        """Sets the fare of this TripRequestResponseJourney.


        :param fare: The fare of this TripRequestResponseJourney.  # noqa: E501
        :type: TripRequestResponseJourneyFare
        """

        self._fare = fare

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
        if issubclass(TripRequestResponseJourney, dict):
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
        if not isinstance(other, TripRequestResponseJourney):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TripRequestResponseJourney):
            return True

        return self.to_dict() != other.to_dict()
