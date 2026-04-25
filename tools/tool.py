from crewai.tools import tool
from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool,
    ListSQLDatabaseTool,
    QuerySQLCheckerTool,
    QuerySQLDatabaseTool
)
from langchain_community.utilities.sql_database import SQLDatabase
from crewai import LLM
import os
from dotenv import load_dotenv


#config. db
db = SQLDatabase.from_uri(database_uri = "postgresql://lele:0000@localhost:5432/postgres", 
                          schema='weflai')

load_dotenv()
api_key = os.getenv("OLLAMA_API_KEY")

llm = LLM(
    model="ollama/gpt-oss:120b",
    base_url="https://ollama.com",
    extra_headers={
        "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
    },
    temperature=0
)

#config. Tools sql

@tool("list_tables")
def list_tables_tool() -> str:
    """List the available tables in the DB."""
    return ListSQLDatabaseTool(db=db).invoke("")

@tool("tables_schema")
def tables_schema_tool(tables: str) -> str:
    """Show schema & sample rows for the given tables (comma-separated)."""
    return InfoSQLDatabaseTool(db=db).invoke(tables)

@tool("execute_sql")
def execute_sql_tool(sql_query: str) -> str:
    """
    Execute a SQL query against the database.
    Supports SELECT, INSERT, UPDATE, DELETE statements.
    For INSERT with RETURNING clause, returns the generated IDs.
    
    Args:
        sql_query: The complete SQL query string to execute (e.g., "SELECT * FROM table" or "INSERT INTO table (...) VALUES (...) RETURNING id")
    
    Returns:
        For SELECT/RETURNING: List of rows as string, e.g. "[(1, 'value'), (2, 'value2')]"
        For INSERT/UPDATE/DELETE: Success message with row count
        On error: Error message starting with "SQL Error:"
    
    Example usage:
        execute_sql("SELECT id_volo FROM weflai.voli WHERE id_volo = 1")
        execute_sql("INSERT INTO weflai.prenotazioni (...) VALUES (...) RETURNING id_prenotazione")
    """
    from sqlalchemy import text
    
    # Sanitize input
    sql_query = sql_query.strip()
    if not sql_query:
        return "SQL Error: Empty query provided"
    
    print(f"\n{'='*60}")
    print(f"[EXECUTE_SQL] Query received:")
    print(f"{sql_query}")
    print(f"{'='*60}")
    
    try:
        with db._engine.connect() as connection:
            with connection.begin():
                result = connection.execute(text(sql_query))
                
                if result.returns_rows:
                    rows = result.fetchall()
                    print(f"[EXECUTE_SQL] ✅ Query returned {len(rows)} rows: {rows}")
                    return str(rows)
                else:
                    msg = f"Query executed successfully. Rows affected: {result.rowcount}"
                    print(f"[EXECUTE_SQL] ✅ {msg}")
                    return msg
                    
    except Exception as e:
        error_msg = f"SQL Error: {str(e)}"
        print(f"[EXECUTE_SQL] ❌ {error_msg}")
        return error_msg

@tool("check_sql")
def check_sql_tool(sql_query: str) -> str:
    """Check if the SQL query is correct. Returns suggestions/fixes or success message."""
    try:
        llm_checker = llm
        query_checker_tool = QuerySQLCheckerTool(db=db, llm=llm_checker)
        return query_checker_tool.invoke({"query": sql_query})
    except Exception as e:
        return f"Error using QuerySQLCheckerTool: {str(e)}"