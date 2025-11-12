// src/pages/Events.jsx
import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import api from '../api';
import '../styles/Events.css';

function Events() {
  const [events, setEvents] = useState([]);

  const fetchEvents = () => {
    api.get('/api/events/events/')
      .then(res => setEvents(res.data))
      .catch(err => console.error(err));
  };

  useEffect(() => {
    fetchEvents();
  }, []);

  const handleRegister = (eventId) => {
    api.post(`/api/event/events/${eventId}/register/`)
      .then(() => {
        fetchEvents();  
      })
      .catch(err => {
        console.error(err);
        alert(err.response?.data?.detail || 'Ошибка регистрации');
      });
  };

  const formatDate = (date) => {
    return new Date(date).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' });
  };

  const formatTime = (time) => {
    if (!time) return '';
    const [hours, minutes] = time.split(':');
    return `${hours}:${minutes}`;
  };

  const getStatusText = (status) => {
    switch (status) {
      case 'upcoming':
        return 'Предстоящее';
      case 'ongoing':
        return 'Сейчас';
      case 'completed':
        return 'Прошедшее';
      default:
        return status;
    }
  };

  const getTypeText = (type) => {
    switch (type) {
      case 'sport':
        return 'Спорт';
      case 'competition':
        return 'Соревнование';
      case 'conference':
        return 'Конференция';
      case 'courses':
        return 'Курсы';
      case 'seminar':
        return 'Семинар';
      case 'cultural':
        return 'Культурное';
      default:
        return type;
    }
  };

  return (
    <div className="events-container">
      <Sidebar />
      <div className="main-content">
        <div className="header">
          <h1>Мероприятия и активности</h1>
        </div>
        {events.map((event) => (
          <div key={event.id} className="event-block">
            <div className="event-header">
              <h2>{event.title}</h2>
              <span className={`status ${event.status}`}>{getStatusText(event.status)}</span>
              <span className={`type ${event.type_status}`}>{getTypeText(event.type_status)}</span>
            </div>
            <p className="description">{event.description}</p>
            <div className="details">
              <p>
                <img src="/images/logo-time.png" alt="Date" className="icon" />
                {formatDate(event.start_date)} {event.start_time ? `в ${formatTime(event.start_time)}` : ''}
                {event.end_date && ` - ${formatDate(event.end_date)} ${event.end_time ? `до ${formatTime(event.end_time)}` : ''}`}
              </p>
              <p>
                <img src="/images/pin.png" alt="Location" className="icon" />
                {event.location || 'Не указано'}
              </p>
              <p>
                <img src="/images/icon-teachers.png" alt="Organizer" className="icon" />
                Организатор: {event.organizer || 'Не указано'}
              </p>
              {event.progress && (
                <div className="progress">
                  <span>{event.progress} участников</span>
                  <div className="progress-bar">
                    <div
                      className="progress-fill"
                      style={{ width: `${(event.current_participants / event.participants_limit) * 100}%` }}
                    ></div>
                  </div>
                </div>
              )}
              {event.participants_limit === 0 || event.current_participants >= event.participants_limit ? (
                <p className="no-registration">{event.participants_limit === 0 ? '' : 'Места закончились'}</p>
              ) : event.is_registered ? (
                <p className="registered">Вы зарегистрированы</p>
              ) : (
                <button className="register-button" onClick={() => handleRegister(event.id)}>Записаться</button>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Events;