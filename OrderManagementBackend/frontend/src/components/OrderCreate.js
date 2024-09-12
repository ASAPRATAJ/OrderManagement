import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { jwtDecode } from 'jwt-decode';

const OrderCreate = () => {
  const [products, setProducts] = useState([]);
  const [orderProducts, setOrderProducts] = useState([]);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const token = localStorage.getItem('token');
  let decodedToken = null;
  let userId = null;

  if (token) {
    try {
      decodedToken = jwtDecode(token);
      userId = decodedToken.user_id;
    } catch (error) {
      console.error('Error decoding token:', error);
    }
  }

  useEffect(() => {
    if (!token) {
      navigate('/login');
    }
  }, [token, navigate]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/products/', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setProducts(response.data);
        setOrderProducts(response.data.map(product => ({ product_id: product.id, quantity: 0 })));
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    if (token) {
      fetchProducts();
    }
  }, [token]);

  const handleQuantityChange = (index, value) => {
    const newOrderProducts = [...orderProducts];
    newOrderProducts[index].quantity = parseInt(value);
    setOrderProducts(newOrderProducts);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      user: userId,
      products: orderProducts.filter(product => product.quantity > 0),
    };

    try {
      const response = await axios.post('http://127.0.0.1:8000/api/orders/create/', data, {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      setMessage('Order created successfully!');
      console.log(response.data);
    } catch (error) {
      console.error(error);
      setMessage('Error creating order.');
    }
  };

  if (!token) {
    return <p>You must be logged in to create an order.</p>;
  }

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white shadow-md rounded-lg mt-10">
      <h2 className="text-2xl font-bold mb-6 text-center">Create Order</h2>
      {message && (
        <p className={`mb-4 text-center ${message.includes('successfully') ? 'text-green-500' : 'text-red-500'}`}>
          {message}
        </p>
      )}
      <form onSubmit={handleSubmit} className="space-y-6">
        <h3 className="text-xl font-semibold">Products</h3>
        {products.length === 0 ? (
          <p className="text-center">Loading products...</p>
        ) : (
          products.map((product, index) => (
            <div key={product.id} className="flex items-center space-x-4">
              <label className="w-1/2">{product.title}</label>
              <input
                type="number"
                value={orderProducts[index]?.quantity || 0}
                onChange={(e) => handleQuantityChange(index, e.target.value)}
                min="0"
                className="w-1/4 p-2 border border-gray-300 rounded-md"
              />
            </div>
          ))
        )}
        <button
          type="submit"
          className="w-full py-2 px-4 bg-blue-500 text-white font-semibold rounded-md hover:bg-blue-600 transition duration-300"
        >
          Create Order
        </button>
      </form>
    </div>
  );
};

export default OrderCreate;
