import React, { useState, useEffect } from 'react';
import axios from 'axios';

const OrderList = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/orders/'); // Endpoint do pobierania zamówień
        if (response.data.length === 0) {
          setError('No orders found.');
        } else {
          setOrders(response.data);
        }
      } catch (error) {
        console.error('Error fetching orders:', error);
        setError('Error fetching orders.');
      } finally {
        setLoading(false);
      }
    };

    fetchOrders();
  }, []);

  if (loading) {
    return <p>Loading orders...</p>;
  }

  return (
    <div>
      <h2>Order List</h2>
      {error ? (
        <p>{error}</p>
      ) : (
        <ul>
          {orders.map((order) => (
            <li key={order.id}>
              <h3>Order ID: {order.id}</h3>
              <p>User ID: {order.user}</p>
              <p>Created At: {order.created_at}</p>
              <h4>Products:</h4>
              <ul>
                {order.products.map((product, index) => (
                  <li key={index}>
                    Product Name: {product.product_title}, Quantity: {product.quantity}
                  </li>
                ))}
              </ul>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default OrderList;
