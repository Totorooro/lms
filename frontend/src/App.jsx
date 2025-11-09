import React from "react"
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import Login from "./pages/Login"
import Home from "./pages/Home"
import NotFound from "./pages/NotFound"
// import ProtectedRoute from "./components/ProtectedRoute"  // ← ЗАКОММЕНТИРУЙ

import Events from "./pages/Events";
import Teachers from "./pages/Teachers";
import Exams from "./pages/Exams";
import Tasks from "./pages/Tasks";
import Grades from "./pages/Grades";
import Notifications from "./pages/Notifications";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/home" />} />
        <Route path="/home" element={<Home />} />  {/* УБРАЛ ProtectedRoute */}
        <Route path="/events" element={<Events />} />
        <Route path="/teachers" element={<Teachers />} />
        <Route path="/exams" element={<Exams />} />
        <Route path="/tasks" element={<Tasks />} />
        <Route path="/grades" element={<Grades />} />
        <Route path="/notifications" element={<Notifications />} />
        <Route path="/login" element={<Login />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App