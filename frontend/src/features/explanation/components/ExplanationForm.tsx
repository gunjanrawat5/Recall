import { useEffect, useState } from 'react'
import { ApiError } from '../../../api/client'
import { AuthButton } from '../../auth/components/AuthButton'
import { useAuth } from '../../auth/useAuth'
import { createExplanation, getExplanations } from '../explanationApi'
import { toExplanationMode } from '../explanationTypes'
import type { ExplanationLevel, ExplanationResponse } from '../explanationTypes'
import { ExportDestinations } from './ExportDestinations'
import { ExplanationResult } from './ExplanationResult'
import { ModelSelector } from './ModelSelector'
import { SelectedTextPreview } from './SelectedTextPreview'

type ExplanationFormProps = {
  selectedText: string
}

export function ExplanationForm({ selectedText }: ExplanationFormProps) {
  const { user } = useAuth()
  const [level, setLevel] = useState<ExplanationLevel>('Beginner')
  const [history, setHistory] = useState<ExplanationResponse[]>([])
  const [activeExplanation, setActiveExplanation] = useState<ExplanationResponse | null>(null)
  const [loadedForUserId, setLoadedForUserId] = useState<string | null>(null)
  const [isSubmitting, setIsSubmitting] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    if (!user) return

    let isCurrent = true
    getExplanations()
      .then((items) => {
        if (!isCurrent) return
        setError('')
        setHistory(items)
        setActiveExplanation(items[0] ?? null)
      })
      .catch((requestError) => {
        if (isCurrent) setError(requestError instanceof ApiError ? requestError.message : 'Could not load explanations.')
      })
      .finally(() => {
        if (isCurrent) setLoadedForUserId(user.id)
      })

    return () => { isCurrent = false }
  }, [user])

  const submitExplanation = async () => {
    if (!user || !selectedText.trim()) return

    setIsSubmitting(true)
    setError('')
    try {
      const created = await createExplanation({
        selected_text: selectedText,
        surrounding_context: 'An article about learning, memory, and the spacing effect.',
        page_title: 'How memory becomes knowledge',
        page_url: window.location.href,
        mode: toExplanationMode(level),
      })
      setHistory((items) => [created, ...items.filter((item) => item.id !== created.id)])
      setActiveExplanation(created)
    } catch (requestError) {
      setError(requestError instanceof ApiError ? requestError.message : 'Could not create the explanation.')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <>
      <header className="panel-heading">
        <div>
          <span className="eyebrow">RECALL</span>
          <h2>Understand anything.</h2>
        </div>
        <AuthButton />
      </header>

      <SelectedTextPreview text={selectedText} />
      <ExportDestinations />

      <section className="panel-section level-section">
        <label htmlFor="level">Explanation level</label>
        <ModelSelector value={level} onChange={setLevel} />
        {error && <div className="explanation-error" role="alert">{error}</div>}
        {!user && <p className="login-required">Log in to generate and save explanations.</p>}
        <button className="explain-button" type="button" disabled={!user || isSubmitting} onClick={submitExplanation}>
          <span aria-hidden="true">✦</span> {isSubmitting ? 'Explaining…' : 'Explain & save'}
        </button>
      </section>

      {user && (
        <ExplanationResult
          explanation={activeExplanation}
          history={history}
          isLoading={loadedForUserId !== user.id}
          onSelect={setActiveExplanation}
        />
      )}
    </>
  )
}
