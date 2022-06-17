import redis

if __name__ == '__main__':
    # Redis example
    redis_client = redis.Redis(host='localhost', port=6379, db=0)

    redis_client.set('stock', 'AAPL')
    stock = redis_client.get('stock')
    print(stock)

