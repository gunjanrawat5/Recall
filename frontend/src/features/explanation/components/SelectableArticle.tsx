type SelectableArticleProps = {
  onTextSelected: (text: string) => void
}

export function SelectableArticle({ onTextSelected }: SelectableArticleProps) {
  const captureSelection = () => {
    const text = window.getSelection()?.toString().trim()
    if (text) onTextSelected(text)
  }

  return (
    <article className="webpage" onMouseUp={captureSelection}>
      <div className="article-label">LEARNING SCIENCE · 8 MIN READ</div>
      <h1>How memory becomes knowledge</h1>
      <p className="lead">
        Learning is not a single event. It is a process of returning to an idea,
        testing what remains, and rebuilding what has faded.
      </p>
      <div className="article-rule" />
      <h2>The spacing effect</h2>
      <p>
        When we encounter an idea repeatedly over time, the path back to it becomes
        stronger. The best time to review something is just before you forget it.
        This effortful moment of recall is what makes the memory more durable.
      </p>
      <blockquote>
        “We remember what we actively retrieve, not simply what we reread.”
      </blockquote>
      <p>
        Select any sentence in this article to see it appear in the Recall panel.
        You can then choose how much detail you want in the explanation.
      </p>
    </article>
  )
}
