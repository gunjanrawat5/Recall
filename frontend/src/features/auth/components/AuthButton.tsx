import { useState } from 'react'
import { useAuth } from '../useAuth'
import { AuthModal } from './AuthModal'

export function AuthButton() {
  const { user, isLoading, logout } = useAuth()
  const [isOpen, setIsOpen] = useState(false)

  if (isLoading) return <span className="auth-loading">Checking…</span>

  if (user) {
    return (
      <div className="account-control">
        <span title={user.email}>{user.email.split('@')[0]}</span>
        <button type="button" onClick={logout}>Log out</button>
      </div>
    )
  }

  return (
    <>
      <button className="login-button" type="button" onClick={() => setIsOpen(true)}>Log in</button>
      {isOpen && <AuthModal onClose={() => setIsOpen(false)} />}
    </>
  )
}
