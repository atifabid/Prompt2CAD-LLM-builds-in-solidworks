# Prompt2CAD (previously referred to as Text2CAD) 

**CAD+LLM: LLM integration to build CAD in SolidWorks by Atif (its not just tool calling)**

This is a prototype enables a user to generate CAD geometry in SolidWorks directly from natural language prompts using a locally hosted Large Language Model (LLM). The project was made open source to help contritbution from community and further development. As a basic ethical practice it is certainly expected that anyone using this repo/ idea shall tag this author in your integrations and further enhancements.

---

##  Built Using
- **Python**
- **Local LLM (Meta’s LLaMA 3)**
- **Flask Web Framework**
- **ChatGPT (for development assistance)**
- **SolidWorks Software Installed Locally**

---

## 💡 What It Does
- Accepts **natural language input** like:  
  *"Create a solid cylinder with 30mm radius and 40mm height"*
- Parses dimensions and intent using LLM
- Automates **SolidWorks** to build the CAD model via Python scripts
- Shows model response + logs on a clean Flask interface

---

## 📸 Screenshots

| Interface | CAD Output |
|----------|------------|
| ![Interface](screenshots/Text2CAD_interface.png) | ![CAD](screenshots/Text2CAD_CADmodel.png) |


---

## 🚀 Getting Started

### 1. Clone this repo

       git clone https://github.com/abigit240/Text2CAD.git
       cd Text2CAD


### 2. Setup Python Environment

       pip install -r requirements.txt

### 3. Setup Local LLM

You need a local LLaMA model. You can run it using llama-cpp-python. Ensure:

The LLM is served as a local endpoint (localhost:11434)

Model used: LLaMA3 (7B recommended for decent performance)
       Example with ollama:
       ollama run llama3

### 4. Start the Flask App

        python app.py

    Then open your browser at: http://127.0.0.1:5000
### 5. Launch SolidWorks

        Make sure SolidWorks is open before generating a model — the script interfaces using its COM API.

💡 Prompt Examples

    A rectangular block of 100mm length, 20mm width, and 20mm height

    Create a solid cylinder with 40mm height and 60mm diameter

📂 Project Structure

    Text2CAD/
    ├── app.py                     # Main Flask application
    ├── create_block.py           # SolidWorks API: create block
    ├── create_solidcylinder.py   # SolidWorks API: create cylinder
    ├── templates/
    │       └── index.html            # Web interface
    ├── .gitignore
    └── README.md

❓ Why This Project?

    Generating CAD through natural language is still emerging. Most CAD tools aren't designed to interpret free-form instructions. This project:

    Shows how engineers can leverage LLMs to automate CAD prototyping

    Bridges between natural input and mechanical design tools

    Demonstrates SolidWorks automation via Windows COM API, a lesser-known but powerful capability
📢 Attribution & Tools

######################

📬 Contribute or Reach Out

   Have an idea to add cones, spheres, or assemblies? Want to collaborate on expanding LLM-based design tools?

   Feel free to fork, submit issues, or reach out on LinkedIn @https://www.linkedin.com/in/atifsohail/

📄 License

    MIT License


---

    
