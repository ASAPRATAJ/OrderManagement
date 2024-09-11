import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProductCreate from './components/ProductCreate';
import ProductList from './components/ProductList';
import UserCreate from './components/UserCreate';
import UserList from './components/UserList';
import OrderCreate from './components/OrderCreate';
import OrderList from './components/OrderList';
import UserLogin from './components/UserLogin';
import UserLogout from './components/UserLogout';
import Navbar from './components/Navbar';
import UserOrderList from './components/UserOrderList'; // Import UserOrderList

const App = () => {
  return (
    <Router>
      <Navbar />
      <div style={{ paddingTop: '60px' }}>
        <Routes>
          <Route path="/" element={<h1>Welcome to MyApp</h1>} />
          <Route path="/login" element={<UserLogin />} />
          <Route path="/products/create" element={<ProductCreate />} />
          <Route path="/products" element={<ProductList />} />
          <Route path="/users/create" element={<UserCreate />} />
          <Route path="/users" element={<UserList />} />
          <Route path="/orders/create" element={<OrderCreate />} />
          <Route path="/orders" element={<OrderList />} />
          <Route path="/users/orders" element={<UserOrderList />} /> {/* Dodano ścieżkę do UserOrderList */}
          <Route path="/logout" element={<UserLogout />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
