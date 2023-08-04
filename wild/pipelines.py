import psycopg2

from .settings import POSTGRES_DATABASE


class WildPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(**POSTGRES_DATABASE)
        self.cur = self.connection.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS wild (
            id SERIAL PRIMARY KEY,
            title TEXT,
            brand TEXT,
            price NUMERIC,
            old_price NUMERIC,
            rating NUMERIC,
            review_count INTEGER
        )
    """)

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO wild(title, brand, price, old_price, rating, review_count) values(%s,%s,%s,%s,%s,%s)",
                         (item['title'], item['brand'], item['price'], item['old_price'], item['rating'], item['review_count']))
        self.connection.commit()
        return item
