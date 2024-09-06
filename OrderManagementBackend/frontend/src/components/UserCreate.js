import React, { useState } from 'react';
import axios from 'axios';

function UserCreate() {
  const [email, setEmail] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://127.0.0.1:8000/api/users/create/', {
      email,
      company_name: companyName,
      password,
    })
    .then((response) => {
      console.log(response.data);
      alert('User created successfully!');
    })
    .catch((error) => {
      console.error('There was an error creating the user!', error);
    });
  };

  return (
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
  );
}

export default UserCreate;
