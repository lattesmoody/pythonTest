from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
import asyncio
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up the server...")
    scheduler.start()
    yield
    print("Shutting down the server...")
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

@app.on_event("startup")
async def startup_event():
    # 예시 작업 추가
    scheduler.add_job(lambda: print("Scheduled job running..."), 'interval', seconds=10)

@app.post("/shutdown")
async def shutdown(request: Request):
    if scheduler.get_jobs():
        return {"message": "There are still scheduled jobs running. Shutdown aborted."}
    
    async def terminate():
        print("Terminating server...")
        await asyncio.sleep(1)

        # 모든 스케줄러 작업이 완료될 때까지 대기
        while scheduler.get_jobs():
            await asyncio.sleep(1)

        # 서버를 종료합니다.
        app.state.server.should_exit = True

    asyncio.create_task(terminate())
    return {"message": "Server is shutting down..."}

async def main():
    config = uvicorn.Config(app, host="127.0.0.1", port=8000)
    server = uvicorn.Server(config)
    app.state.server = server
    try:
        await server.serve()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Server has been shut down.")

if __name__ == "__main__":
    asyncio.run(main())
