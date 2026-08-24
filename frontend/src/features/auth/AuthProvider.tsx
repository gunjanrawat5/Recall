import { useEffect, useState } from 'react'
import type { ReactNode } from 'react'
import { getAccessToken, setAccessToken } from '../../api/client'
import * as authApi from './authApi'
import { AuthContext } from './authContext'
import type { AuthUser, LoginCredentials } from './authTypes'

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null)
  const [isLoading, setIsLoading] = useState(Boolean(getAccessToken()))

  useEffect(() => {
    if (!getAccessToken()) return

    authApi.getCurrentUser()
      .then(setUser)
      .catch(() => setAccessToken(null))
      .finally(() => setIsLoading(false))
  }, [])

  const login = async (credentials: LoginCredentials) => {
    const token = await authApi.login(credentials)
    setAccessToken(token.access_token)
    try {
      setUser(await authApi.getCurrentUser())
    } catch (error) {
      setAccessToken(null)
      throw error
    }
  }

  const register = async (credentials: LoginCredentials) => {
    await authApi.register(credentials)
    await login(credentials)
  }

  const logout = () => {
    setAccessToken(null)
    setUser(null)
  }

  return (
    <AuthContext.Provider value={{ user, isLoading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
