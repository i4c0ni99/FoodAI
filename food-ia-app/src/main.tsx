import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

import { Copertine } from './page/copertine.page'
import { ChatIA } from './page/chatAI.page'
import { RouterProvider, createBrowserRouter } from 'react-router-dom'
import { Calculator } from './page/calculator.page'
import { PrefererAliment } from './page/preferer-aliment.page'
const router = createBrowserRouter([
    {
        path: "*",
        element: <Copertine />
    },
    {
        path: "/chat",
        element: <ChatIA />
    },
    {
        path:"/calculator",
        element: <Calculator/>
    },
    {
        path:"/preferer-aliment",
        element: <PrefererAliment/>
    }

])
ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <main>
            <RouterProvider router={router}></RouterProvider>
        </main>
    </React.StrictMode>,
)
