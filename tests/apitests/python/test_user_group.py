# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.

    OpenAPI spec version: 1.4.0

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys

sys.path.append(os.environ["SWAGGER_CLIENT_PATH"])


import unittest
import testutils
from testutils import ADMIN_CLIENT

from v2_swagger_client.models.user_group import UserGroup
from library.configurations import Configurations
from pprint import pprint

#Testcase
#12-01-LDAP-usergroup-add
#12-02-LDAP-usergroup-update
#12-03-LDAP-usergroup-delete

class TestUserGroup(unittest.TestCase):
    """UserGroup unit test stubs"""
    product_api = testutils.GetProductApi("admin", "Harbor12345")
    usergroup_api = testutils.GetUserGroupApi("admin", "Harbor12345")
    groupId = 0
    def setUp(self):
        self.conf= Configurations()
        self.conf.set_configurations_of_ldap(ldap_filter="", ldap_group_attribute_name="cn", ldap_group_base_dn="ou=groups,dc=example,dc=com",
                                             ldap_group_search_filter="objectclass=groupOfNames", ldap_group_search_scope=2, **ADMIN_CLIENT)

    def tearDown(self):
        if self.groupId > 0 :
            self.usergroup_api.delete_user_group(group_id=self.groupId)

    def testAddUpdateUserGroup(self):
        """Test UserGroup"""
        user_group = UserGroup(group_name="harbor_group123", group_type=1, ldap_group_dn="cn=harbor_group,ou=groups,dc=example,dc=com")
        result = self.usergroup_api.create_user_group(usergroup=user_group)
        pprint(result)

        user_groups = self.usergroup_api.list_user_groups()
        found = False

        for ug in user_groups :
            if ug.group_name == "harbor_group123" :
                found = True
                print("Found usergroup")
                pprint(ug)
                self.groupId = ug.id
        self.assertTrue(found)

        result = self.usergroup_api.update_user_group(self.groupId, usergroup = UserGroup(group_name = "newharbor_group"))

        new_user_group = self.usergroup_api.get_user_group(group_id=self.groupId)
        self.assertEqual("newharbor_group", new_user_group.group_name)


if __name__ == '__main__':
    unittest.main()
