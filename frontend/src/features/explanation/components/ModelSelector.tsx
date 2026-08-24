import { explanationLevels } from '../explanationTypes'
import type { ExplanationLevel } from '../explanationTypes'

type ModelSelectorProps = {
  value: ExplanationLevel
  onChange: (level: ExplanationLevel) => void
}

export function ModelSelector({ value, onChange }: ModelSelectorProps) {
  return (
    <div className="select-wrap">
      <select
        id="level"
        value={value}
        onChange={(event) => onChange(event.target.value as ExplanationLevel)}
      >
        {explanationLevels.map((level) => <option key={level}>{level}</option>)}
      </select>
    </div>
  )
}
