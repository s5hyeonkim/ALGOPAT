from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import json

from database.problem import insert_problem, insert_gpt_problem_summary, insert_user_submit_problem, check_problem_is_exist
from myclass.problem import ProblemSummary
from pydantic import BaseModel

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from database.problem import UserSubmitSolution, GPTSolution, Problem, UserSubmitProblem, GPTProblemSummary


from utils.shared_env import mariadb_config

config = json.loads(mariadb_config)

DATABASE_URL = f"mysql+aiomysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}?charset=utf8mb4"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# session 정보 가져오기 
async def get_session() -> AsyncSession:
    async with async_session() as session:
        return session
    
Base = declarative_base()
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all, tables=[Problem.__table__])
        await conn.run_sync(Base.metadata.create_all, tables=[UserSubmitProblem.__table__])
        await conn.run_sync(Base.metadata.create_all, tables=[GPTProblemSummary.__table__])
        await conn.run_sync(Base.metadata.create_all, tables=[UserSubmitSolution.__table__])
        await conn.run_sync(Base.metadata.create_all, tables=[GPTSolution.__table__])