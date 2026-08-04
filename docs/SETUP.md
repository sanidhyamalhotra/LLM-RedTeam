# Setup Log

## Stage 1: Ollama installation
- OS: Windows
- Installed Ollama from ollama.com/download
- Pulled model: llama3.2 (3B params, ~2GB)
- Verified local API responds on http://localhost:11434
- Why: Ollama lets us run an LLM fully locally, avoiding API costs
  and giving us a self-hosted target that's realistic to what
  companies actually deploy internally.


### Gotcha: TemplateNotFound error
Running `python app/app.py` from the repo root failed with
`jinja2.exceptions.TemplateNotFound: chat.html`. Fixed by explicitly
setting `template_folder` in the Flask app using the script's own
file location, so template resolution doesn't depend on the working
directory the app is launched from.