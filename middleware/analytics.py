from fastapi import Request


async def log_requests_middleware(request: Request, call_next):
    print(request)

    response = await call_next(request)
    return response
