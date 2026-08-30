from __future__ import annotations

from pathlib import Path

from app.domain.knowledge import KnowledgeDocument
from app.domain.reflection import ReflectionDocument


class MarkdownExporter:
    """
    Service responsible for exporting learning documents as Markdown files.
    """

    def __init__(self, output_directory: str | Path) -> None:
        self._output_directory = Path(output_directory)

    def export_knowledge(
        self,
        document: KnowledgeDocument,
    ) -> Path:
        """
        Export a KnowledgeDocument to a Markdown file.
        """

        return self._export(
            filename=self._sanitize_filename(document.title),
            content=self._build_frontmatter(
                title=document.title,
                document_type="knowledge",
                content=document.markdown,
            ),
        )

    def export_reflection(
        self,
        document: ReflectionDocument,
    ) -> Path:
        """
        Export a ReflectionDocument to a Markdown file.
        """

        filename = (
            self._sanitize_filename(document.title)
            + " - Reflection"
        )

        return self._export(
            filename=filename,
            content=self._build_frontmatter(
                title=document.title,
                document_type="reflection",
                content=document.markdown,
            ),
        )

    def _export(
        self,
        filename: str,
        content: str,
    ) -> Path:
        """
        Write Markdown content to the output directory.
        """

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = self._output_directory / f"{filename}.md"

        path.write_text(
            content,
            encoding="utf-8",
        )

        return path

    @staticmethod
    def _build_frontmatter(
        title: str,
        document_type: str,
        content: str,
    ) -> str:
        """
        Add YAML frontmatter to a Markdown document.
        """

        return (
            "---\n"
            f"title: {title}\n"
            f"type: {document_type}\n"
            "source: youtube\n"
            "---\n\n"
            f"{content.strip()}\n"
        )

    @staticmethod
    def _sanitize_filename(
        filename: str,
    ) -> str:
        """
        Remove characters that are invalid in filenames.
        """

        invalid_characters = '<>:"/\\|?*'

        return "".join(
            character
            for character in filename
            if character not in invalid_characters
        ).strip()