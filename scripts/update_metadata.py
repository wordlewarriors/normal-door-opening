import sys, re, yaml, os
from pathlib import Path

HASHTAG_RE = re.compile(r"#(\w+)")


def parse_frontmatter(text: str):
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) > 2:
            _, fm, rest = parts[0], parts[1], parts[2]
            return yaml.safe_load(fm) or {}, rest.lstrip('\n')
    if text.startswith('----'):
        parts = text.split('----', 1)
        if len(parts) > 1:
            rest = parts[1]
            return {}, rest.lstrip('\n')
    return {}, text


def build_frontmatter(path: Path, data: dict, body: str):
    if 'title' not in data or not data['title']:
        data['title'] = path.stem
    if 'draft' not in data:
        data['draft'] = False
    tags_in_body = set(HASHTAG_RE.findall(body))
    existing_tags = set(data.get('tags', []) or [])
    all_tags = sorted(existing_tags | tags_in_body)
    data['tags'] = list(all_tags)
    fm_text = yaml.safe_dump(data, sort_keys=False).strip()
    return f"---\n{fm_text}\n---\n\n{body}".rstrip() + "\n"


def process_file(path: Path):
    text = path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(text)
    new_text = build_frontmatter(path, fm, body)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print(f"Updated {path}")


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else 'content')
    for md in root.rglob('*.md'):
        process_file(md)

if __name__ == '__main__':
    main()
