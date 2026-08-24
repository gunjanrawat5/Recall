import type { ExportDestination } from '../explanationTypes'

const options: Array<{ value: ExportDestination; label: string; hint: string }> = [
  { value: 'markdown', label: 'Markdown file', hint: '.md' },
  { value: 'google-docs', label: 'Google Doc', hint: 'Docs' },
  { value: 'notion', label: 'Notion', hint: 'Page' },
]

export function ExportDestinations() {
  return (
    <section className="panel-section export-section">
      <label>Save to</label>
      <div className="checkbox-list">
        {options.map(({ value, label, hint }) => (
          <label className="checkbox-option" key={value}>
            <input type="checkbox" name="destination" value={value} />
            <span className="custom-checkbox" aria-hidden="true" />
            <span>{label}</span>
            <small>{hint}</small>
          </label>
        ))}
      </div>
    </section>
  )
}
