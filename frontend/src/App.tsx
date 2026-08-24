import { useState } from 'react'
import { ExplanationForm } from './features/explanation/components/ExplanationForm'
import { SelectableArticle } from './features/explanation/components/SelectableArticle'
import { SidebarLayout } from './layouts/SidebarLayout'

const initialSelection =
  'The best time to review something is just before you forget it.'

function App() {
  const [selectedText, setSelectedText] = useState(initialSelection)

  return (
    <SidebarLayout
      content={<SelectableArticle onTextSelected={setSelectedText} />}
      sidebar={<ExplanationForm selectedText={selectedText} />}
    />
  )
}

export default App
