import React, { useState } from 'react';
import axios from 'axios';

function UserCreate() {
  const [email, setEmail] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState(''); // State na wiadomość z backendu
  const [error, setError] = useState('');     // State na wiadomości o błędach

  const handleSubmit = (e) => {
    e.preventDefault();
    setMessage(''); // Resetowanie wiadomości przed wysłaniem
    setError('');

    axios.post('http://127.0.0.1:8000/api/users/create/', {
      email,
      company_name: companyName,
      password,
    })
    .then((response) => {
      setMessage('User created successfully!'); // Wyświetlenie wiadomości o sukcesie
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        // Sprawdzenie czy są szczegóły odpowiedzi od backendu i wyświetlenie ich
        setError(error.response.data.detail || JSON.stringify(error.response.data));
      } else {
        setError('An error occurred. Please try again.');
      }
    });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div>
          <label>Company Name:</label>
          <input
            type="text"
            value={companyName}
            onChange={(e) => setCompanyName(e.target.value)}
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button type="submit">Register</button>
      </form>

      {/* Wyświetlenie wiadomości o sukcesie lub błędzie */}
      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default UserCreate;
