// src/App.js
import React from 'react';
import ProductList from './components/ProductList';
import ProductForm from './components/ProductForm';
import UserRegistrationForm from './components/UserRegistrationForm';

function App() {
  return (
    <div className="App">
      <h1>Product Management</h1>
      <ProductForm />
      <ProductList />

      <h2>User Registration</h2>
      <UserRegistrationForm />
    </div>
  );
}

export default App;
