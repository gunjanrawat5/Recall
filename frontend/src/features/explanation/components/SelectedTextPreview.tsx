type SelectedTextPreviewProps = {
  text: string
}

export function SelectedTextPreview({ text }: SelectedTextPreviewProps) {
  return (
    <section className="panel-section">
      <label>Selected text</label>
      <div className="selection-card">“{text}”</div>
    </section>
  )
}
