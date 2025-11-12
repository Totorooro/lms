import { useState, useEffect } from 'react';
import '../styles/Teachers.css';
import api from '../api';  // ← ИСПОЛЬЗУЕМ ЕДИНЫЙ api.js

const Teachers = () => {
  const [teachers, setTeachers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);  // ← ДОБАВЛЕНО: обработка ошибок

  useEffect(() => {
    const fetchTeachers = async () => {
      try {
        const response = await api.get('/api/teachers/teachers/');  // ← ЧЕРЕЗ api.js!
        
        if (!response.data) {
          throw new Error('Пустой ответ от сервера');
        }

        console.log('Преподаватели загружены:', response.data);
        setTeachers(response.data);
        setLoading(false);
      } catch (err) {
        console.error('Ошибка загрузки преподавателей:', err);
        setError(err.response?.data?.detail || err.message || 'Не удалось загрузить данные');
        setLoading(false);
      }
    };

    fetchTeachers();
  }, []);

  // === ЗАГРУЗКА ===
  if (loading) {
    return (
      <div className="teachers-page teachers-offset">
        <div className="loading">
          <div className="spinner"></div>
          <p>Загрузка преподавателей...</p>
        </div>
      </div>
    );
  }

  // === ОШИБКА ===
  if (error) {
    return (
      <div className="teachers-page teachers-offset">
        <div className="error">
          <p>Ошибка: {error}</p>
          <button onClick={() => window.location.reload()} className="retry-btn">
            Повторить
          </button>
        </div>
      </div>
    );
  }

  // === ОСНОВНОЙ КОНТЕНТ ===
  return (
    <div className="teachers-page teachers-offset">
      <header className="header">
        <h1>Преподаватели</h1>
        <p className="subtitle">Контакты преподавателей группы ИУ7-71Б</p>
      </header>

      <div className="teachers-grid">
        {teachers.length === 0 ? (
          <div className="no-data">
            <p>Преподаватели не добавлены</p>
          </div>
        ) : (
          teachers.map(teacher => (
            <div key={teacher.id} className="teacher-card">
              {/* АВАТАР */}
              <div className="avatar">
                {teacher.last_name?.[0] || '?'}
                {teacher.first_name?.[0] || '?'}
              </div>

              {/* ФИО */}
              <h3>
                {teacher.last_name || ''} {teacher.first_name || ''}{' '}
                {teacher.middle_name || ''}
              </h3>

              {/* ДОЛЖНОСТЬ */}
              <p className="position">{teacher.position || 'Преподаватель'}</p>

              {/* КАФЕДРА */}
              <p className="department">
                Кафедра {teacher.department_name || '—'}
              </p>

              {/* ПРЕДМЕТЫ */}
              <div className="subjects">
                <strong>Предметы:</strong>
                <div className="subject-tags">
                  {Array.isArray(teacher.subjects) && teacher.subjects.length > 0 ? (
                    teacher.subjects.map((s, i) => (
                      <span key={i} className="subject-tag">
                        {s.subject_name || 'Без названия'}
                      </span>
                    ))
                  ) : (
                    <span className="no-subjects">—</span>
                  )}
                </div>
              </div>

              {/* КОНТАКТЫ */}
              <div className="contacts">
                {teacher.email && (
                  <div className="contact-item">
                    <strong>Email:</strong>{' '}
                    <a href={`mailto:${teacher.email}`} className="contact-link">
                      {teacher.email}
                    </a>
                  </div>
                )}
                {teacher.phone && (
                  <div className="contact-item">
                    <strong>Телефон:</strong>{' '}
                    <a href={`tel:${teacher.phone}`} className="contact-link">
                      {teacher.phone}
                    </a>
                  </div>
                )}
                {teacher.office && (
                  <div className="contact-item">
                    <strong>Кабинет:</strong> {teacher.office}
                  </div>
                )}
                {teacher.consultation_schedule && (
                  <div className="contact-item">
                    <strong>Консультации:</strong> {teacher.consultation_schedule}
                  </div>
                )}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default Teachers;