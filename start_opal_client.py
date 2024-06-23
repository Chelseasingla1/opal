from opal_client.cli import main as opal_client_main
import sys

if __name__ == "__main__":
    sys.argv = ["opal-client", "--config-file", "opal_config.yaml"]
    opal_client_main()
