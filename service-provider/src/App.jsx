import { BrowserRouter } from 'react-router-dom'
import './App.css'
import ClientRoutes from './routes/ClientRoutes'

function App() {

  return (
    <BrowserRouter>
      <ClientRoutes />
    </BrowserRouter>
  )
}

export default App
