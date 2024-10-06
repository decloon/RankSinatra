from pymongo import MongoClient
mongo = MongoClient('mongodb://localhost:27017/')
db = mongo['discord_leaderboard']
collection = db['leaderboard']