import React from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Sidebar from "./components/Sidebar"
import Login from "./pages/Login"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"

import Events from "./pages/Events"
import Teachers from "./pages/Teachers"
import Exams from "./pages/Exams"
import Tasks from "./pages/Tasks"
import Grades from "./pages/Grades"
import Notifications from "./pages/Notifications"

function App() {
  return (
    <BrowserRouter>
      <div className="app-container">
        {/* БОКОВАЯ ПАНЕЛЬ — ВСЕГДА ВИДНА */}
        <Sidebar />

        {/* ОСНОВНОЙ КОНТЕНТ */}
        <div className="main-content">
          <Routes>
            <Route path="/" element={<Navigate to="/home" />} />
            <Route path="/home" element={<Home />} />
            <Route path="/events" element={<Events />} />
            <Route  path="/teachers" element={  <div className="teachers-offset">    <Teachers /> </div> } />
            <Route path="/exams" element={<Exams />} />
            <Route path="/tasks" element={<Tasks />} />
            <Route path="/grades" element={<Grades />} />
            <Route path="/notifications" element={<Notifications />} />
            <Route path="/login" element={<Login />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  )
}

export default App