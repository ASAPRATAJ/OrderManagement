import React, { useState, useEffect } from 'react';
import axios from 'axios';

function OrderCreate() {
  const [users, setUsers] = useState([]);
  const [products, setProducts] = useState([]);
  const [selectedUser, setSelectedUser] = useState('');
  const [selectedProducts, setSelectedProducts] = useState({});
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  // Pobieranie listy użytkowników
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/users/')
      .then(response => {
        setUsers(response.data);
      })
      .catch(error => {
        setError('Failed to fetch users');
      });
  }, []);

  // Pobieranie listy produktów
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/products/')
      .then(response => {
        setProducts(response.data);
      })
      .catch(error => {
        setError('Failed to fetch products');
      });
  }, []);

  // Obsługa zmiany ilości produktu
  const handleProductQuantityChange = (e, productId) => {
    const quantity = parseInt(e.target.value, 10);

    setSelectedProducts(prevSelectedProducts => ({
      ...prevSelectedProducts,
      [productId]: quantity > 0 ? quantity : 0,
    }));
  };

  // Obsługa wysyłania formularza
  const handleSubmit = (e) => {
    e.preventDefault();

    // Filtracja produktów z ilością większą niż 0
    const selectedProductIds = Object.keys(selectedProducts).filter(
      (productId) => selectedProducts[productId] > 0
    );

    if (selectedProductIds.length === 0) {
      setError('Please select at least one product with a quantity greater than 0.');
      return;
    }

    const data = {
      user: selectedUser,
      products: selectedProductIds,
    };

    axios.post('http://127.0.0.1:8000/api/orders/create/', data)
      .then(response => {
        setMessage('Order created successfully!');
        setError('');
      })
      .catch(error => {
        if (error.response && error.response.data) {
          setError('Failed to create order: ' + JSON.stringify(error.response.data));
        } else {
          setError('An error occurred. Please try again.');
        }
      });
  };

  return (
    <div>
      <h2>Create Order</h2>
      <form onSubmit={handleSubmit}>
        {/* Wybór użytkownika */}
        <div>
          <label>User:</label>
          <select value={selectedUser} onChange={(e) => setSelectedUser(e.target.value)} required>
            <option value="">Select a user</option>
            {users.map(user => (
              <option key={user.id} value={user.id}>
                {user.company_name}
              </option>
            ))}
          </select>
        </div>

        {/* Wybór ilości produktów */}
        <div>
          <label>Products and Quantity:</label>
          {products.map(product => (
            <div key={product.id}>
              <label>{product.title}</label>
              <input
                type="number"
                min="0"
                value={selectedProducts[product.id] || 0}
                onChange={(e) => handleProductQuantityChange(e, product.id)}
                placeholder="Quantity"
              />
            </div>
          ))}
        </div>

        <button type="submit">Create Order</button>
      </form>

      {/* Wyświetlanie wiadomości o sukcesie lub błędzie */}
      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default OrderCreate;
