import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import ProductCreate from './components/ProductCreate';
import ProductList from './components/ProductList';
import UserCreate from './components/UserCreate';
import UserList from './components/UserList';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/product-create">Create Product</Link>
          </li>
          <li>
            <Link to="/product-list">Product List</Link>
          </li>
          <li>
            <Link to="/user-create">Create User</Link>
          </li>
          <li>
            <Link to="/user-list">User List</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/product-create" element={<ProductCreate />} />
        <Route path="/product-list" element={<ProductList />} />
        <Route path="/user-create" element={<UserCreate />} />
        <Route path="/user-list" element={<UserList />} />
      </Routes>
    </Router>
  );
}

export default App;
