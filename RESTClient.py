#!/bin/python
# -*- coding: utf-8 -*-
# ####################################################################
# Copyright (C) 2016  Fridolin Pokorny, fpokorny@redhat.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
# ####################################################################

import sys
import urllib2
import json

DEFAULT_REST_API_URL='http://10.3.11.149/api/v1'
DEFAULT_REST_DEPS_URL='http://10.3.10.217/deps/v1'

# TODO: propagate meta info as well


class RESTClient(object):
    '''
    A simple REST client for API and DEPS
    '''

    def __init__(self, deps_url=DEFAULT_REST_DEPS_URL, api_url=DEFAULT_REST_API_URL):
        if api_url.endswith("/"):
            api_url = api_url[:-1]

        if deps_url.endswith("/"):
            deps_url = deps_url[:-1]

        self.deps_url = deps_url
        self.api_url = api_url

    def api_project_listing(self):
        '''
        Get listing of all available projects available in REST with analyzed API
        @return: a list of projects available
        '''
        url = self.api_url + '/project/listing'

        response = urllib2.urlopen(url)
        ret = json.loads(response.read())

        return ret['projects']

    def api_project_commits(self, proj_name):
        '''
        Get list of commits with commit date for a project
        @param proj_name: project name
        @return: list of commits with commit date
        '''
        url = self.api_url + '/project/log/' + proj_name

        response = urllib2.urlopen(url)
        ret = json.loads(response.read())

        return ret['log']

    def api_project(self, proj_name, commit):
        '''
        Get API for a project
        @param proj_name: project name
        @param commit: commit
        @return: output from API analysis
        '''
        url = self.api_url + ('/project/api/%s/%s' % (proj_name, commit))

        response = urllib2.urlopen(url)
        ret = json.loads(response.read())

        return ret['api']

    def deps_project_listing(self):
        '''
        Get listing of all available projects available in REST with analyzed dependencies
        @return: a list of projects available
        '''
        url = self.deps_url + '/project/listing'

        response = urllib2.urlopen(url)
        ret = json.loads(response.read())

        return ret['projects']

    def deps_project_commits(self, proj_name):
        '''
        Get list of commits with commit date for a project
        @param proj_name: project name
        @return: list of commits with commit date
        '''
        url = self.deps_url + '/project/log/' + proj_name

        response = urllib2.urlopen(url)
        ret = json.loads(response.read())

        return ret['log']

    def deps_project(self, proj_name, commit):
        '''
        Get output of dependency analysis for a project
        @param proj_name: project name
        @param commit: project commit
        @return: dependency analysis output
        '''
        url = self.deps_url + ('/project/deps/%s/%s' % (proj_name, commit))

        response = urllib2.urlopen(url)
        ret = json.loads(response.read())

        return ret['deps']


if __name__ == "__main__":
    # client = RESTClient()
    # print(client.api_project_listing())
    # print(client.api_project_commits('golang-github-hashicorp-hcl'))
    # print(client.api_project('golang-github-hashicorp-hcl', '7e929f0990aaed77217525533296f70753d61bc3'))
    # print(client.deps_project_listing())
    # print(client.deps_project_commits('golang-github-hashicorp-hcl'))
    # print(client.deps_project('golang-github-hashicorp-hcl', '7e929f0990aaed77217525533296f70753d61bc3'))
    sys.exit(1)
