import orm, asyncio
from model import users

async def test(loop):
    await orm.create_pool(loop=loop, user='ubuntu', password='ubuntu', database='throughmypain')

    u = users(user_name='Test', user_passwd='1234567890', age=24, gender='male',records_number=0,last_record_date='')

    await u.save()
    await orm.destory_pool()
     
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test(loop))

#关闭EventLoop
loop.close()