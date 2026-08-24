import { useEffect, useState } from 'react'
import { ApiError } from '../../../api/client'
import { useAuth } from '../useAuth'

type AuthModalProps = {
  onClose: () => void
}

export function AuthModal({ onClose }: AuthModalProps) {
  const { login, register } = useAuth()
  const [mode, setMode] = useState<'login' | 'register'>('login')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [isSubmitting, setIsSubmitting] = useState(false)

  useEffect(() => {
    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === 'Escape') onClose()
    }
    window.addEventListener('keydown', closeOnEscape)
    return () => window.removeEventListener('keydown', closeOnEscape)
  }, [onClose])

  const submit = async (event: React.FormEvent) => {
    event.preventDefault()
    setError('')
    setIsSubmitting(true)
    try {
      const credentials = { email, password }
      if (mode === 'login') await login(credentials)
      else await register(credentials)
      onClose()
    } catch (requestError) {
      setError(requestError instanceof ApiError ? requestError.message : 'Unable to connect to Recall.')
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="auth-overlay" role="presentation" onMouseDown={(event) => {
      if (event.target === event.currentTarget) onClose()
    }}>
      <section className="auth-dialog" role="dialog" aria-modal="true" aria-labelledby="auth-title">
        <button className="auth-close" type="button" onClick={onClose} aria-label="Close">×</button>
        <span className="eyebrow">RECALL</span>
        <h2 id="auth-title">{mode === 'login' ? 'Welcome back.' : 'Create your account.'}</h2>
        <p>{mode === 'login' ? 'Log in to save and revisit explanations.' : 'Start building your learning history.'}</p>

        <form onSubmit={submit}>
          <label htmlFor="auth-email">Email</label>
          <input id="auth-email" type="email" autoComplete="email" value={email} onChange={(event) => setEmail(event.target.value)} required autoFocus />
          <label htmlFor="auth-password">Password</label>
          <input id="auth-password" type="password" autoComplete={mode === 'login' ? 'current-password' : 'new-password'} minLength={8} value={password} onChange={(event) => setPassword(event.target.value)} required />
          {error && <div className="auth-error" role="alert">{error}</div>}
          <button className="auth-submit" disabled={isSubmitting}>
            {isSubmitting ? 'Please wait…' : mode === 'login' ? 'Log in' : 'Create account'}
          </button>
        </form>

        <button className="auth-switch" type="button" onClick={() => {
          setMode(mode === 'login' ? 'register' : 'login')
          setError('')
        }}>
          {mode === 'login' ? 'New to Recall? Create an account' : 'Already have an account? Log in'}
        </button>
      </section>
    </div>
  )
}
