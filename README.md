
🚀 Smart To-Do List Manager (2026 Edition)
Welcome to my first comprehensive Python project! This isn't just a simple list; it's a Logic-Driven Task Management System designed with a focus on data integrity, user experience, and defensive programming.
Built from scratch during my 4th month of learning Python, this project represents over 10 days of intensive logic architectural work.


🌟 Key Features:


🧠 Intelligent Data Validation (The Core)

● Advanced Logic Flow: Unlike basic apps, this system uses a "Strict-to-General" validation filter. It prioritizes Time and Status checks before assigning Titles to prevent data overlap.

● Self-Healing Storage: Integrated with JSON, the system automatically detects corrupted files or missing values (is deleted) and prompts the user for immediate repair.

● Smart Auto-Time: Features an intelligent scheduling algorithm that can automatically set task deadlines by adding 30-minute increments to the last recorded task.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

🔍 Multi-Layered Search Engine

● Temporal Categorization: A sophisticated search function that classifies tasks into Past, Present (Today), and Future views.

● Customized Filters: Users can search by Title, Status, or use a Comprehensive Search that combines all three parameters for pinpoint accuracy.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

👤 Robust User Management

● Profile Integrity: Validates user info (Name, Age, Gender, Birth) with cross-checks. It automatically calculates age based on the birth year and vice versa.

● Privacy First: Includes a "Prefer not to say" option for gender while maintaining system functionality.

● Age-Gate Protection: Implements a strict policy for users aged 7 and above.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

🎨 Minimalist Terminal UI

● Visual Feedback: Uses ANSI color coding (Green for success, Red for errors, Blue for info) to make the CLI intuitive.

● UX Touches: Features custom loading animations and "Type-writer" effects to provide a modern feel to the terminal.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

<img width="1121" height="555" alt="Screenshot (14)" src="https://github.com/user-attachments/assets/e23944df-45ee-47b3-858d-b0d1f62ba297" />

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

🛠 Project Architecture

The project is divided into a modular structure to ensure maintainability:

1. main.py: The orchestrator (The Maestro) that manages the application flow.
 
2. logic.py: Contains the Task and User classes and core validation functions.
   
3. file_logic.py: The "Scanner" module; dedicated to identifying corrupted data fields and ensuring file consistency.
  
4. storage.py: Manages JSON I/O operations and data recovery.
   
5. search_logic.py: Dedicated engine for all search and filtering operations.
 
6. ui.py: Handles terminal clearing, coloring, and timing animations.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 How to Run
1. Ensure you have Python 3.10+ installed.
2. Clone the repository.
3. Run python main.py.
4. Follow the "beautiful" prompts to manage your day!
-----------------------------------------------------------------------------------------------------------------------

“The logic was simpler than the complexity I imagined, yet the journey of building it taught me the soul of clean code.”
Developed with ❤️ by a passionate Python Learner.



