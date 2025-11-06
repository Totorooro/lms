import React, { useState, useEffect } from 'react';
import Sidebar from '../components/Sidebar';
import api from '../api';
import '../styles/Home.css';
function Home() {
  const [schedule, setSchedule] = useState({});
  const [weekStart, setWeekStart] = useState(getMonday(new Date()));
  const [group, setGroup] = useState('');
  const formatTime = (timeString) => {
    return timeString.split(':').slice(0, 2).join(':');
  };
  useEffect(() => {
    const week_start = weekStart.toISOString().split('T')[0];
    api.get('/api/schedule/lessons/', { params: { week_start } })
      .then(res => {
        setSchedule(res.data);
        const firstDay = Object.keys(res.data)[0];
        const firstLesson = res.data[firstDay]?.[0];
        if (firstLesson && firstLesson.group && firstLesson.group.name) {
          setGroup(firstLesson.group.name);
        }
      })
      .catch(err => console.error(err));
  }, [weekStart]);
  function getMonday(date) {
    const d = new Date(date);
    const day = d.getDay();
    const diff = d.getDate() - day + (day === 0 ? -6 : 1);
    return new Date(d.setDate(diff));
  }
  function getISOWeek(date) {
    let d = new Date(date);
    let dayNum = d.getUTCDay() || 7;
    d.setUTCDate(d.getUTCDate() + 4 - dayNum);
    let yearStart = new Date(Date.UTC(d.getUTCFullYear(), 0, 1));
    return Math.ceil((((d - yearStart) / 86400000) + 1) / 7);
  }
  const parity = getISOWeek(weekStart) % 2 === 1 ? 'Четная' : 'Нечетная';
  const getTypeText = (type) => {
    switch (type) {
      case 'seminar':
        return 'Семинар';
      case 'lecture':
        return 'Лекция';
      case 'lab':
        return 'Лаб. работа';
      case 'practice':
        return 'Практика';
      default:
        return type;
    }
  };
  function changeWeek(offset) {
    const newDate = new Date(weekStart);
    newDate.setDate(newDate.getDate() + offset * 7);
    setWeekStart(getMonday(newDate));
  }
  const endOfWeek = new Date(weekStart.getTime() + 6 * 24 * 60 * 60 * 1000);
  return (
    <div className="home-container">
      <Sidebar />
      <div className="main-content">
        <div className="header">
          <div className="title-group">
            <h1>Расписание занятий</h1>
            {group && <p className="group-name">Группа {group}</p>}
          </div>
          <div className="week-selector">
            <button onClick={() => changeWeek(-1)}><img src="/images/left_page.png" className="logo-topage" /></button>
            <div className="week-info">
              <span className="date-range">
                <span className='date-range-text'>Неделя от </span>{weekStart.toLocaleDateString('ru-RU', { day: '2-digit', month: '2-digit', year: '2-digit' })} -
                {endOfWeek.toLocaleDateString('ru-RU', { day: '2-digit', month: '2-digit', year: '2-digit' })}
              </span> 
              <span className={`type ${parity === 'Четная' ? 'Четная' : 'Нечетная'}`}>{parity} неделя</span>
            </div>
            <button onClick={() => changeWeek(1)}><img src="/images/right_page.png" className="logo-topage" /></button>
          </div>
        </div>
        <div className='today-container'>
          <span className="today-button" onClick={() => setWeekStart(getMonday(new Date()))}>Сегодня</span>
        </div>
        {Object.entries(schedule).map(([day, lessons]) => (
          <div key={day} className="day-block">
            <h2>{getDayName(day)} {getDateForDay(weekStart, day)}</h2>
            {lessons.map((lesson, index) => (
              <div key={index} className="lesson-block">
                <div className="time-type">
                  <span className="time-circle">
                    <img src="/images/logo-time.png" alt="Logo" className="logo-placeholder" />
                    {formatTime(lesson.start_time)}-{formatTime(lesson.end_time)}
                  </span>
                  <span className={`type ${lesson.type === 'lecture' ? 'lecture' : 'lab'}`}>
                    {getTypeText(lesson.type)}
                  </span>
                </div>
                <p className="subject">{lesson.subject.name}</p>
                <p className="teacher-room">
                  {lesson.teacher} <img src="/images/pin.png" className="room-icon" />
                  ауд. {lesson.classroom}
                </p>
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}
function getDayName(dayNum) {
  const days = ['', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'];
  return days[dayNum];
}
function getDateForDay(weekStart, dayNum) {
  const date = new Date(weekStart);
  date.setDate(date.getDate() + (dayNum - 1));
  return date.toLocaleDateString('ru-RU', { day: 'numeric', month: 'short' });
}
export default Home;
