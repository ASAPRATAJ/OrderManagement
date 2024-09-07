import React, { useState, useEffect } from 'react';
import axios from 'axios';

function OrderList() {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState('');

  // Pobieranie zamówień z API
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/orders/')
      .then(response => {
        setOrders(response.data);
      })
      .catch(error => {
        setError('Failed to fetch orders.');
      });
  }, []);

  return (
    <div>
      <h2>Order List</h2>

      {/* Wyświetlanie błędu */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Wyświetlanie zamówień */}
      <ul>
        {orders.length === 0 ? (
          <p>No orders found.</p>
        ) : (
          orders.map(order => (
            <li key={order.id}>
              <p><strong>Order ID:</strong> {order.id}</p>
              <p><strong>User:</strong> {order.user.company_name}</p>
              <p><strong>Created At:</strong> {new Date(order.created_at).toLocaleString()}</p>
              <p><strong>Products:</strong></p>
              <ul>
                {order.products.map(product => (
                  <li key={product.id}>{product.title} (Price: {product.price})</li>
                ))}
              </ul>
            </li>
          ))
        )}
      </ul>
    </div>
  );
}

export default OrderList;
