import { useState, useEffect } from 'react';
import '../styles/Teachers.css'; // Создай этот файл

const Teachers = () => {
  const [teachers, setTeachers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
  fetch('http://127.0.0.1:8000/api/teachers/teachers/', {  // ← ПОЛНЫЙ URL
    headers: {
      'Content-Type': 'application/json',
    }
  })
    .then(res => {
      if (!res.ok) throw new Error('Ошибка API');
      return res.json();
    })
    .then(data => {
      console.log('Данные преподавателей:', data);  // ← ДЛЯ ОТЛАДКИ
      setTeachers(data);
      setLoading(false);
    })
    .catch(error => {
      console.error('Ошибка:', error);  // ← ДЛЯ ОТЛАДКИ
      setLoading(false);
    });
}, []);

  if (loading) return <div className="loading">Загрузка преподавателей...</div>;

  return (
    <div className="teachers-page">
      <header className="header">
        <h1>Преподаватели</h1>
        <p className="subtitle">Контакты преподавателей группы ИУ7-71Б</p>
      </header>

      <div className="teachers-grid">
        {teachers.length === 0 ? (
          <p className="no-data">Преподаватели не добавлены</p>
        ) : (
          teachers.map(teacher => (
            <div key={teacher.id} className="teacher-card">
              <div className="avatar">
                {teacher.last_name[0]}{teacher.first_name[0]}
              </div>
              <h3>{teacher.last_name} {teacher.first_name} {teacher.middle_name || ''}</h3>
              <p className="position">{teacher.position || 'Преподаватель'}</p>
              <p className="department">Кафедра {teacher.department_name || '—'}</p>

              <div className="subjects">
                <strong>Предметы:</strong>
                <div className="subject-tags">
                  {teacher.subjects.length > 0 ? (
                    teacher.subjects.map((s, i) => (
                      <span key={i} className="subject-tag">
                        {s.subject_name}
                      </span>
                    ))
                  ) : (
                    <span className="no-subjects">—</span>
                  )}
                </div>
              </div>

              <div className="contacts">
                {teacher.email && (
                  <div className="contact-item">
                    <span>Email</span> {teacher.email}
                  </div>
                )}
                {teacher.phone && (
                  <div className="contact-item">
                    <span>Phone</span> {teacher.phone}
                  </div>
                )}
                {teacher.office && (
                  <div className="contact-item">
                    <span>Office</span> {teacher.office}
                  </div>
                )}
                {teacher.consultation_schedule && (
                  <div className="contact-item">
                    <span>Clock</span> Консультации: {teacher.consultation_schedule}
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