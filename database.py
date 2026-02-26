from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URL

client = AsyncIOMotorClient(
    MONGO_URL,
    maxPoolSize=100,
    minPoolSize=5
)

db = client["reward_bot"]

users = db["users"]
stock = db["stock"]
products = db["products"]
logs = db["logs"]

async def create_indexes():
    await users.create_index("user_id", unique=True)
    await users.create_index("referrals")
    await logs.create_index("type")
    await logs.create_index("date")
    await stock.create_index("used")
    await stock.create_index("product")
