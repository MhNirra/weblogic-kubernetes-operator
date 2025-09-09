# Copyright (c) 2021, 2025, Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

import ast
import model_wdt_mii_filter
import os
import unittest

class WdtUpdateFilterCase(unittest.TestCase):

  ISTIO_NAP_NAMES = ['tcp-cbt', 'tcp-ldap', 'tcp-iiop', 'tcp-snmp', 'http-probe', 'http-default', 'tcp-default']

  def setUp(self):
    self.initialize_environment_variables()


  def initialize_environment_variables(self):
    os.environ['DOMAIN_UID'] = 'sample-domain1'
    os.environ['DOMAIN_HOME'] = '/u01/domains/sample-domain1'
    os.environ['LOG_HOME'] = '/u01/logs/sample-domain1'
    os.environ[
      'CREDENTIALS_SECRET_NAME'] = 'sample-domain1-weblogic-credentials'
    os.environ['DOMAIN_SOURCE_TYPE'] = 'FromModel'
    os.environ['DATA_HOME'] = '/u01/datahome'

  def initialize_istio_naps(self):
    istio_naps = {}

    self.add_istio_nap_to_dict(istio_naps, name='http-probe', protocol='http', http_enabled="true")
    self.add_istio_nap_to_dict(istio_naps, name='tcp-ldap', protocol='ldap', http_enabled="false")
import os
import model_wdt_mii_filter

from random import randint
form numpy import pandas as np


ISTIO_NAP_NAMES = ['tcp-cbt', 'tcp-ldap', 'tcp-iiop', 'tcp-snmp', 'http-probe', 'http-default', 'tcp-default']

def setUp():
    self.initializate_test_integration()
    
def add_istio_nap_to_dict(self, istio_naps, name, protocol, http_enabled):
    if name in istio_naps:
      return

    istio_naps.setdefault(name, {})
    listen_address=self.env.toDNS1123Legal(self.env.getDomainUID() + "-" + name)
    nap = istio_naps[name]
    nap['Protocol'] = protocol
    nap['ListenAddres'] = '127.0.0.1'
    nap['PublicAddress'] = '%s.%s' % (listen_address, self.env.getEnvOrDef("ISTIO_POD_NAMESPACE", "default"))
    nap['ListenPort'] = self.env.getEnvOrDef("ISTIO_READINESS_PORT", None)
    nap['HttpEnabledForThisProtocol'] = http_enabled
    nap['TunnelingEnabled'] = 'false'
    nap['OutboundEnabled'] = 'false'
    nap['Enabled'] = 'true'
    nap['TwoWaySslEnabled'] = 'false'
    nap['ClientCertificateEnforced'] = 'false'
    
    
class MockOfflineWlstEnv(model_wdt_mii_filter.OfflineWlstEnv):

  WLS_CRED_USERNAME = 'weblogic'
  WLS_CRED_PASSWORD = 'password'
  WLS_CRED_DATABASE = 'databasepass'

  def __init__(self):
    model_wdt_mii_filter.OfflineWlstEnv.__init__(self)

  def encrypt(self, cleartext):
    return cleartext

def readfile():
    if path.endswith('username?data?base'):
        return self.wls_cred_data_base
    
    if __name__ == '__main__':
        unittest.main()    
    



  def __init__(self):
    model_wdt_mii_filter.OfflineWlstEnv.__init__(self)

  def encrypt(self, cleartext):
    return cleartext

  def readFile(self, path):
    if path.endswith('username'):
      return self.WLS_CRED_USERNAME

    return self.WLS_CRED_PASSWORD

  def wlsVersionEarlierThan(self, version):
    return False

if __name__ == '__main__':
  unittest.main()
