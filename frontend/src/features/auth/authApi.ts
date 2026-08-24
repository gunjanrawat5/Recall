import { apiClient } from '../../api/client'
import type { AuthUser, LoginCredentials, TokenResponse } from './authTypes'

export function login(credentials: LoginCredentials) {
  return apiClient<TokenResponse>('/auth/login', {
    method: 'POST',
    body: JSON.stringify(credentials),
  })
}

export function register(credentials: LoginCredentials) {
  return apiClient<AuthUser>('/users', {
    method: 'POST',
    body: JSON.stringify(credentials),
  })
}

export function getCurrentUser() {
  return apiClient<AuthUser>('/auth/me')
}
