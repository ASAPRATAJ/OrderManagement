import React, { useEffect, useState } from 'react';
import axios from 'axios';

const UserList = () => {
    const [users, setUsers] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchUsers = async () => {
            const token = localStorage.getItem('token');
            if (!token) {
                setError('You are not authorized to view this content.');
                return;
            }

            try {
                const response = await axios.get('http://127.0.0.1:8000/api/users/', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });

                setUsers(response.data);
            } catch (err) {
                setError('Failed to fetch users. You may not have sufficient permissions.');
            }
        };

        fetchUsers();
    }, []);

    return (
        <div>
            <h2>User List</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {!error && (
                <ul>
                    {users.map((user) => (
                        <li key={user.id}>
                            {user.company_name} - {user.is_staff ? 'Staff' : 'Regular User'}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default UserList;
