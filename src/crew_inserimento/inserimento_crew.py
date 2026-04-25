from typing import List
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from models.models import TicketOutput
from tools.tool import llm

from tools.tool import (
    list_tables_tool,
    tables_schema_tool,
    execute_sql_tool
)


#parte per API



#config. Agents e Tasks
@CrewBase
class InserimentoCrew():

    agents: List[BaseAgent]
    tasks: List[Task]

    
    agents_config = "config/agents_inserimento.yaml"
    tasks_config = "config/tasks_inserimento.yaml"

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

    @agent
    def customer_experience_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_experience_agent'],
            llm=llm,
            verbose=True,
            tools=[]  # Non ha bisogno di tool SQL - usa i dati dal context dei task precedenti
        )

    #definizione delle task
    @task
    def search_flight_task(self) -> Task:
        return Task(
            config=self.tasks_config["search_flight_task"],
            agent=self.flight_analyst()  # Agente esplicito
        )
    @task
    def insert_booking_task(self) -> Task:
        return Task(
            config=self.tasks_config["insert_booking_task"],
            context=[self.search_flight_task()],
            agent=self.booking_manager()  # Agente esplicito
        )
    @task
    def generate_ticket_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_ticket_task"],
            output_pydantic=TicketOutput,        
            output_file="ticket_generato.json",   
            context=[self.search_flight_task(), self.insert_booking_task()],
            agent=self.customer_experience_agent()  # CRITICO: necessario per output_pydantic
        )
    
    #definizione della crew di inserimento
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,   
            process=Process.sequential,
            verbose=True,
        )