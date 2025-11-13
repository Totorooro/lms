import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import api from '../api';
import '../styles/Grades.css';

function Grades() {
  const [summary, setSummary] = useState({
    overall_performance: 0,
    total_grades: 0,
    subjects_count: 0,
    subjects: []
  });

  useEffect(() => {
    api.get('/api/journal/summary/')
      .then((res) => setSummary(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="grades-container">
      <Sidebar />
      <div className="main-content">
        <div className="header">
          <h1>Электронный журнал</h1>
          <p>Ваши оценки и успеваемость</p>
        </div>
        <div className="overall-stats">
          <h2>Общая успеваемость</h2>
          <p>{summary.overall_performance.toFixed(1)}%</p>
          <p>{summary.total_grades} Всего оценок</p>
          <p>{summary.subjects_count} Предметов</p>
        </div>
        <div className="subjects-performance">
          <h2>Успеваемость по предметам</h2>
          {summary.subjects.map((subj, index) => (
            <div key={index} className="subject-block">
              <h3>{subj.name}</h3>
              <p>Последняя: {subj.avg_grade.toFixed(1)} ({subj.grade_count} оценок)</p>
              <div className="progress-bar">
                <div
                  className="fill"
                  style={{ width: `${subj.avg_grade}%` }}
                ></div>
              </div>
              <p className={subj.change >= 0 ? 'positive' : 'negative'}>
                {subj.change.toFixed(1)}% ({subj.grade_count} оценок)
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default Grades;
