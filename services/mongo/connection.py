from motor.motor_asyncio import AsyncIOMotorClient
import config

configuration = config.get_config()
connection_string = configuration['Connection']
client = AsyncIOMotorClient(connection_string)
