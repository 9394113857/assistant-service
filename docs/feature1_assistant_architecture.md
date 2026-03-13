# 🧠 Assistant Service – Feature 1 Architecture

## Overview
Feature 1 introduces an AI-powered assistant chatbot for the e-commerce platform. The assistant allows users to interact with the system using natural language queries such as "show products", "recommend phones", "track my order", or greetings like "hello". The assistant interprets these messages, detects the intent, and routes the request to the correct backend functionality. This feature establishes the foundational architecture of the AI assistant system.

---

# 🎯 Goal of Feature 1
The primary goal of Feature 1 is to build a conversational interface that:
- Understands natural language queries from users
- Detects the user’s intent
- Routes the request to appropriate backend handlers
- Allows guest users to interact with the assistant
- Restricts sensitive actions to authenticated users
- Collects training data to improve machine learning models over time

---

# ⚙️ Hybrid Intent Detection Architecture
The assistant uses a **Hybrid Intent Detection System**, which combines three approaches:

1. Rule-Based Detection  
2. Intent-Based Handler Routing  
3. Machine Learning-Based Intent Detection  

These three layers together form the **assistant brain**.

---

# 1️⃣ Rule-Based Detection
Rule-based detection uses keyword matching to identify known patterns quickly.

Example:

User message:
show products

Detected intent:
product_query

Typical rule examples:
- "show products"
- "list products"
- "display items"

Advantages:
- Very fast
- Deterministic
- Reliable for known commands

This is the **first layer of intent detection**.

---

# 2️⃣ Intent-Based Architecture
Once the intent is detected, the assistant loads the correct handler dynamically through an **Intent Registry**.

Intent → Handler mapping:

product_query → ProductHandler  
order_tracking → OrderHandler  
recommendation → RecommendationHandler  
greeting → GreetingHandler  

Flow:

User Message  
→ Intent Detection  
→ Intent Registry  
→ Handler Execution  
→ Response Generation

This architecture follows a **Strategy Pattern**, making the assistant modular and easy to extend.

---

# 3️⃣ Machine Learning-Based Intent Detection
If rule-based detection cannot confidently determine the intent, the system falls back to an ML model.

The ML pipeline currently uses:
- TF-IDF vectorization
- Logistic Regression or Naive Bayes classification

Example:

User message:
suggest good phones

ML predicted intent:
recommendation

Training data comes from the database table:

assistant_training_logs

---

# 📊 Continuous Learning System
Every assistant interaction is stored in the training log table.

Table:
assistant_training_logs

Stored fields include:
- user_message
- predicted_intent
- confidence_score
- model_version

These logs are used for **continuous training of the ML model**.

---

# 🔄 ML Retraining Pipeline
The system includes an automated machine learning training pipeline.

Process:

User Messages  
→ Training Logs Stored in Database  
→ GitHub Actions Pipeline Executes  
→ Model Retrained  
→ New Model Saved  
→ Assistant Improves Over Time

This enables a **self-improving AI assistant system**.

---

# 🔐 Guest Access Control
Feature 1 introduces **guest assistant support with login restrictions**.

Guest users can perform general queries such as:
- view products
- ask for recommendations
- greetings

Restricted actions:
- track order
- view personal orders

Example:

Guest message:
track my order

Assistant response:
Please login to view your order status.

This ensures **security and proper access control**.

---

# 🏗 Feature 1 Architecture

Angular Chat Widget  
↓  
Assistant Flask Service  
↓  
Hybrid Intent Detection (Rule + ML)  
↓  
Intent Registry  
↓  
Intent Handler  
↓  
Product / Order / Recommendation Services  
↓  
Supabase PostgreSQL Database  
↓  
Assistant Training Logs  
↓  
ML Training Pipeline

---

# ✅ Feature 1 Status
Feature 1 is now **fully implemented and operational**.

Completed components include:
- Assistant microservice
- Chat session tracking
- Hybrid intent detection
- Intent handler architecture
- Guest assistant support
- Login restrictions for protected operations
- Training data logging
- Automated ML retraining pipeline

Feature 1 provides the **core AI assistant foundation**.

---

# 🚀 Next Step – Feature 2 (Conversation Context Memory)

Currently the assistant treats every message independently.

Example conversation today:

User: show phones  
Assistant: Here are available phones  

User: recommend one  
Assistant: Unable to determine context

Feature 2 will introduce **Conversation Context Memory**.

New system behavior:

User Message  
→ Load Chat Session  
→ Retrieve Previous Messages  
→ Context-Aware Intent Detection  
→ Response Generation

Example conversation after Feature 2:

User: show laptops  
Assistant: Here are laptops  

User: recommend one  
Assistant: MacBook Air M2 is highly recommended

Feature 2 will make the assistant **context-aware similar to ChatGPT-style assistants**.

---

# 🧠 Summary
Feature 1 implements a hybrid AI assistant architecture combining rule-based detection, intent routing, and machine learning classification. It supports guest users while enforcing login restrictions for sensitive operations and logs interactions for continuous model training. This feature forms the foundational architecture for building an intelligent conversational assistant system.