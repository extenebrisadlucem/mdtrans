import re
import sys
import argparse
from pathlib import Path

from preprocessor import MarkdownProtector
from translator import LibreTranslator

# ======================================================
# translate_between_tokens
# ======================================================
def translate_between_tokens(protected: str, translator: LibreTranslator, source: str, target: str, api_key=None):
    token_regex = re.compile(r"<HTML:TOKEN:[a-f0-9]+-[a-f0-9]+-[a-f0-9]+-[a-f0-9]+-[a-f0-9]+:END>")
    result = []
    last_index = 0

    for match in token_regex.finditer(protected):
        start, end = match.span()
        segment = protected[last_index:start]

        # split par lignes pour ne pas casser le Markdown
        lines = segment.splitlines(keepends=True)
        for line in lines:
            if line.strip():
                translated = translator.translate_text(line, source=source, target=target, api_key=api_key)

                # enlever le point final si ajouté par LT
                if translated.endswith(".") and not line.strip().endswith("."):
                    translated = translated[:-1]   

                # enlever le point d'interrogation final si ajouté par LT
                if translated.endswith("?") and not line.strip().endswith("?"):
                    translated = translated[:-1]

                # enlever le point d'interrogation final si ajouté par LT
                if translated.endswith("\n?") or translated.endswith("\n."):
                    translated = translated[:-1]

                result.append(translated)
            else:
                result.append(line)

        # token intact
        result.append(match.group(0))
        last_index = end

    # dernier segment après le dernier token
    segment = protected[last_index:]
    lines = segment.splitlines(keepends=True)
    for line in lines:
        if line.strip():
            translated = translator.translate_text(line, source=source, target=target, api_key=api_key)
            if translated.endswith(".") and not line.strip().endswith("."):
                translated = translated[:-1]
            result.append(translated)
        else:
            result.append(line)

    return "".join(result)

# ======================================================
# main
# ======================================================
def main():
    parser = argparse.ArgumentParser(description="Safe Markdown Translator CLI")
    parser.add_argument("input", type=str, help="Input Markdown file")
    parser.add_argument("-o", "--output", type=str, help="Output translated file")
    parser.add_argument("--api", type=str, required=True, help="LibreTranslate API URL")
    parser.add_argument("--api-key", type=str, default=None, help="LibreTranslate API key")
    parser.add_argument("-s", "--source", default="auto", help="Source language")
    parser.add_argument("-t", "--target", default="fr", help="Target language")
    parser.add_argument("-n", "--noref", required=False , action='store_true', help="Don't show the reference at the end of the text")
    args = parser.parse_args()

    in_path = Path(args.input)
    if not in_path.exists():
        print(f"Fichier introuvable: {in_path}", file=sys.stderr)
        sys.exit(1)
    out_path = Path(args.output) if args.output else in_path.with_name(in_path.stem + "_translated.md")

    md = in_path.read_text(encoding="utf-8")
    protector = MarkdownProtector()
    protected, mapping = protector.protect(md)

    translator = LibreTranslator(api_url=args.api)

    #Traduction smart entre tokens
    translated = translate_between_tokens(protected, translator, source=args.source, 
                                            target=args.target, api_key=args.api_key)

    restored = protector.restore(translated, mapping)
    if args.noref is None: 
        restored = restored+"<br><br><br><sub>Translated by [mdtrans](https://github.com/extenebrisadlucem/mdtrans)/[LibreTranslate](https://github.com/LibreTranslate/LibreTranslate.git)</sub>"
    out_path.write_text(restored, encoding="utf-8")
    print(f"Fichier traduit généré : {out_path}")


# ======================================================
# MAIN
# ======================================================
if __name__ == "__main__":
    main()
