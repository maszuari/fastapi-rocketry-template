from fastapi import FastAPI
from scheduler import app as app_rocketry

app = FastAPI()
session = app_rocketry.session

@app.post("/session/shut_down")
async def shut_down_session():
    "Shut down the scheduler"
    session.shut_down()

@app.post("/tasks/{task_name}/run")
async def run_task(task_name:str):
    "Run given task"
    task = session[task_name]
    task.force_run = True

@app.get("/tasks")
async def read_tasks():
    return list(session.tasks)

@app.get("/logs")
async def read_logs():
    "Get task logs"
    repo = session.get_repo()
    return repo.filter_by().all()

@app.get("/")
async def root():
    return {"message": "Hello World"}