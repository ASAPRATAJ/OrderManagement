import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserList() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/users/')
    .then((response) => {
      setUsers(response.data);
    })
    .catch((error) => {
      console.error('There was an error fetching the users!', error);
    });
  }, []);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.company_name}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UserList;
