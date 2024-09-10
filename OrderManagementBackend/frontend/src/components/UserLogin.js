import React, { useState } from 'react';
import axios from 'axios';

const UserLogin = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        setError('');

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/users/token/create/', {
                email: email,  // W Django JWT TokenAuth standardowo używa pola "username" dla logowania
                password: password
            });

            // Przechwyć token i zapisz w localStorage
            const { access } = response.data;
            localStorage.setItem('token', access);

            alert('Logged in successfully!');
            // Możesz przekierować użytkownika lub wywołać inny komponent po zalogowaniu
        } catch (err) {
            setError('Login failed. Check your credentials.');
        }
    };

    return (
        <div>
            <h2>Login</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <form onSubmit={handleLogin}>
                <div>
                    <label>Email:</label>
                    <input
                        type="text"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label>Password:</label>
                    <input
                        type="password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    );
};

export default UserLogin;
