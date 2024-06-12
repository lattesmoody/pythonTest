from fastapi import FastAPI, Request, BackgroundTasks, HTTPException
from contextlib import asynccontextmanager
import asyncio
import uvicorn
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger('apscheduler').setLevel(logging.WARN)

scheduler = AsyncIOScheduler()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up the server...")
    scheduler.start()
    yield
    logger.info("Shutting down the server...")
    scheduler.shutdown()

app = FastAPI(lifespan=lifespan)

@app.post("/add_job")
async def add_job(background_tasks: BackgroundTasks):
    # 작업 추가 함수
    def job_function():
        logger.info("Scheduled job running...")

    # 백그라운드 작업으로 스케줄러 작업 추가
    job = scheduler.add_job(job_function, 'interval', seconds=10)
    job_id = job.id
    return {"message": "Job is being added in the background.", "job_id": job_id}

@app.post("/remove_job")
async def remove_job(job_id: str):
    job = scheduler.get_job(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    job.remove()
    return {"message": f"Job {job_id} has been removed."}

@app.get("/jobs/")
async def list_jobs():
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({
            "job_id": job.id,
            "name": job.name,
            "next_run_time": job.next_run_time.isoformat() if job.next_run_time else None
        })
    return jobs

@app.post("/shutdown")
async def shutdown(request: Request, background_tasks: BackgroundTasks):
    if scheduler.get_jobs():
        return {"message": "There are still scheduled jobs running. Shutdown aborted."}
    
    async def terminate():
        logger.info("Terminating server...")
        await asyncio.sleep(1)

        # 모든 스케줄러 작업이 완료될 때까지 대기
        while scheduler.get_jobs():
            await asyncio.sleep(1)

        # 서버를 종료합니다.
        app.state.server.should_exit = True

    # 백그라운드 작업으로 종료 작업 추가
    background_tasks.add_task(terminate)
    return {"message": "Server is shutting down..."}

async def main():
    config = uvicorn.Config(app, host="127.0.0.1", port=8000)
    server = uvicorn.Server(config)
    app.state.server = server
    try:
        await server.serve()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
    finally:
        logger.info("Server has been shut down.")

if __name__ == "__main__":
    asyncio.run(main())
