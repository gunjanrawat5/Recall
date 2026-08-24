import { useState } from 'react'
import type { ExplanationLevel } from '../explanationTypes'
import { ExportDestinations } from './ExportDestinations'
import { ModelSelector } from './ModelSelector'
import { SelectedTextPreview } from './SelectedTextPreview'

type ExplanationFormProps = {
  selectedText: string
}

export function ExplanationForm({ selectedText }: ExplanationFormProps) {
  const [level, setLevel] = useState<ExplanationLevel>('Beginner')

  return (
    <>
      <header className="panel-heading">
        <div>
          <span className="eyebrow">RECALL</span>
          <h2>Understand anything.</h2>
        </div>
        <span className="spark" aria-hidden="true">✦</span>
      </header>

      <SelectedTextPreview text={selectedText} />
      <ExportDestinations />

      <section className="panel-section level-section">
        <label htmlFor="level">Explanation level</label>
        <ModelSelector value={level} onChange={setLevel} />
        <button className="explain-button" type="button">
          <span aria-hidden="true">✦</span> Save selection
        </button>
      </section>
    </>
  )
}
