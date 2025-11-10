import React from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import api from '../api';
import { REFRESH_TOKEN } from '../constants';
import '../styles/Sidebar.css'; 

function Sidebar() {
  const navigate = useNavigate();  

  const handleLogout = async () => {
    const refresh = localStorage.getItem(REFRESH_TOKEN);
    if (refresh) {
      try {
        await api.post('/api/logout/', { refresh });  
      } catch (error) {
        console.error('Logout error:', error);  
      }
    }
    localStorage.clear();  
    navigate('/login');  
  };

  return (
    <div className="sidebar">
      <ul>
        <li>
          <NavLink 
            to="/home" 
            className={({ isActive }) => isActive ? 'active' : ''}
          >
            <img src="/images/icon-schedule.png" className="icon" alt="Расписание" /> Расписание
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/events" 
            className={({ isActive }) => isActive ? 'active' : ''}
          >
            <img src="/images/icon-events.png" className="icon" alt="Мероприятия" /> Мероприятия
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/teachers" 
            className={({ isActive }) => isActive ? 'active' : ''}
          >
            <img src="/images/icon-teachers.png" className="icon" alt="Преподаватели" /> Преподаватели
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/exams" 
            className={({ isActive }) => isActive ? 'active' : ''}
          >
            <img src="/images/icon-exams.png" className="icon" alt="Экзамены" /> Экзамены
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/tasks" 
            className={({ isActive }) => isActive ? 'active' : ''}
          >
            <img src="/images/icon-tasks.png" className="icon" alt="Домашние задания" /> Домашние задания
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/grades" 
            className={({ isActive }) => isActive ? 'active' : ''}
          >
            <img src="/images/icon-grades.png" className="icon" alt="Журнал оценок" /> Журнал оценок
          </NavLink>
        </li>
        <li>
          <NavLink 
            to="/notifications" 
            className={({ isActive }) => isActive ? 'active' : ''}
          >
            <img src="/images/icon-notification.png" className="icon" alt="Уведомления" /> Уведомления
          </NavLink>
        </li>
      </ul>
      <button onClick={handleLogout} className="logout-button">
        <img src="/images/icon-logout.png" className="logout-icon" alt="Выйти" /> Выйти
      </button>
    </div>
  );
}

export default Sidebar;