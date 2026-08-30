from __future__ import annotations

from pathlib import Path

from app.domain.knowledge import KnowledgeDocument
from app.domain.reflection import ReflectionDocument
from app.domain.transcript import TranscriptDocument

class MarkdownExporter:
    """
    Service responsible for exporting learning documents as Markdown files.
    """

    def __init__(self, output_directory: str | Path) -> None:
        self._output_directory = Path(output_directory)

    def export_knowledge(
        self,
        document: KnowledgeDocument,
        source: TranscriptDocument,
    ) -> Path:
        """
        Export a KnowledgeDocument to a Markdown file.
        """

        return self._export(
            directory="Knowledge",
            filename=self._sanitize_filename(document.title),
            content=self._build_frontmatter(
                title=document.title,
                document_type="knowledge",
                content=document.markdown,
                source=source,
            ),
        )

    def export_reflection(
        self,
        document: ReflectionDocument,
        source: TranscriptDocument,
    ) -> Path:
        """
        Export a ReflectionDocument to a Markdown file.
        """

        return self._export(
            directory="Reflections",
            filename=(
                self._sanitize_filename(document.title)
                + " - Reflection"
            ),
            content=self._build_frontmatter(
                title=document.title,
                document_type="reflection",
                content=document.markdown,
                source=source,
            ),
        )

    def _export(
        self,
        directory: str,
        filename: str,
        content: str,
    ) -> Path:
        """
        Write Markdown content to the specified output directory.
        """

        output_directory = self._output_directory / directory

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        path = output_directory / f"{filename}.md"

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
        source: TranscriptDocument,
    ) -> str:
        """
        Add YAML frontmatter to a Markdown document.
        """

        return (
            "---\n"
            f"title: {title}\n"
            f"type: {document_type}\n"
            "source: youtube\n"
            f"source_url: {source.source_url}\n"
            f"video_id: {source.video_id}\n"
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