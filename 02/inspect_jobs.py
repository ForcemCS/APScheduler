import sqlite3
import pickle

DB_FILE = 'jobs.sqlite'
TABLE_NAME = 'apscheduler_jobs'

try:
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    print(f"Inspecting table '{TABLE_NAME}' in database '{DB_FILE}'...")

    # 从数据库中获取所有任务的二进制数据
    cursor.execute(f"SELECT id, job_state FROM {TABLE_NAME}")
    rows = cursor.fetchall()

    if not rows:
        print("No jobs found in the database.")
    else:
        print(f"Found {len(rows)} job(s).")
        print("-" * 30)

    for row in rows:
        job_id, job_state_blob = row

        # 使用 pickle 反序列化二进制数据
        job_state = pickle.loads(job_state_blob)

        print(f"Job ID: {job_id}")
        print("Job Details:")
        # 使用更美观的方式打印字典
        for key, value in job_state.items():
            print(f"  - {key}: {value}")
        print("-" * 30)

except sqlite3.OperationalError:
    print(f"Error: Database file '{DB_FILE}' or table '{TABLE_NAME}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'conn' in locals() and conn:
        conn.close()
