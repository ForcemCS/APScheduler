from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

# Define job stores
jobstores = {
    'default': MemoryJobStore(),  # In-memory store (no persistence)
    'persistent': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')  # SQLite-based persistent store
}

# Create scheduler with job stores configuration
scheduler = BackgroundScheduler(jobstores=jobstores)

def initialize_scheduler():
    scheduler.start()
    return scheduler
