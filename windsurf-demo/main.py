"""
Windsurf Demo: Showcasing Planning Mode and Wave 10
"""
from planning.planner import PlanningDemo
from wave10.wave10_demo import Wave10Demo

def main():
    print("=== Windsurf Demo ===\n")
    
    # Demonstrate Planning Mode
    print("1. Planning Mode Demo")
    print("-" * 30)
    planning_demo = PlanningDemo()
    planning_demo.run()
    
    print("\n" + "=" * 50 + "\n")
    
    # Demonstrate Wave 10
    print("2. Wave 10 Demo")
    print("-" * 30)
    wave10_demo = Wave10Demo()
    wave10_demo.run()

if __name__ == "__main__":
    main()
