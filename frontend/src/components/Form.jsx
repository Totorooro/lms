import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import LoadingIndicator from "./LoadingIndicator";
import "../styles/Form.css"; 

function Form() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();

        try {
            const res = await api.post("/api/login/", { username, password });
            localStorage.setItem(ACCESS_TOKEN, res.data.access);
            localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
            navigate("/home")
        } catch (error) {
            console.error(error.response ? error.response.data : error);
            alert(error.response ? error.response.data.detail || 'Error' : 'Error');
        } finally {
            setLoading(false)
        }
    };

    return (
        <>
            <form onSubmit={handleSubmit} className="form-container">
                <div className="form-logo">🎓</div>
                <h1>Вход в LMS</h1>
                <p className="form-description">Введите свои учетные данные для доступа к системе</p>
                <input
                    className="form-input"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Логин"
                />
                <input
                    className="form-input"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Пароль"
                />
                {loading && <LoadingIndicator />}
                <button className="form-button" type="submit">
                    Войти
                </button>
            </form>
        </>
    );
}

export default Form;