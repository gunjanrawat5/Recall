import { apiClient } from '../../api/client'
import type { ExplanationRequest, ExplanationResponse } from './explanationTypes'

export function createExplanation(request: ExplanationRequest) {
  return apiClient<ExplanationResponse>('/explanations/', {
    method: 'POST',
    body: JSON.stringify(request),
  })
}

export function getExplanations() {
  return apiClient<ExplanationResponse[]>('/explanations')
}
