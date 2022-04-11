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


class TripRequestResponseJourneyLegStopInfo(object):
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
        'timestamps': 'AdditionalInfoResponseTimestamps',
        'priority': 'str',
        'id': 'str',
        'version': 'int',
        'url_text': 'str',
        'url': 'str',
        'content': 'str',
        'subtitle': 'str'
    }

    attribute_map = {
        'timestamps': 'timestamps',
        'priority': 'priority',
        'id': 'id',
        'version': 'version',
        'url_text': 'urlText',
        'url': 'url',
        'content': 'content',
        'subtitle': 'subtitle'
    }

    def __init__(self, timestamps=None, priority=None, id=None, version=None, url_text=None, url=None, content=None, subtitle=None, _configuration=None):  # noqa: E501
        """TripRequestResponseJourneyLegStopInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._timestamps = None
        self._priority = None
        self._id = None
        self._version = None
        self._url_text = None
        self._url = None
        self._content = None
        self._subtitle = None
        self.discriminator = None

        if timestamps is not None:
            self.timestamps = timestamps
        if priority is not None:
            self.priority = priority
        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if url_text is not None:
            self.url_text = url_text
        if url is not None:
            self.url = url
        if content is not None:
            self.content = content
        if subtitle is not None:
            self.subtitle = subtitle

    @property
    def timestamps(self):
        """Gets the timestamps of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This contains a number of timestamps that describe when the alert was created, and when the described alert actually takes place and/or is relevant.   # noqa: E501

        :return: The timestamps of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: AdditionalInfoResponseTimestamps
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        """Sets the timestamps of this TripRequestResponseJourneyLegStopInfo.

        This contains a number of timestamps that describe when the alert was created, and when the described alert actually takes place and/or is relevant.   # noqa: E501

        :param timestamps: The timestamps of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: AdditionalInfoResponseTimestamps
        """

        self._timestamps = timestamps

    @property
    def priority(self):
        """Gets the priority of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This value indicates how important the service alert is. A value of `high` or `veryHigh` likely indicates that the alert will correspond to an event that impacts the ability to travel for relevant users, while `low` or `veryLow` might be more of an informational message.   # noqa: E501

        :return: The priority of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: str
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this TripRequestResponseJourneyLegStopInfo.

        This value indicates how important the service alert is. A value of `high` or `veryHigh` likely indicates that the alert will correspond to an event that impacts the ability to travel for relevant users, while `low` or `veryLow` might be more of an informational message.   # noqa: E501

        :param priority: The priority of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["veryLow", "low", "normal", "high", "veryHigh"]  # noqa: E501
        if (self._configuration.client_side_validation and
                priority not in allowed_values):
            raise ValueError(
                "Invalid value for `priority` ({0}), must be one of {1}"  # noqa: E501
                .format(priority, allowed_values)
            )

        self._priority = priority

    @property
    def id(self):
        """Gets the id of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This is a unique identifier for this particular service alert. Note that this same ID is used in XML_ADDINFO_REQUEST for the same alert.   # noqa: E501

        :return: The id of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TripRequestResponseJourneyLegStopInfo.

        This is a unique identifier for this particular service alert. Note that this same ID is used in XML_ADDINFO_REQUEST for the same alert.   # noqa: E501

        :param id: The id of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This number indicates the version of this alert. Initially when it is created it has version `1`, but if it is then updated it will have a new `lastModification` value and the version will now be `2`.   # noqa: E501

        :return: The version of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TripRequestResponseJourneyLegStopInfo.

        This number indicates the version of this alert. Initially when it is created it has version `1`, but if it is then updated it will have a new `lastModification` value and the version will now be `2`.   # noqa: E501

        :param version: The version of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def url_text(self):
        """Gets the url_text of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This field contains a title that can be used when displaying the `url` URL. This value is equivalent to the `infoLinkText` value in `XML_ADDINFO_REQUEST`.    # noqa: E501

        :return: The url_text of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: str
        """
        return self._url_text

    @url_text.setter
    def url_text(self, url_text):
        """Sets the url_text of this TripRequestResponseJourneyLegStopInfo.

        This field contains a title that can be used when displaying the `url` URL. This value is equivalent to the `infoLinkText` value in `XML_ADDINFO_REQUEST`.    # noqa: E501

        :param url_text: The url_text of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: str
        """

        self._url_text = url_text

    @property
    def url(self):
        """Gets the url of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This field contains a URL that contains additional information about the alert. This value is equivalent to the `infoLinkURL` value in `XML_ADDINFO_REQUEST`.   # noqa: E501

        :return: The url of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TripRequestResponseJourneyLegStopInfo.

        This field contains a URL that contains additional information about the alert. This value is equivalent to the `infoLinkURL` value in `XML_ADDINFO_REQUEST`.   # noqa: E501

        :param url: The url of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def content(self):
        """Gets the content of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This is the descriptive alert content. It may contain HTML tags and/or HTML entities.   # noqa: E501

        :return: The content of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TripRequestResponseJourneyLegStopInfo.

        This is the descriptive alert content. It may contain HTML tags and/or HTML entities.   # noqa: E501

        :param content: The content of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def subtitle(self):
        """Gets the subtitle of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501

        This is short summary that can be used as a heading for the alert content. It may contain HTML tags and/or HTML entities.   # noqa: E501

        :return: The subtitle of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :rtype: str
        """
        return self._subtitle

    @subtitle.setter
    def subtitle(self, subtitle):
        """Sets the subtitle of this TripRequestResponseJourneyLegStopInfo.

        This is short summary that can be used as a heading for the alert content. It may contain HTML tags and/or HTML entities.   # noqa: E501

        :param subtitle: The subtitle of this TripRequestResponseJourneyLegStopInfo.  # noqa: E501
        :type: str
        """

        self._subtitle = subtitle

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
        if issubclass(TripRequestResponseJourneyLegStopInfo, dict):
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
        if not isinstance(other, TripRequestResponseJourneyLegStopInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TripRequestResponseJourneyLegStopInfo):
            return True

        return self.to_dict() != other.to_dict()