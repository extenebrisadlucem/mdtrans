import re
import uuid

class MarkdownProtector:
    # ============================================
    # ============================================
    def __init__(self):
        self.token_regex = re.compile(r"<HTML:TOKEN:[a-f0-9]+-[a-f0-9]+-[a-f0-9]+-[a-f0-9]+-[a-f0-9]+:END>")

        # MEGA PATTERN : une seule passe
        self.pattern = re.compile(
            r"("

            # Code blocks ```...```
            r"```[\s\S]*?```"

            r"|"

            # Math blocks $$...$$
            r"\$\$[\s\S]*?\$\$"

            r"|"

            # Inline math $...$
            r"\$(?!\s)([^$]+?)\$(?!\s)"

            r"|"

            # HTML tags <div ... > ou </div>
            r"</?(?:div|span|section|article|header|footer|details|summary|"
            r"table|tr|th|figure|iframe|img|u|i|sup|sub|br|h[0-6]|a"
            r")\b[^>]*>"

            r"|"

            # Inline code `...`
            r"`[^`]+`"

            r"|"

            # indentation `     `
            r"^\s+-\s"
            r"|"
            r"^\s+[0-9]\.\s"
            r"|"
            r"^\s+\*\s"
            r"|"
            r"^\s+[a-zA-Z]"
            r"|"

            # Images markdown ![alt](url)
            r"!\[[^\]]*\]\([^)]+\)"

            r"|"

            # Links [text](url)
            r"\[[^\]]+\]\([^)]+\)"

            r"|"

            # Pipes | (sauf si dans un TOKEN)
            r"(?<!HTML:TOKEN:[a-f0-9]{32}:END)\|"

            r"|"

            # Emojis textuels :sob:
            r":[a-z_]+?:"

            r")",
            flags=re.IGNORECASE | re.MULTILINE | re.DOTALL
        )

    # ============================================
    # ============================================
    def _make_token(self):
        return f"<HTML:TOKEN:{str(uuid.uuid4())}:END>"

    # ============================================
    # ============================================
    def protect(self, text: str):
        mapping = {}

        def repl_tokenize(match):
            raw = match.group(0)

            # Ne jamais tokeniser un token
            if raw.startswith("<HTML:TOKEN:"):
                return raw

            token = self._make_token()
            mapping[token] = raw
            return token

        protected = self.pattern.sub(repl_tokenize, text)

        return protected, mapping

    # ======================================================
    # RESTORE — on remplace les tokens dans l'ordre inverse
    # ======================================================
    def restore(self, text: str, mapping: dict) -> str:
        """
        Parcours le texte, détecte les tokens un par un et les remplace
        avec leur valeur originale dans mapping. Pas d'escape foireux.
        """
        restored = []
        last_index = 0

        for match in self.token_regex.finditer(text):
            start, end = match.span()
            token = match.group(0)

            # ajouter le texte avant le token
            restored.append(text[last_index:start])

            if token in mapping:
                restored.append(mapping[token])
            else:
                # debug possible si token manquant
                print(f"Warning: token {token} not found in mapping")
                restored.append(token)

            last_index = end

        # ajouter ce qui reste après le dernier token
        restored.append(text[last_index:])

        return "".join(restored)
