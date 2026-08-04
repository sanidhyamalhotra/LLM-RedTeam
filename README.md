# LLM Red Team Lab

A hands-on offensive/defensive security lab targeting a locally-hosted 
LLM chatbot, built to learn practical AI security through attack and 
defense — rather than just reading about it.

## What this is

This project simulates a realistic scenario: a company deploys an 
internal LLM-powered chatbot (built here with Flask + a local Ollama 
model) that's meant to follow strict rules and protect sensitive 
information. I attack it using real-world adversarial techniques — 
prompt injection, jailbreaking, and indirect injection — then build 
and test guardrail defenses against those same attacks.

Every attack is logged, mapped to a MITRE ATLAS technique (the 
AI/ML-focused equivalent of MITRE ATT&CK), and compared before/after 
defenses were added.

## Why I built this

AI/ML systems are being deployed everywhere with security practices 
that are years behind traditional application security. This project 
was my way of applying red team / blue team methodology — the same 
approach I used in my MITRE ATT&CK threat hunting work — to this 
emerging attack surface.

## What's inside

- A Flask-based chatbot backed by a locally-hosted LLM (Ollama, 
  llama3.2) — zero API cost, fully self-hosted
- A structured attack log covering prompt injection, jailbreaking, 
  and indirect (document-based) injection, each mapped to MITRE ATLAS
- A guardrail layer (input/output filtering) built to defend against 
  the logged attacks
- A before/after comparison showing attack success rate with and 
  without defenses
- Full documentation of setup, methodology, and findings (see /docs)

## Tech stack

Python · Flask · Ollama (local LLM runtime) · MITRE ATLAS · SQLite 
(logging)

## Status

🚧 In progress — see `docs/` for the running build log.
