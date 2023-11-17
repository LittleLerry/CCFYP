import asyncio
from bilibili_api import video

async def main() -> None:
    bv = input()
    #v = video.Video(bvid="BV1uv411q7Mv")
    v = video.Video(bvid=bv)
    info = await v.get_info()
    print(info)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())