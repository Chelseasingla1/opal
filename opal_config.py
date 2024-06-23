from opal_common.config import opal_common_config
from opal_client.config import opal_client_config

opal_common_config.POLICY_BUNDLE_URL = "http://localhost:7002/policy"
opal_common_config.DATA_CONFIG_SOURCES = ["mysql://root:password@localhost/permit_app"] # Update with actual password

opal_client_config.OPAL_SERVER_URL = "http://localhost:7002"
