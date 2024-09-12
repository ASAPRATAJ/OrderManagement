import React, { useState } from 'react';
import axios from 'axios';
import './UserCreate.css'; // Import pliku CSS

function UserCreate() {
  const [email, setEmail] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    setMessage('');
    setError('');

    axios.post('http://127.0.0.1:8000/api/users/create/', {
      email,
      company_name: companyName,
      password,
    })
    .then((response) => {
      setMessage('User created successfully!');
    })
    .catch((error) => {
      if (error.response && error.response.data) {
        setError(error.response.data.detail || JSON.stringify(error.response.data));
      } else {
        setError('An error occurred. Please try again.');
      }
    });
  };

  return (
    <div className="create-container">
      {message && <p className="success-message">{message}</p>}
      {error && <p className="error-message">{error}</p>}
      <form onSubmit={handleSubmit} className="create-form">
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
          <label>Company Name:</label>
          <input
            type="text"
            value={companyName}
            onChange={(e) => setCompanyName(e.target.value)}
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
        <button type="submit" className="create-button">Register</button>
      </form>
    </div>
  );
}

export default UserCreate;
