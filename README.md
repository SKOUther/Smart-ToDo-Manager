🚀 Smart To-Do List Manager (2026 Edition)

Welcome to my first comprehensive Python project!

This is not just a simple to-do list.  
It is a **Logic-Driven Task Management System** built with strong focus on:

- Data integrity
- Defensive programming
- Logical flow design
- User-controlled decisions

Built from scratch during my 4th month of learning Python, this project represents over **10 days of deep logical architecture work**, experimentation, debugging, and redesign.

---

🌟 Key Features

🧠 Intelligent Data Validation (Core System)

● Strict-to-General Validation Flow  
The system validates critical data (Time, Status) before assigning Titles to prevent logical conflicts and data overlap.

● Self-Healing Storage (JSON)  
Automatically detects:
- Missing values  
- Deleted fields  
- Corrupted task data  

The system then prompts the user to repair the file instead of crashing.

● Smart Auto-Time Scheduling  
Automatically assigns task time by adding **30-minute increments** based on the last recorded task.

---

🔍 Advanced Multi-Layered Search Engine

● Search by Task Number  
Allows direct access to tasks using their numerical index.

● Temporal Classification  
Tasks are automatically categorized into:
- Past Tasks  
- Today’s Tasks  
- Future Tasks  

● Flexible Filters  
Search by:
- Title  
- Status  
- Time  
- Or a comprehensive combined search

Designed to return accurate results even when multiple tasks share similar attributes.

---

✅ Task Confirmation System

● Preview Before Saving  
Before a task is saved, the system displays the complete task details to the user.

● User Decision Control  
The task is saved **only after explicit user confirmation**.

This prevents accidental task creation and reinforces intentional input.

---

👤 Robust User Management

● Profile Integrity Checks  
Validates:
- Name
- Age
- Gender
- Birth year

Includes cross-validation:
- Age → Birth year  
- Birth year → Age  

Ensures consistency at all times.

● Privacy-First Design  
Includes a **“Prefer not to say”** gender option while maintaining full system functionality.

● Age-Gate Protection  
Restricts system usage to users aged **7 and above**.

---

🎨 Minimalist Terminal UI

● ANSI Color Feedback  
- Green → success  
- Red → errors  
- Blue → information  

● Enhanced CLI Experience  
Includes:
- Loading animations  
- Typewriter-style text output  

Designed to make terminal interaction feel modern and engaging.

---

📸 Preview

<img width="1121" height="555" alt="Project Screenshot" src="https://github.com/user-attachments/assets/e23944df-45ee-47b3-858d-b0d1f62ba297" />
<img width="946" height="442" alt="Screenshot (21)" src="https://github.com/user-attachments/assets/9bf04e44-2860-47da-a2c7-fb9456919866" />
<img width="977" height="403" alt="Screenshot (22)" src="https://github.com/user-attachments/assets/061f8a08-822d-488d-bf27-1b75c66945cc" />
<img width="987" height="482" alt="Screenshot (19)" src="https://github.com/user-attachments/assets/1e62d4cc-b21a-4a51-a89d-9a41a3b3d652" />
<img width="927" height="411" alt="Screenshot (20)" src="https://github.com/user-attachments/assets/22ba1a0d-ef8c-4afe-9fb7-dab3b65120eb" />

---

🛠 Project Architecture

The project follows a modular architecture for scalability and clarity:

1. main.py  
   The orchestrator that controls program flow.

2. logic.py  
   Contains Task and User classes and core validation logic.

3. file_logic.py  
   Data integrity scanner that detects and repairs corrupted fields.

4. storage.py  
   Handles JSON read/write operations and safe data recovery.

5. search_logic.py  
   Dedicated engine for all search, filtering, and categorization logic.

6. ui.py  
   Terminal visuals, screen control, animations, and timing effects.

---

🚀 How to Run

1. Make sure Python 3.10+ is installed.
2. Clone the repository.
3. Run:

   python main.py

4. Follow the interactive prompts to manage your tasks.

---

“The logic was simpler than the complexity I imagined,  
yet the journey of building it taught me the soul of clean code.”

Developed with ❤️ by a passionate Python learner.


