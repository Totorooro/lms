import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import api from '../api';
import '../styles/Exams.css';

function Exams() {
  const [exams, setExams] = useState([]);
  const [hasUndefinedDates, setHasUndefinedDates] = useState(false);

  useEffect(() => {
    api.get('/api/exams/exams/')
      .then(res => {
        setExams(res.data);
        setHasUndefinedDates(res.data.some(e => !e.date));
      })
      .catch(err => console.error(err));
  }, []);

  const formatDate = (date) => {
    return new Date(date).toLocaleDateString('ru-RU', { day: 'numeric', month: 'long', year: 'numeric' });
  };

  const formatTime = (time) => {
    const [hours, minutes] = time.split(':');
    return `${hours}:${minutes}`;
  };

  const getExamTypeText = (type) => {
    switch (type) {
      case 'credit': return 'Зачет';
      case 'diff_credit': return 'Диф. зачет';
      case 'exam': return 'Экзамен';
      default: return type;
    }
  };

  const getDaysText = (days) => {
    if (days === 0) return 'Сегодня';
    if (days === 1) return 'Завтра';
    return `Через ${days} дн.`;
  };

  return (
    <div className="exams-container">
      <Sidebar />
      <div className="main-content">
        <div className="header">
          <h1>Экзамены и зачеты</h1>
          <p>Расписание экзаменационной сессии для всех групп</p>
        </div>

        {hasUndefinedDates && (
          <div className="warning-banner">
            Даты экзаменов по некоторым предметам не определены. Загляните в другое время.
          </div>
        )}

        <div className="section-title">Запланированные экзамены</div>

        <div className="exams-list">
          {exams.length === 0 ? (
            <p>Экзамены не запланированы.</p>
          ) : (
            exams.map((exam) => (
              <div key={exam.id} className="exam-card">
                <div className="exam-header">
                  <div className="subject-type">
                    <span className="icon"></span>
                    <h3>{exam.subject_name}</h3>
                    <span className={`type-badge ${exam.exam_type}`}>
                      {getExamTypeText(exam.exam_type)}
                    </span>
                  </div>
                  <div className="days-until">
                    {getDaysText(exam.days_until)}
                  </div>
                </div>

                <p className="teacher">Преподаватель: {exam.teacher}</p>
                <p className="group">Группа: {exam.group_name}</p>

                <div className="details">
                  <p>
                    <span className="icon"></span> {formatDate(exam.date)}
                  </p>
                  <p>
                    <span className="icon"></span> {formatTime(exam.time)}
                  </p>
                  <p>
                    <span className="icon"></span> {exam.location}
                  </p>
                </div>

                {exam.description && (
                  <div className="description">
                    {exam.description}
                  </div>
                )}
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default Exams;