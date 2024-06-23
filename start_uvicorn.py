# start_uvicorn.py
import uvicorn
from opal_common.logger import configure_logs
from opal_client.config import opal_client_config

def start():
    configure_logs()
    uvicorn.run(
        "opal_client.main:app",
        host=opal_client_config.CLIENT_API_SERVER_HOST,
        port=opal_client_config.CLIENT_API_SERVER_PORT,
        log_level=opal_client_config.LOG_LEVEL.lower(),
    )

if __name__ == "__main__":
    start()
