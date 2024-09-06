import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import ProductCreate from './components/ProductCreate';
import ProductList from './components/ProductList';
import UserCreate from './components/UserCreate';
import UserList from './components/UserList';
import OrderCreate from './components/OrderCreate';
import OrderList from './components/OrderList';
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
          <li>
            <Link to="/order-create">Order Create</Link>
          </li>
          <li>
            <Link to="/order-list">Order List</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/product-create" element={<ProductCreate />} />
        <Route path="/product-list" element={<ProductList />} />
        <Route path="/user-create" element={<UserCreate />} />
        <Route path="/user-list" element={<UserList />} />
        <Route path="/order-create" element={<OrderCreate />} />
        <Route path="/order-list" element={<OrderList />} />
      </Routes>
    </Router>
  );
}

export default App;
