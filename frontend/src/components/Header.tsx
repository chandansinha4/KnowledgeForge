function Header() {
  return (
    <header className="header">
      <div className="brand">
        <div className="brand-mark">K</div>

        <div>
          <h1>KnowledgeForge</h1>
          <p>AI-powered learning workspace</p>
        </div>
      </div>

      <div className="status">
        <span className="status-dot" />
        API Online
      </div>
    </header>
  )
}

export default Header