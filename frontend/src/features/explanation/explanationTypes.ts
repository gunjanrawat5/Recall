export const explanationLevels = ['Beginner', 'Concise', 'Detailed'] as const
export const exportDestinations = ['markdown', 'google-docs', 'notion'] as const

export type ExplanationLevel = (typeof explanationLevels)[number]
export type ExportDestination = (typeof exportDestinations)[number]
export type ExplanationMode = 'beginner' | 'concise' | 'detailed'

export type ExplanationRequest = {
  selected_text: string
  surrounding_context?: string
  page_title?: string
  page_url?: string
  mode: ExplanationMode
}

export function toExplanationMode(level: ExplanationLevel): ExplanationMode {
  return level.toLowerCase() as ExplanationMode
}

export type ExplanationResponse = ExplanationRequest & {
  id: string
  summary: string
  explanation: string
  key_points: string[]
  example?: string
  analogy?: string
  created_at: string
}
