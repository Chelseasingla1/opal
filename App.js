// src/App.js
import React, { useEffect, useState } from 'react';

function App() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('http://localhost:3000/users')
            .then(response => response.json())
            .then(data => setUsers(data));
    }, []);

    return (
        <div>
            <h1>User Permissions</h1>
            <ul>
                {users.map(user => (
                    <li key={user.id}>{user.username}: {user.karma} - {user.location}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;
