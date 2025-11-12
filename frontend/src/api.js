// src/api.js
import axios from "axios";
import { ACCESS_TOKEN } from "./constants";

// === БАЗОВЫЙ URL ===
const getBaseURL = () => {
  const envUrl = import.meta.env.VITE_API_URL;
  
  // Если в .env — используем его
  if (envUrl) return envUrl;

  // Если в dev — localhost:8000
  if (import.meta.env.DEV) {
    return "http://127.0.0.1:8000/api";
  }

  // В продакшене — тот же домен (через прокси или CORS)
  return "/api";
};

const api = axios.create({
  baseURL: getBaseURL(),
  headers: {
    "Content-Type": "application/json",
  },
});

// === ИНТЕРЦЕПТОР ТОКЕНА ===
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem(ACCESS_TOKEN);

    // Добавляем токен ТОЛЬКО если он есть и это НЕ публичный маршрут
    const publicRoutes = [
      '/auth/token/',
      '/auth/token/refresh/',
      '/auth/logout/',
      '/teachers/teachers/',     // ← ПУБЛИЧНЫЙ!
      '/schedule/lessons/',      // ← ПУБЛИЧНЫЙ!
      '/events/events/',         // ← ПУБЛИЧНЫЙ!
    ];

    const isPublic = publicRoutes.some(route => 
      config.url?.includes(route)
    );

    if (token && !isPublic) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },
  (error) => Promise.reject(error)
);

// === ОБРАБОТКА 401 (опционально) ===
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem(ACCESS_TOKEN);
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;