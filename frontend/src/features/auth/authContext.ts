import { createContext } from 'react'
import type { AuthUser, LoginCredentials } from './authTypes'

export type AuthContextValue = {
  user: AuthUser | null
  isLoading: boolean
  login: (credentials: LoginCredentials) => Promise<void>
  register: (credentials: LoginCredentials) => Promise<void>
  logout: () => void
}

export const AuthContext = createContext<AuthContextValue | null>(null)
