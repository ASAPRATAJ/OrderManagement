import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserOrderList = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const token = localStorage.getItem('token'); // Pobieramy token z localStorage

    const fetchUserOrders = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/users/orders/', {
          headers: {
            Authorization: `Bearer ${token}`, // Dodajemy token w nagłówkach
          },
        });

        if (response.data.length === 0) {
          setError('No orders found.');
        } else {
          setOrders(response.data);
        }
      } catch (error) {
        console.error('Error fetching user orders:', error);
        setError('Error fetching user orders.');
      } finally {
        setLoading(false);
      }
    };

    fetchUserOrders();
  }, []);

  if (loading) {
    return <p>Loading orders...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <div>
      <h2>Your Orders</h2>
      {orders.length === 0 ? (
        <p>No orders found.</p>
      ) : (
        orders.map((order) => (
          <div key={order.id} style={{ border: '1px solid black', marginBottom: '20px', padding: '10px' }}>
            <h3>Order ID: {order.id}</h3>
            <p>Created At: {new Date(order.created_at).toLocaleString()}</p>
            <h4>Products:</h4>
            <ul>
              {order.products.map((product, index) => (
                <li key={index}>
                  <strong>Product Name:</strong> {product.product_title} <br />
                  <strong>Quantity:</strong> {product.quantity}
                </li>
              ))}
            </ul>
          </div>
        ))
      )}
    </div>
  );
};

export default UserOrderList;
