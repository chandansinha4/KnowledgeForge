import ReactMarkdown from "react-markdown"

interface DocumentViewerProps {
  title: string
  content: string
}

function DocumentViewer({
  title,
  content,
}: DocumentViewerProps) {
  return (
    <article className="document">
      <div className="document-header">
        <h3>{title}</h3>
      </div>

      <div className="document-content">
        <ReactMarkdown>
          {content}
        </ReactMarkdown>
      </div>
    </article>
  )
}

export default DocumentViewer