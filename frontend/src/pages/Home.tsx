import { useState } from "react"

import Header from "../components/Header"
import YouTubeInput from "../components/YouTubeInput"
import LearningOutput from "../components/LearningOutput"
import { processYouTubeVideo } from "../services/youtube"
import type { YouTubeResponse } from "../types/youtube"

function Home() {
  const [url, setUrl] = useState("")
  const [result, setResult] =
    useState<YouTubeResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  async function handleSubmit() {
    if (!url.trim()) {
      return
    }

    setLoading(true)
    setError("")
    setResult(null)

    try {
      const data = await processYouTubeVideo(url)

      setResult(data)
    } catch (error) {
      setError(
        error instanceof Error
          ? error.message
          : "Something went wrong.",
      )
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <Header />

      <main>
        <YouTubeInput
          url={url}
          loading={loading}
          onUrlChange={setUrl}
          onSubmit={handleSubmit}
        />

        {error && (
          <div className="error">
            {error}
          </div>
        )}

        {result && <LearningOutput result={result} />}
      </main>
    </div>
  )
}

export default Home