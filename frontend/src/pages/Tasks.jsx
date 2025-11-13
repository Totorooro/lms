import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import api from '../api';
import '../styles/Tasks.css';

function Tasks() {
  const [homeworks, setHomeworks] = useState([]);
  const [group, setGroup] = useState('');

  useEffect(() => {
    api.get('/api/user/group')
      .then(res => setGroup(res.data.name || res.data))
      .catch(err => console.error(err));

    api.get('/api/homework/homeworks/')
      .then(res => setHomeworks(res.data))
      .catch(err => console.error(err));
  }, []);

  const formatDate = (date) => {
    return new Date(date).toLocaleDateString('ru-RU', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
    });
  };

  const formatTime = (time) => {
    if (!time) return '';
    const [hours, minutes] = time.split(':');
    return `${hours}:${minutes}`;
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'pending':
        return 'Ожидает выполнения';
      case 'urgent':
        return 'Срочно!';
      case 'overdue':
        return 'Просрочено';
      default:
        return status;
    }
  };

  return (
    <div className="tasks-container">
      <Sidebar />
      <div className="main-content">
        <div className="header">
          <h1>Домашние задания</h1>
          {group && <p className="group-name">Текущие задания для группы {group}</p>}
        </div>
        {homeworks.map((hw) => (
          <div key={hw.id} className="hw-block">
            <div className="hw-header">
              <span className={`status ${hw.status}`}>{getStatusText(hw.status)}</span>
              <h2>{hw.title}</h2>
            </div>
            <p className="subject">{hw.subject.name}</p>
            <p className="description">{hw.description}</p>
            <p className="due-date">
              Выдано: {formatDate(hw.due_date)} {hw.due_time ? ` до ${formatTime(hw.due_time)}` : ''}
            </p>
            <p className="assigned-by">
              Преподаватель: {hw.assigned_by ? hw.assigned_by.username : 'Не указано'}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Tasks;
