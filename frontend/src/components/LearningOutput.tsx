import DocumentViewer from "./DocumentViewer"
import type { YouTubeResponse } from "../types/youtube"

interface LearningOutputProps {
  result: YouTubeResponse
}

function LearningOutput({
  result,
}: LearningOutputProps) {
  return (
    <section className="learning-output">
      <div className="video-meta">
        <div>
          <span className="eyebrow">GENERATED DOCUMENT</span>

          <h2>{result.title}</h2>

          <span className="video-id">
            YouTube · {result.video_id}
          </span>
        </div>

        <a
          className="source-link"
          href={result.source_url}
          target="_blank"
          rel="noreferrer"
        >
          Open video ↗
        </a>
      </div>

      <div className="documents">
        <DocumentViewer
          title="Knowledge"
          content={result.knowledge}
        />

        <DocumentViewer
          title="Reflection"
          content={result.reflection}
        />
      </div>
    </section>
  )
}

export default LearningOutput