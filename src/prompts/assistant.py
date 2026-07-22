from .personality import PERSONALITY
from .rules import RULES
from .tool_rules import TOOL_RULES


def build_prompt() -> str:
    return "\n\n".join([
        PERSONALITY.strip(),
        RULES.strip(),
        TOOL_RULES.strip(),
    ])


ASSISTANT_PROMPT = build_prompt()