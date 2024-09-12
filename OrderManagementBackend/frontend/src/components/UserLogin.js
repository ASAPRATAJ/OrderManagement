import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';
import './UserLogin.css'; // Upewnij się, że dodajesz odpowiedni plik CSS

const UserLogin = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/users/token/create/', {
                email,
                password
            });

            const { access } = response.data;

            // Zapisanie tokenu do localStorage
            localStorage.setItem('token', access);

            // Dekodowanie tokenu, aby sprawdzić uprawnienia
            const decodedToken = jwtDecode(access);
            console.log('Decoded Token:', decodedToken);

            // Zapisanie informacji o użytkowniku do localStorage
            localStorage.setItem('user', JSON.stringify({
                isStaff: decodedToken.is_staff,
                isSuperUser: decodedToken.is_superuser,
            }));
            // Przekierowanie użytkownika na stronę główną
            navigate('/');

        } catch (error) {
            setError('Invalid email or password');
        }
    };

    return (
        <div className="login-container">
            {error && <p className="error-message">{error}</p>}
            <form onSubmit={handleSubmit} className="login-form">
                <div className="form-group">
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className="form-group">
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit" className="login-button">Login</button>
            </form>
        </div>
    );
};

export default UserLogin;
