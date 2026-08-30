from pathlib import Path

from app.domain.knowledge import KnowledgeDocument
from app.domain.reflection import ReflectionDocument
from app.exporters.markdown import MarkdownExporter


output_directory = Path("tmp/markdown")

exporter = MarkdownExporter(
    output_directory=output_directory,
)

knowledge = KnowledgeDocument(
    title="Test Knowledge",
    markdown="# Test Knowledge\n\nThis is a test.",
)

reflection = ReflectionDocument(
    title="Test Knowledge",
    markdown="# Reflection\n\nThis is a test reflection.",
)

knowledge_path = exporter.export_knowledge(
    knowledge
)

reflection_path = exporter.export_reflection(
    reflection
)

print("Knowledge:", knowledge_path)
print("Reflection:", reflection_path)