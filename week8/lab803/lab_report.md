# Lab Report: Custom Dataset Creation & Evaluation with LangSmith

**Student:** Marco Martins
**Domain:** Arduino Programming Q&A  
**Date:** April 2026  

---

## 1. Dataset Documentation

### Domain Description
This evaluation focuses on Arduino programming knowledge. Arduino is an open-source 
electronics platform widely used in education and prototyping. The dataset covers core 
programming concepts such as pin configuration, I/O functions, timing, communication 
protocols, and hardware libraries. This domain is well-suited for LLM evaluation because 
questions have clear, verifiable answers.

### Dataset Name & Description
- **Name**: `Arduino Q&A Evaluation Dataset`
- **Description**: 15 Arduino programming Q&A examples for LLM evaluation
- **LangSmith Dataset ID**: `3bec138e-329b-4599-8e3d-e2987b882d40`
- **LangSmith Project**: `arduino-qa-eval`

### Data Structure
Each example in the dataset has the following structure:

| Field      | Type   | Description                              |
|------------|--------|------------------------------------------|
| `question` | string | Input: an Arduino programming question   |
| `answer`   | string | Output: the reference (ground truth) answer |

### Examples

| # | Question | Reference Answer |
|---|----------|-----------------|
| 1 | What is the purpose of the setup() function in Arduino? | Runs once on power-on; initializes pin modes, variables, and libraries. |
| 2 | What is the difference between digitalRead() and analogRead()? | digitalRead() returns HIGH/LOW; analogRead() returns 0–1023. |
| 3 | What does pinMode() do? | Configures a pin as INPUT, OUTPUT, or INPUT_PULLUP. |
| 4 | What is the loop() function in Arduino? | Runs repeatedly after setup(); contains the main program logic. |
| 5 | How do you turn on an LED connected to pin 13? | pinMode(13, OUTPUT) in setup(); digitalWrite(13, HIGH) in loop(). |
| 6 | What is PWM in Arduino? | Simulates analog output on digital pins using analogWrite(). |
| 7 | What is the difference between delay() and millis()? | delay() blocks execution; millis() enables non-blocking timing. |
| 8 | What voltage does a standard Arduino Uno operate at? | 5V logic level. |
| 9 | What is a serial monitor used for in Arduino? | Send/receive text between Arduino and computer for debugging. |
| 10 | How do you read a button press on Arduino? | Use INPUT_PULLUP and check digitalRead() for LOW. |
| 11 | What is the difference between int and long in Arduino? | int is 16-bit; long is 32-bit for larger numbers. |
| 12 | What does the Wire library do in Arduino? | Enables I2C communication with sensors and displays. |
| 13 | What is a servo motor and how do you control it? | Use Servo library; myServo.write(angle) for 0–180 degrees. |
| 14 | What is the purpose of a pull-up resistor? | Ensures a pin reads HIGH by default, preventing floating states. |
| 15 | How do you store data permanently on an Arduino? | Use EEPROM library to read/write data that persists after power off. |

---

## 2. Implementation Code

### 2.1 Environment Setup
```python
# Load environment variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()

# Configure LangSmith
os.environ["LANGSMITH_TRACING"] = "true"   # Enable automatic tracing
os.environ["LANGSMITH_PROJECT"] = "arduino-qa-eval"  # Project name in LangSmith
```

### 2.2 Client Initialization
```python
from langsmith import Client, traceable
from langsmith.wrappers import wrap_openai  # Adds tracing to OpenAI calls
from openai import OpenAI
from openevals.llm import create_llm_as_judge
from openevals.prompts import CORRECTNESS_PROMPT

# Initialize LangSmith client
client = Client()

# Wrap OpenAI client to enable automatic LangSmith tracing
openai_client = wrap_openai(OpenAI())
```

### 2.3 Dataset Creation
```python
# Define 15 Arduino Q&A examples
examples = [
    {"question": "What is the purpose of the setup() function in Arduino?",
     "answer": "The setup() function runs once when the Arduino powers on or resets. It is used to initialize variables, pin modes, and libraries."},
    {"question": "What is the difference between digitalRead() and analogRead()?",
     "answer": "digitalRead() reads a digital pin and returns HIGH or LOW. analogRead() reads an analog pin and returns a value between 0 and 1023."},
    {"question": "What does pinMode() do?",
     "answer": "pinMode() configures a specific pin as either INPUT, OUTPUT, or INPUT_PULLUP."},
    {"question": "What is the loop() function in Arduino?",
     "answer": "The loop() function runs repeatedly after setup(). It contains the main logic of the program that executes continuously."},
    {"question": "How do you turn on an LED connected to pin 13?",
     "answer": "Use pinMode(13, OUTPUT) in setup(), then digitalWrite(13, HIGH) in loop() to turn it on."},
    {"question": "What is PWM in Arduino?",
     "answer": "PWM (Pulse Width Modulation) simulates analog output using digital pins. analogWrite() on PWM-capable pins controls LED brightness or motor speed."},
    {"question": "What is the difference between delay() and millis()?",
     "answer": "delay() pauses the program for a given number of milliseconds, blocking all execution. millis() returns the time elapsed since the program started and allows non-blocking timing."},
    {"question": "What voltage does a standard Arduino Uno operate at?",
     "answer": "The Arduino Uno operates at 5V logic level."},
    {"question": "What is a serial monitor used for in Arduino?",
     "answer": "The serial monitor is used to send and receive text data between the Arduino and a computer, useful for debugging and displaying sensor values."},
    {"question": "How do you read a button press on Arduino?",
     "answer": "Connect the button to a digital pin, use pinMode(pin, INPUT_PULLUP), then use digitalRead(pin) to check if the value is LOW when the button is pressed."},
    {"question": "What is the difference between int and long in Arduino?",
     "answer": "int stores 16-bit integers (-32768 to 32767). long stores 32-bit integers (-2,147,483,648 to 2,147,483,647), used when larger numbers are needed."},
    {"question": "What does the Wire library do in Arduino?",
     "answer": "The Wire library enables I2C communication between the Arduino and other I2C-compatible devices like sensors and displays."},
    {"question": "What is a servo motor and how do you control it with Arduino?",
     "answer": "A servo motor rotates to a specific angle. It is controlled using the Servo library with myServo.write(angle) where angle is between 0 and 180."},
    {"question": "What is the purpose of a pull-up resistor in Arduino circuits?",
     "answer": "A pull-up resistor ensures a digital pin reads HIGH by default when no signal is applied, preventing floating pin states."},
    {"question": "How do you store data permanently on an Arduino?",
     "answer": "Use the EEPROM library to read and write data to the Arduino's built-in EEPROM memory, which persists after power off."},
]

# Create dataset in LangSmith (skip if already exists)
dataset_name = "Arduino Q&A Evaluation Dataset"
existing = [d.name for d in client.list_datasets()]

if dataset_name not in existing:
    dataset = client.create_dataset(
        dataset_name,
        description="15 Arduino programming Q&A examples for LLM evaluation."
    )
    client.create_examples(
        inputs=[{"question": e["question"]} for e in examples],
        outputs=[{"answer": e["answer"]} for e in examples],
        dataset_id=dataset.id,
    )
    print(f"Created dataset with {len(examples)} examples!")
else:
    print(f"Dataset '{dataset_name}' already exists — skipping upload.")
```

### 2.4 Target Function
```python
@traceable  # Automatically logs every call to LangSmith
def answer_arduino_question(inputs: dict) -> dict:
    """
    Target function: takes a question from the dataset,
    sends it to GPT-4o-mini, and returns the model's answer.
    """
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,  # Deterministic output
        messages=[
            {"role": "system", "content": "You are an expert Arduino programming assistant. Answer questions clearly and concisely."},
            {"role": "user", "content": inputs["question"]}
        ]
    )
    return {"answer": response.choices[0].message.content.strip()}
```

### 2.5 Evaluator Setup
```python
# Create LLM-as-judge evaluator using built-in CORRECTNESS_PROMPT
_judge = create_llm_as_judge(
    prompt=CORRECTNESS_PROMPT,  # Built-in prompt from openevals
    judge=openai_client,        # Use OpenAI client as the judge
    model="gpt-4o-mini",        # Judge model
    feedback_key="correctness", # Key used to store the score
)

def correctness_evaluator(inputs: dict, outputs: dict, reference_outputs: dict) -> dict:
    """
    Evaluator function: compares model output against reference answer.
    Returns a binary score (True/False) with reasoning comment.
    """
    return _judge(inputs=inputs, outputs=outputs, reference_outputs=reference_outputs)
```

### 2.6 Evaluation Execution
```python
# Run the full evaluation experiment
results = client.evaluate(
    answer_arduino_question,            # Target function to evaluate
    data="Arduino Q&A Evaluation Dataset",  # LangSmith dataset to use
    evaluators=[correctness_evaluator], # Evaluators to score outputs
    experiment_prefix="gpt-4o-mini",    # Prefix for experiment name in LangSmith
    max_concurrency=2,                  # Max parallel API calls
)
print(results)
```

---

## 3. Evaluation Results

### LangSmith Experiment
- **Experiment name**: `gpt-4o-mini-84e708c8`
- **Link**: https://smith.langchain.com/o/3b161d59-853b-4037-9456-e4fa9d149381/datasets/3bec138e-329b-4599-8e3d-e2987b882d40/compare?selectedSessions=7c0cdef6-2cf6-4a94-9e4e-e89877377be1

### Results Summary

| Metric            | Value  |
|-------------------|--------|
| Total examples    | 15     |
| Correct (True)    | 15     |
| Incorrect (False) | 0      |
| Pass rate         | 100%   |

### Per-Question Scores

| Score | Question |
|-------|----------|
| ✅ True | What voltage does a standard Arduino Uno operate at? |
| ✅ True | What is the purpose of the setup() function in Arduino? |
| ✅ True | How do you store data permanently on an Arduino? |
| ✅ True | How do you read a button press on Arduino? |
| ✅ True | What is a serial monitor used for in Arduino? |
| ✅ True | What is the difference between int and long in Arduino? |
| ✅ True | What is the difference between digitalRead() and analogRead()? |
| ✅ True | What is the loop() function in Arduino? |
| ✅ True | What is a servo motor and how do you control it with Arduino? |
| ✅ True | What is the purpose of a pull-up resistor in Arduino circuits? |
| ✅ True | What does pinMode() do? |
| ✅ True | What does the Wire library do in Arduino? |
| ✅ True | How do you turn on an LED connected to pin 13? |
| ✅ True | What is PWM in Arduino? |
| ✅ True | What is the difference between delay() and millis()? |

### Key Findings
- GPT-4o-mini achieved a **perfect 100% pass rate** on the Arduino Q&A dataset
- The model consistently provided **more detailed answers** than the reference, while remaining factually correct
- The LLM judge correctly recognised **semantic equivalence** even when phrasing differed significantly from the reference
- Performance was **consistent across all topic areas**: basic functions, I/O, timing, communication protocols, and hardware libraries

---

## 4. Evaluation Report

### Executive Summary
GPT-4o-mini was evaluated on a custom Arduino programming Q&A dataset of 15 examples 
using LangSmith for experiment tracking and an LLM-as-judge evaluator for scoring. 
The model achieved a 100% correctness rate, demonstrating strong knowledge of Arduino 
programming concepts across all tested topics.

### Methodology

**Dataset**: 15 manually curated Arduino Q&A pairs covering core programming concepts 
including pin configuration, digital/analog I/O, PWM, timing functions, serial 
communication, and hardware libraries (Wire, Servo, EEPROM). Examples were designed 
to test a range of difficulty levels from basic (setup/loop functions) to intermediate 
(I2C communication, EEPROM storage).

**Target Function**: GPT-4o-mini with temperature=0 and a system prompt instructing 
it to act as an Arduino expert. The `@traceable` decorator and `wrap_openai` wrapper 
ensured all calls were automatically logged to LangSmith for inspection.

**Evaluator**: LLM-as-judge using openevals' built-in `CORRECTNESS_PROMPT` with 
GPT-4o-mini as the judge model. The evaluator scores each answer as True (correct) 
or False (incorrect) based on factual accuracy and semantic equivalence with the 
reference answer, and provides a reasoning comment for each decision.

### Results
The model scored 15/15 (100% pass rate). In every case, the judge confirmed that 
the model's answer was factually accurate and semantically equivalent to the reference. 
Notably, the model often provided richer answers than the reference — for example, 
explaining not just that the Arduino Uno runs at 5V but also detailing its power supply 
range — without introducing any factual errors.

### Analysis

**Strengths**: GPT-4o-mini demonstrated reliable, accurate knowledge of Arduino 
programming across all topic areas. It handled both conceptual questions (what is PWM?) 
and practical ones (how do you turn on an LED?) with equal confidence. The model's 
tendency to elaborate beyond the reference answer suggests it is well-suited for 
educational assistance use cases.

**Limitations**: The dataset is small (15 examples) and consists of straightforward 
factual questions. This makes the evaluation easy for a capable model like GPT-4o-mini 
and limits the ability to identify weaknesses. Additionally, using the same model 
(GPT-4o-mini) as both the target and the judge introduces a risk of self-preference 
bias, where the judge may favour outputs that match its own generation style.

**Limitations of binary scoring**: The True/False scoring does not distinguish between 
a perfect answer and one that is merely passable. A continuous scale (0–1) would 
provide more nuance, particularly for partially correct or overly verbose responses.

### Recommendations
1. **Expand the dataset** with harder questions covering edge cases, common beginner 
   mistakes, and advanced topics (interrupts, timers, memory management)
2. **Use a stronger judge model** such as GPT-4o to reduce self-preference bias
3. **Add a conciseness evaluator** to penalise unnecessarily long answers, which 
   matter in educational and embedded contexts
4. **Establish a baseline** by running the same evaluation with a weaker model 
   (e.g. GPT-3.5-turbo) to create a meaningful performance comparison
5. **Test with ambiguous questions** to probe the model's ability to handle 
   uncertainty and avoid hallucination