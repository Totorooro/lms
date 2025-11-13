import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import api from '../api';
import '../styles/Teachers.css';

function Teachers() {
  const [teachers, setTeachers] = useState([]);
  const [group, setGroup] = useState('');

  useEffect(() => {
    // Получаем группу пользователя
    api.get('/api/user/group')
      .then(res => setGroup(res.data.name || res.data))
      .catch(err => console.error(err));

    // Получаем преподавателей
    api.get('/api/teachers/teachers/')
      .then(res => setTeachers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="teachers-container">
      <Sidebar />
      <div className="main-content">
        <div className="header">
          <h1>Преподаватели</h1>
          <p>Контакты преподавателей группы {group}</p>
        </div>
        <div className="teachers-grid">
          {teachers.length === 0 ? (
            <p>Преподаватели не найдены.</p>
          ) : (
            teachers.map((teacher) => (
              <div key={teacher.id} className="teacher-card">
                <div className="avatar">
                  <div className="avatar-initials">
                    {teacher.full_name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2)}
                  </div>
                </div>
                <div className="info">
                  <h3>{teacher.full_name}</h3>
                  <p className="position">{teacher.position || 'Должность не указана'}</p>
                  <p className="department">{teacher.department || 'Кафедра не указана'}</p>

                  {teacher.subjects && teacher.subjects.length > 0 && (
                    <div className="subjects">
                      <strong>Предметы:</strong>
                      <div className="subject-tags">
                        {teacher.subjects.map((subj, i) => (
                          <span key={i} className="subject-tag">{subj}</span>
                        ))}
                      </div>
                    </div>
                  )}

                  <div className="contact">
                    {teacher.email && (
                      <p>
                        <span className="icon">Email</span> {teacher.email}
                      </p>
                    )}
                    {teacher.phone && (
                      <p>
                        <span className="icon">Phone</span> {teacher.phone}
                      </p>
                    )}
                    {teacher.office && (
                      <p>
                        <span className="icon">Office</span> каб. {teacher.office}
                      </p>
                    )}
                    {teacher.consultation_hours && (
                      <p>
                        <span className="icon">Clock</span> Консультации: {teacher.consultation_hours}
                      </p>
                    )}
                  </div>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default Teachers;