import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import ProductCreate from './components/ProductCreate';
import ProductList from './components/ProductList';
import UserCreate from './components/UserCreate';
import UserList from './components/UserList';
import OrderCreate from './components/OrderCreate';
import OrderList from './components/OrderList';
import UserLogin from './components/UserLogin';
import Navbar from './components/Navbar'; // Importujemy Navbar

const App = () => {
  return (
    <Router>
      {/* Dodajemy Navbar, aby był wyświetlany na wszystkich stronach */}
      <Navbar />
      <div style={{ paddingTop: '60px' }}> {/* Padding dla treści, żeby nie nachodziła na Navbar */}
        <Routes>
          <Route path="/" element={<h1>Welcome to MyApp</h1>} /> {/* Strona główna */}
          <Route path="/login" element={<UserLogin />} />
          <Route path="/products/create" element={<ProductCreate />} />
          <Route path="/products" element={<ProductList />} />
          <Route path="/users/create" element={<UserCreate />} />
          <Route path="/users" element={<UserList />} />
          <Route path="/orders/create" element={<OrderCreate />} />
          <Route path="/orders" element={<OrderList />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
