
# AI Traffic Controller

### A Developer-Focused AI Gateway & Intelligent Routing System

**Current Release: V0 — Learning Prototype**

## Overview

AI Traffic Controller is a project exploring how AI applications can intelligently route requests across different AI models and providers.

The long-term vision is to build a developer-focused AI gateway that provides a single integration point while handling model selection, conversation context, reliability, and cost optimisation behind the scenes.

Instead of developers manually managing multiple AI providers, the goal is to let the routing system decide which model is best suited for each request.

**Connect once. Let the router handle the rest.**

## The Problem

Developers building AI applications often integrate multiple providers separately.

This can create challenges involving:

- Managing different provider APIs.
- Choosing the right model for each task.
- Balancing response quality, speed and cost.
- Handling provider failures and availability.
- Maintaining conversation context when switching models.

AI Traffic Controller aims to explore a unified approach to these problems.

## Current Implementation — V0

V0 is the initial Python prototype.

It demonstrates the basic classification and routing workflow:

**User Prompt → Classification → Python Routing → AI Response**

### Features

- Uses an LLM to classify incoming prompts.
- Supports four categories: Coding, Writing, Mathematics and General.
- Routes requests through dedicated Python handler functions.
- Integrates with the Groq API.
- Uses OpenAI's GPT-OSS 120B model through Groq.
- Loads API credentials using environment variables.

## Technologies

- Python
- Groq API
- GPT-OSS 120B
- python-dotenv

## Project Roadmap

The project is being developed incrementally.

| Phase | Objective |
|---|---|
| V0 | Basic classification and routing |
| Phase 1 | Conversational chat and history |
| Phase 2 | Multiple AI provider integration |
| Phase 3 | Intelligent model selection |
| Phase 4 | Reliability, retries and failover |
| Phase 5 | Context management and memory |
| Phase 6 | Cost optimisation |
| Phase 7 | Developer API and platform |
| Phase 8 | Real-world product validation |
| Phase 9 | Potential business development |

Later phases depend on the results of earlier milestones and real-world validation.

## Long-Term Vision

The intended architecture will eventually connect applications to a unified gateway, which manages:

- Task classification and complexity.
- Model and provider selection.
- Cost, quality and latency considerations.
- Conversation context.
- Provider reliability and automatic failover.
- Usage and budget controls.

The aim is to make AI integration simpler, more reliable and more efficient for developers.

## Development Philosophy

This project is being built as a learning journey and a potential developer-infrastructure product.

The focus is on:

1. Building a working foundation.
2. Learning through implementation.
3. Improving the architecture one milestone at a time.
4. Testing with real developers before pursuing a business.

## Author

**Aditya Pauly Koonammave**

Computer Science Student  
Eötvös Loránd University (ELTE), Budapest
year 2026

---

*This is an ongoing project. Features described in the roadmap represent future goals and are not necessarily implemented in the current release.*
