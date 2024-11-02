import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import DocumentProc from './components/DocumentProc'

function App() {
  const [count, setCount] = useState(0)

  return (
    <DocumentProc />
  )
}

export default App
