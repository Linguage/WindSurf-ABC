"""
Planning Mode Demo
"""
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class Task:
    id: str
    description: str
    dependencies: List[str]
    status: str = "pending"

class PlanningDemo:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self._initialize_tasks()
    
    def _initialize_tasks(self):
        """Initialize demo tasks"""
        self.tasks = {
            "task1": Task("task1", "Initialize project", []),
            "task2": Task("task2", "Setup dependencies", ["task1"]),
            "task3": Task("task3", "Implement core features", ["task2"]),
            "task4": Task("task4", "Write tests", ["task3"]),
            "task5": Task("task5", "Deploy application", ["task4"])
        }
    
    def get_ready_tasks(self) -> List[Task]:
        """Get tasks that are ready to be executed (no pending dependencies)"""
        ready = []
        for task in self.tasks.values():
            if task.status != "pending":
                continue
                
            all_deps_complete = all(
                self.tasks[dep_id].status == "completed"
                for dep_id in task.dependencies
            )
            
            if all_deps_complete or not task.dependencies:
                ready.append(task)
        return ready
    
    def complete_task(self, task_id: str):
        """Mark a task as completed"""
        if task_id in self.tasks:
            self.tasks[task_id].status = "completed"
    
    def run(self):
        """Run the planning demo"""
        print("Initializing project planning...")
        print("Task Dependencies:")
        for task in self.tasks.values():
            deps = ", ".join(task.dependencies) if task.dependencies else "None"
            print(f"- {task.id}: {task.description} (Depends on: {deps})")
        
        print("\nExecuting tasks in order:")
        completed_tasks = []
        
        while len(completed_tasks) < len(self.tasks):
            ready_tasks = self.get_ready_tasks()
            
            if not ready_tasks:
                print("No more tasks can be executed. Possible circular dependency.")
                break
                
            for task in ready_tasks:
                print(f"  ✓ {task.id}: {task.description}")
                self.complete_task(task.id)
                completed_tasks.append(task.id)
        
        print("\nAll tasks completed successfully!")
