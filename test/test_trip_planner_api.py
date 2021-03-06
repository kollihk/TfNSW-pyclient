# coding: utf-8

"""
    Trip Planner

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.trip_planner_api import TripPlannerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTripPlannerApi(unittest.TestCase):
    """TripPlannerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.trip_planner_api.TripPlannerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tfnsw_addinfo_request(self):
        """Test case for tfnsw_addinfo_request

        Provides capability to display all public transport service status and incident information (as published from the Incident Capture System).  # noqa: E501
        """
        pass

    def test_tfnsw_coord_request(self):
        """Test case for tfnsw_coord_request

        When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.  # noqa: E501
        """
        pass

    def test_tfnsw_dm_request(self):
        """Test case for tfnsw_dm_request

        Provides capability to provide NSW public transport departure information from a stop, station or wharf including real-time.  # noqa: E501
        """
        pass

    def test_tfnsw_stopfinder_request(self):
        """Test case for tfnsw_stopfinder_request

        Provides capability to return all NSW public transport stop, station, wharf, points of interest and known addresses to be used for auto-suggest/auto-complete (to be used with the Trip planner and Departure board APIs).  # noqa: E501
        """
        pass

    def test_tfnsw_trip_request2(self):
        """Test case for tfnsw_trip_request2

        Provides capability to provide NSW public transport trip plan options, including walking and driving legs, real-time and Opal fare information.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
