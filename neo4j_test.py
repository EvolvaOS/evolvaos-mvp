from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

# 載入 .env
load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
NEO4J_DB = os.getenv("NEO4J_DATABASE", "neo4j")

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def test_connectivity():
    driver.verify_connectivity()
    print("✅ 成功連線到 AuraDB!")

def create_and_query():
    with driver.session(database=NEO4J_DB) as session:
        session.run("CREATE (p:Person {name:'TestUser'})")
        result = session.run("MATCH (p:Person) RETURN p.name AS name LIMIT 5")
        print("節點名稱：", [r["name"] for r in result])

if __name__ == "__main__":
    try:
        test_connectivity()
        create_and_query()
    finally:
        driver.close()