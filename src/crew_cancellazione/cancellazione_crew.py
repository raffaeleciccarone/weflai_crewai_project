from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from tools.tool import llm

from tools.tool import (
    list_tables_tool,
    tables_schema_tool,
    execute_sql_tool
)

#parte per API


#config. Agents e Tasks
@CrewBase
class CancellazioneCrew():

    agents: List[BaseAgent]
    tasks: List[Task]

    
    agents_config = "config/agents_cancellazione.yaml"
    tasks_config = "config/tasks_cancellazione.yaml"

    #definizione degli agenti
    @agent
    def flight_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['flight_analyst'],
            llm=llm,
            verbose=True,
            tools=[list_tables_tool, tables_schema_tool, execute_sql_tool]
        )
    @agent
    def booking_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['booking_manager'],
            llm=llm,
            verbose=True,
            tools=[execute_sql_tool]
        )

    #definizione delle task
    @task
    def find_booking_to_cancel_task(self) -> Task:
        return Task(
            config=self.tasks_config["find_booking_to_cancel_task"],
            agent=self.flight_analyst()
        )

    @task
    def delete_booking_task(self) -> Task:
        return Task(
            config=self.tasks_config["delete_booking_task"],
            context=[self.find_booking_to_cancel_task()],
            agent=self.booking_manager()
        )
    
    #definizione della crew di cancellazione
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,   
            process=Process.sequential,
            verbose=True,
        )