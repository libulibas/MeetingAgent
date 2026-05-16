import os, sys
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()
MODEL = "claude-sonnet-4-20250514"

def claude(prompt, system="", max_tokens=2000):
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        sys.exit("Set ANTHROPIC_API_KEY (copy .env.example to .env).")
    c = Anthropic(api_key=key)
    kw = dict(model=MODEL, max_tokens=max_tokens,
              messages=[{"role": "user", "content": prompt}])
    if system:
        kw["system"] = system
    r = c.messages.create(**kw)
    return "".join(b.text for b in r.content if b.type == "text")



def process(notes: str) -> str:
    sys_p = ("You are a meeting assistant. Output markdown: ## Summary, "
             "## Decisions, ## Action Items (owner + due), ## Follow-up Email.")
    return claude(f"Meeting notes:\n\n{notes}", system=sys_p, max_tokens=2000)

if __name__ == "__main__":
    notes = sys.stdin.read() if not sys.stdin.isatty() else \
        "discussed Q3 roadmap; Ana to ship API by Fri; revisit pricing next week"
    print(process(notes))
