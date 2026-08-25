import type { ExplanationResponse } from '../explanationTypes'

type ExplanationResultProps = {
  explanation: ExplanationResponse | null
  history: ExplanationResponse[]
  isLoading: boolean
  onSelect: (explanation: ExplanationResponse) => void
}

export function ExplanationResult({ explanation, history, isLoading, onSelect }: ExplanationResultProps) {
  if (isLoading) {
    return <section className="panel-section result-section"><p className="result-empty">Loading your explanations…</p></section>
  }

  if (!explanation) return null

  return (
    <section className="panel-section result-section" aria-live="polite">
      <div className="result-heading">
        <label>Explanation</label>
        <span>{explanation.mode}</span>
      </div>
      <h3>{explanation.summary}</h3>
      <p className="result-copy">{explanation.explanation}</p>

      {explanation.key_points.length > 0 && (
        <ul className="key-points">
          {explanation.key_points.map((point) => <li key={point}>{point}</li>)}
        </ul>
      )}

      {explanation.example && (
        <div className="result-detail"><strong>Example</strong><p>{explanation.example}</p></div>
      )}
      {explanation.analogy && (
        <div className="result-detail"><strong>Analogy</strong><p>{explanation.analogy}</p></div>
      )}

      {history.length > 1 && (
        <div className="history-list">
          <span>Recent</span>
          {history.slice(0, 4).map((item) => (
            <button
              className={item.id === explanation.id ? 'active' : ''}
              type="button"
              key={item.id}
              onClick={() => onSelect(item)}
            >
              {item.selected_text}
            </button>
          ))}
        </div>
      )}
    </section>
  )
}
