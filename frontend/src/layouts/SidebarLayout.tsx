import type { ReactNode } from 'react'

type SidebarLayoutProps = {
  content: ReactNode
  sidebar: ReactNode
}

export function SidebarLayout({ content, sidebar }: SidebarLayoutProps) {
  return (
    <main className="workspace">
      {content}
      <aside className="recall-panel">{sidebar}</aside>
    </main>
  )
}
