interface YouTubeInputProps {
  url: string
  loading: boolean
  onUrlChange: (url: string) => void
  onSubmit: () => void
}

function YouTubeInput({
  url,
  loading,
  onUrlChange,
  onSubmit,
}: YouTubeInputProps) {
  return (
    <section className="hero-input">
      <div className="hero-copy">
        <span className="eyebrow">
          LEARNING ASSISTANT
        </span>

        <h2>
          Learn from videos,
          <br />
          not timestamps.
        </h2>

        <p>
          Paste a YouTube educational video and
          KnowledgeForge will transform it into
          structured knowledge and reflection.
        </p>
      </div>

      <div className="input-card">
        <label htmlFor="youtube-url">
          YouTube video URL
        </label>

        <div className="input-row">
          <input
            id="youtube-url"
            type="url"
            placeholder="https://www.youtube.com/watch?v=..."
            value={url}
            onChange={(event) =>
              onUrlChange(event.target.value)
            }
            disabled={loading}
          />

          <button
            type="button"
            onClick={onSubmit}
            disabled={loading || !url.trim()}
          >
            {loading
              ? "Generating..."
              : "Generate Knowledge"}
          </button>
        </div>

        <span className="input-hint">
          Knowledge extraction · Reflection · Markdown export
        </span>
      </div>
    </section>
  )
}

export default YouTubeInput