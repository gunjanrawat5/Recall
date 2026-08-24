export type AuthUser = {
  id: string
  email: string
  created_at: string
  updated_at: string
}

export type LoginCredentials = {
  email: string
  password: string
}

export type TokenResponse = {
  access_token: string
  token_type: string
}
