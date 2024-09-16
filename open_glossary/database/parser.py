import os

import markdown
import yaml
from flask_sqlalchemy import SQLAlchemy
from loguru import logger
from markdown.extensions.wikilinks import WikiLinkExtension

from open_glossary.database.entry import GlossaryEntry


class MDToDBParser:
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def md_to_db(self, path) -> GlossaryEntry:
        meta, html = self.parse_file(path)
        entry = GlossaryEntry(title=meta['title'], description=html)
        logger.debug(f"Entry(title={entry.title}, description={entry.description[0:10]})")
        self.db.session.add(entry)
        self.db.session.commit()
        return entry

    @staticmethod
    def parse_file(path: str) -> (dict[str, object], str):
        logger.info(f"Parsing file at {path}")
        md = markdown.Markdown(extensions=[WikiLinkExtension(base_url='/details/', end_url='')])
        all_lines = None
        meta_lines = []
        content_lines = []
        with open(path, 'r', encoding='utf-8') as f:
            all_lines = f.readlines()
        meta_started = False
        for idx, line in enumerate(all_lines):
            if idx == 0 and line.rstrip() == '---':
                meta_started = True
                meta_lines.append(line)
            elif meta_started and line.rstrip() == '---':
                meta_started = False
            elif meta_started:
                meta_lines.append(line)
            else:
                content_lines.append(line)

        meta_content = yaml.safe_load(
            '\n'.join(meta_lines)
        )
        html = md.convert(
            '\n'.join(content_lines)
        )
        return meta_content, html

    def parse_from_directory(self, path: str) -> [GlossaryEntry]:
        entries = []
        if not os.path.isdir(path):
            raise NotADirectoryError(path)

        for f in os.listdir(path):
            full_path = os.path.join(path, f)
            if os.path.isfile(full_path) and f.endswith('.md'):
                entries.append(
                    self.md_to_db(full_path)
                )

        return entries
