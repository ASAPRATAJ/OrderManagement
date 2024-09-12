import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserOrderList = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [expandedOrderIds, setExpandedOrderIds] = useState([]); // Trzymamy ID rozwiniętych zamówień

  useEffect(() => {
    const token = localStorage.getItem('token');

    const fetchUserOrders = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/users/orders/', {
          headers: {
            Authorization: `Bearer ${token}`,
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

  // Funkcja do obsługi rozwijania i zwijania zamówień
  const toggleOrderDetails = (orderId) => {
    if (expandedOrderIds.includes(orderId)) {
      setExpandedOrderIds(expandedOrderIds.filter((id) => id !== orderId));
    } else {
      setExpandedOrderIds([...expandedOrderIds, orderId]);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p className="text-lg font-semibold">Loading orders...</p>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex justify-center items-center h-screen">
        <p className="text-red-500">{error}</p>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white shadow-md rounded-lg mt-10">
      <h2 className="text-2xl font-bold mb-6 text-center">Your Orders</h2>
      {orders.length === 0 ? (
        <p className="text-center">No orders found.</p>
      ) : (
        <div className="space-y-6">
          {orders.map((order) => (
            <div
              key={order.id}
              className="border border-gray-300 rounded-lg p-4 hover:shadow-lg transition duration-300"
            >
              <div className="flex justify-between items-center">
                <h3 className="text-xl font-semibold">Order ID: {order.id}</h3>
                <button
                  onClick={() => toggleOrderDetails(order.id)}
                  className="py-1 px-3 bg-blue-500 text-white rounded-md hover:bg-blue-600 transition duration-300"
                >
                  {expandedOrderIds.includes(order.id) ? 'Hide Details' : 'Show Details'}
                </button>
              </div>
              <p className="text-gray-600 mb-2">
                Created At: {new Date(order.created_at).toLocaleString()}
              </p>

              {/* Sekcja z produktami jest rozwijana/zwijana */}
              {expandedOrderIds.includes(order.id) && (
                <div className="mt-4">
                  <h4 className="text-lg font-semibold mb-2">Products:</h4>
                  <ul className="list-disc pl-6">
                    {order.products.map((product, index) => (
                      <li key={index} className="mb-1">
                        <strong>Product Name:</strong> {product.product_title} <br />
                        <strong>Quantity:</strong> {product.quantity}
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default UserOrderList;
